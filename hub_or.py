from messages import *
from hub_factory import *

import copy

class OrHub: # на схеме треугольник
    def __init__(self, alternatives_list, parent):
        self.parent = parent
        self.alternatives_list=alternatives_list  #alternative = {new1:old1, ...}, и вот их таких список []
        self.child = None
        self.last_condition_msg = None

    def is_all_alternatives_checked(self):
        if len(self.alternatives_list)>0:
            return False
        return True

    def remove_current_alternative(self):
        del self.child
        self.child = None
        self.alternatives_list.pop(0) # удаляем первый элемент списка

    def get_actual_alternative(self):
        return self.alternatives_list[0]


#### Логика распространения сообщений через этот узел ###########
# -  Его один ребенок: либо hub_and, либо hub_or.
# -  Его один родитель (один из списка: None, hub_rw, hub_or)

# - От родителя всегда приходит сообщение типа TYPE_CONDITION.
# В ответ выбираем текущую альтернативу,создаем под нее ребенка,
# подменяем eid в сообщении (новый на старый), и шлем его ребенку. Cамо сообщение
# запоминаем на узле, оно может понадобиться в будущем при переключении
# альтернатив на этом узле (т.е. если одна зафейлится, то надо будет
# это сообщение слать в другую)

# - От ребенка всегда приходит сообщение типа TYPE_EXEMPLARS.
#  1) FAIL-propagation: если сообщение от ребенка, что данный ребенок провален,
#  то его надо стереть, его альтернативу удалить. Если других альтернатив уже не осталось,
#  то надо послать родителю сообщение о провале. Если еще есть, то распространяем
#  ранее запомненное CONDITION-сообщение в следующую альтернативу (создав под нее ребенка)
# 2) Если сообщение от ребенка валидное, то делаем ремаппинг всех экземпляров
# (старое меняем на новое) и шлем родителю.
#

def propagate_into_orhub(orhub, msg):
    if msg.type == TYPE_CONDITION:
        return propagate_into_orhub_from_parent(orhub, msg)
    if msg.type == TYPE_EXEMPLARS:
        return propagate_into_orhub_from_child(orhub, msg)

def propagate_into_orhub_from_parent(orhub, msg):
    orhub.last_condition_msg = copy.deepcopy(msg)
    remap = orhub.get_actual_alternative()
    some_old_eid = remap[remap.keys()[0]]
    orhub.chid = create_hub_by_eid(some_old_eid, orhub)
    msg.eid = remap[msg.eid]
    return orhub.child, msg

def propagate_into_orhub_from_child(orhub, msg):
    if msg.is_failed(): #если текущий ребенок провален,
        orhub.remove_current_alternative() # то удяляем его и,
        if orhub.is_all_alternatives_checked(): # если больше детей нельзя создать,
            msg = MsgExemplars([])
            return orhub.parent, msg # то шлем родителю сообщение уже о своем провале
        else:
            #  иначе распространяем ранее запомненное CONDITION-сообщение
            #  в следующую альтернативу (создав под нее ребенка)
            # и подменив в сообщении новый eid на старый по актуальному ремаппингу
            map = orhub.get_actual_alternative()
            some_old_eid = map[map.keys()[0]]
            orhub.child = create_hub_by_eid(some_old_eid, orhub)
            new_msg = copy.deepcopy(orhub.last_condition_msg)
            new_msg.eid = map[msg.eid]
            return orhub.child, new_msg
    # Если же сообщение с экземплярами было валидным, то
    # делаем ремаппинг всех его экземпляров (старого на новое) и пересылаем его родителю
    map = orhub.get_actual_alternative()
    msg.exemplars = remap_exemplars_old_to_new(map, msg.exemplars)
    return orhub.parent, msg


def remap_exemplar_old_to_new(map, exemplar):
    new_exemplar = {}
    for new_eid, old_eid in map.items():
        new_exemplar[new_eid]=exemplar[old_eid]
    return new_exemplar

def remap_exemplars_old_to_new(map, exemplars):
    new_exemplars = []
    for exemplar in exemplars:
        new_exemplars.append(remap_exemplar_old_to_new(map, exemplar))
    return new_exemplars