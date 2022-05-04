from messages import *
from prog_exemplar import *
from signature_and import *
from tables import *

class AndHub: # на схеме кружок
    def __init__(self, and_signature, parent):
        self.and_signature=and_signature

        self.leftRW=None
        self.rightRW=None

        self.parent=parent  # либо OrHub либо RemapperWrapper

        self.left_pre_exemplars =[]
        self.right_pre_exemplars=[]

        self.current_RW_is_left = True


    def is_runnable(self):
        if len(self.left_pre_exemplars) != 0 and len(self.right_pre_exemplars) != 0:
            return True
        return False

    def run(self):
        new_exemplars = []
        for pre_left in self.left_pre_exemplars:
            for pre_right in self.right_pre_exemplars:
                new_exemplar = self.and_signature.run(pre_left, pre_right)
                if new_exemplar is not {}:
                    new_exemplars.append(new_exemplar)
        return new_exemplars

#### Логика распространения сообщений через этот узел ###########
# -  У него всегда два ребенка типа hub_rw.
# -  У него всегда один родитель (один из списка: None, hub_rw, hub_or)

# - От родителя всегда приходит сообщение типа TYPE_UNSERTAINTY
# - и перенаправляется без изменений одному из детей (тому, в кого в ремаппере есть нужный eid)

# - От ребенка всегда приходит сообщение типа TYPE_EXEMPLARS, и возможны варианты его обработки:
# 1) FAIL-propagation: если сообщение от ребенка с пустым списком экземпляров -
# это значит, что данный ребенок провален, и потому обоих детей надо стереть,
# кроме того надо отправить родителю сообщение типа TYPE_EXEMPLARS с пустим списком экземпляров -
# так и родитель узнает, что этот хаб провален (провал распространяется по дереву хабов снизу вверх)
# 2) Если список не пуст и от другого ребенка уже раньше тоже приходил непустой список, то этот узел
# запускается на выполнение (по сигнатуре), результатом чего становится список уже его экземпляров
# реализации, который отправляется родитителю и имеет тип TYPE_EXEMPLARS
# 3) Если второй ребенок ранее ничего не присылал, то  конструируется  сообщение типа
# TYPE_UNSERTAINTY для распространения в него.

def propagate_into_andhub(andhub, msg):
    if msg.type == TYPE_UNSERTAINTY:
        return propagate_into_andhub_from_parent(andhub, msg)
    if msg.type == TYPE_EXEMPLARS:
        return propagate_into_andhub_from_child(andhub, msg)

def propagate_into_andhub_from_parent(andhub, msg):
    # без изменений передаем это сообщение одному из детей
    # в какого из двух детей его передать?
    if msg.eid in andhub.leftRW.eid_map.keys(): # в левого
        andhub.current_RW_is_left = True
        return andhub.leftRW, msg
    # если не в левого, то в правого
    andhub.current_RW_is_left = False
    return andhub.rightRW, msg


def propagate_into_andhub_from_child(andhub, msg):
    assert msg.type == TYPE_EXEMPLARS, "Err: child sent msg of wrong type into its parent and_hub!"
    if msg.is_failed():
       # удаляем детей и шлем сигнал о своем провале родителю
        del andhub.leftRW
        del andhub.rightRW
        return andhub.parent, msg

    if andhub.current_RW_is_left == True:
        andhub.left_pre_exemplars = msg.exemplars
    else:
        andhub.right_pre_exemplars = msg.exemplars

    if andhub.is_runnable(): # вверх
        exemplars = andhub.run()
        msg.exemplars = exemplars
        return andhub.top_receiver, msg
    else: # случай, когда на одном ребенке экземпляры есть, а на другом нет
        if andhub.current_RW_is_left == True:
            #если пришло слева, то оправляем вправо
            andhub.current_RW_is_left = False
            msg_to_right = create_msg_to_right(andhub.and_signature, exemplars_from_left=msg.exemplars)
            return andhub.rightRW, msg_to_right
        else:
            # если пришло справа, то оправляем влево
            andhub.current_RW_is_left = True
            msg_to_left = create_msg_to_left(andhub.and_signature, exemplars_from_right=msg.exemplars)
            return andhub.leftRW, msg_to_left


def create_msg_to_left(and_signature, exemplars_from_right):
    right_points = extract_cloud_from_exemplars_list_by_eid(and_signature.pre_eid_right, exemplars_from_right)
    left_points = and_signature.get_left_cloud_by_right_cloud(right_points)
    msg_to_left = MsgUncertainty(and_signature.pre_eid_left, list(left_points))
    return msg_to_left

def create_msg_to_right(and_signature, exemplars_from_left):
    left_points = extract_cloud_from_exemplars_list_by_eid(and_signature.pre_eid_left, exemplars_from_left)
    right_points = and_signature.get_right_cloud_by_left_cloud(left_points)
    msg_to_right = MsgUncertainty(and_signature.pre_eid_right, list(right_points))
    return msg_to_right



