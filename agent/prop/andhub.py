from agent.prop.helpers import *

class AndHub: # на схеме кружок
    def __init__(self):
        self.and_signature=None

        self.leftRW=None
        self.rightRW=None

        self.top_receiver=None  # либо OrHub либо RemapperWrapper

        self.left_pre_exemplars =[]
        self.right_pre_exemplars=[]

        self.current_RW_is_left = True


    def is_runnable(self):
        if len(self.left_pre_exemplars)!=0 and len(self.right_pre_exemplars)!=0:
            return True
        return False

    def run(self):
        new_exemplars = []
        for pre_left in self.left_pre_exemplars:
            for pre_right in self.right_pre_exemplars:
                new_exemplar = try_run_signature(self.and_signature, pre_left, pre_right)
                if new_exemplar is not None:
                    new_exemplars.append(new_exemplar)
        return new_exemplars

def try_run_signature(signature, left_exemplar, right_exemplar):
    return new_exemplar or None

def propagate_into_andhub(andhub, msg):
    if msg.type == FROM_TOP:
        return propagate_into_andhub_from_top(andhub, msg)
    if msg.type == FROM_DOWN:
        return propagate_into_andhub_from_down(andhub, msg)

def propagate_into_andhub_from_top(andhub, msg):
    # в какого из двух детей его передать?
    if msg.eid in andhub.leftRW.eid_map.keys():
        andhub.current_RW_is_left = True
        return andhub.leftRW, msg

    andhub.current_RW_is_left = False
    return andhub.rightRW, msg

def create_msg_to_left(and_signature, exemplars_from_right):
    msg_to_left = Msg1(eid, points)
    return msg_to_left

def create_msg_to_right(and_signature, exemplars_from_left):
    msg_to_right = Msg1(eid, points)
    return msg_to_right

def propagate_into_andhub_from_down(andhub, msg):
    if andhub.current_RW_is_left == True:
        andhub.left_pre_exemplars = msg.exemplars
    else:
        andhub.right_pre_exemplars = msg.exemplars

    if andhub.is_runnable(): # вверх
        exemplars = andhub.run()
        msg.exemplars = exemplars
        return andhub.top_receiver, msg
    else: #вбок
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


