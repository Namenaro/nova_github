from messages import *
from hub_factory import *
from prog_exemplar import *
from prop_visualiser import VIS

#### Логика распространения сообщений через этот узел ###########
# Его родитель всегда это and_hub
# Его ребенок  всегда один (и он один из списка: i_hub, and_hub, or_hub)

# Сообщение от родителя всегда типа TYPE_CONDITION. Реацикя на него -
# просто переправить его ребенку, заменив eid с нового на старый

# Cообщение от ребенка всегда типа TYPE_EXEMPLARS. Если оно пустое,
# то ребенка уничтожить, и переслать пустое сообщение своему родителю.
# Если не пустое, просто отпавить родителю.

def propagate_into_rw(rw_hub, msg):
    if msg.type == TYPE_CONDITION:
        return propagate_into_rw_from_parent( rw_hub, msg)
    if msg.type == TYPE_EXEMPLARS:
        return propagate_into_rw_from_child( rw_hub, msg)

def propagate_into_rw_from_parent(rw_hub, msg):
    old_eid = rw_hub.get_old_eid_by_new(msg.eid)
    msg.eid = old_eid
    if rw_hub.child is None:
        rw_hub.child = create_hub_by_eid(old_eid, parent=rw_hub)
    VIS.EVENT_rw_hub_sent_uncertainty_to_child(ID=rw_hub.ID, uncert_msg=msg)
    return rw_hub.child, msg

def propagate_into_rw_from_child(rw_hub, msg):
    if msg.is_failed():
        VIS.EVENT_rw_hub_failed(rw_hub.ID)
        del rw_hub.child
    VIS.EVENT_rw_hub_obtained_exemplars_from_child(rw_hub.ID, msg)
    return rw_hub.parent, msg



