from messages import *
from hub_factory import *
from prog_exemplar import *

class RemapperWrapper:  # на схеме прямоугольник с 2 рядами цифр
    def __init__(self, map, parent):
        self.map = map # {new_eid1: old_eid1, new_eid2:old_eid2,...}
        self.parent = parent
        self.child = None

    def get_old_eid_by_new(self, new_eid):
        return self.map[new_eid]


#### Логика распространения сообщений через этот узел ###########
# Его родитель всегда это and_hub
# Его ребенок  всегда один (и он один из списка: i_hub, and_hub, or_hub)

# Сообщение от родителя всегда типа TYPE_CONDITION. Реацикя на него -
# просто переправить его ребенку, заменив eid с нового на старый

# Cообщение от ребенка всегда типа TYPE_EXEMPLARS. Если оно пустое,
# то ребенка уничтожить, и переслать пустое сообщение своему родителю.
# Если не пустое, то сделать ему ремаппинг от старого к новому и отпавить родителю.

def propagate_into_rw(rw_hub, msg):
    if msg.type == TYPE_CONDITION:
        return propagate_into_rw_from_parent(rw_hub, msg)
    if msg.type == TYPE_EXEMPLARS:
        return propagate_into_rw_from_child(rw_hub, msg)

def propagate_into_rw_from_parent(rw_hub, msg):
    old_eid = rw_hub.get_old_eid_by_new(msg.eid)
    msg.eid = old_eid
    if rw_hub.child is None:
        create_hub_by_eid(rw_hub.eid_map[old_eid], parent=rw_hub)
    return rw_hub.child, msg

def propagate_into_rw_from_child(rw_hub, msg):
    if msg.is_failed():
        del rw_hub.child
        return rw_hub.parent, msg
    #Если не пустое, то сделать ему ремаппинг от старого к новому и отпавить родителю

    mapped_exemplars = remap_exemplars_old_to_new(rw_hub.map, msg.exemplars)
    msg.exemplars = mapped_exemplars
    return rw_hub.parent, msg


