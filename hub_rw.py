from messages import *
from hub_factory import *

class RemapperWrapper:  # на схеме прямоугольник с 2 рядами цифр
    def __init__(self, eid_map, parent):
        self.eid_map = eid_map# {new_eid1: old_eid1, new_eid2:old_eid2,...}

        self.parent = parent
        self.child = None

    def get_bottom_eid_by_top(self, top_eid):
        return self.eid_map[top_eid]

##############################################################
def propagate_into_rw(rw, msg):
    if msg.type == TYPE_CONDITION:
        return propagate_into_rw_from_top(rw, msg)
    if msg.type == TYPE_EXEMPLARS:
        return propagate_into_rw_from_down(rw, msg)

def propagate_into_rw_from_top(rw, msg):
    new_eid = rw.get_bottom_eid_by_top(msg.eid)
    msg = MsgUncertainty(new_eid, msg.points)
    if rw.child is None:
        create_hub_by_eid(rw.eid_map[new_eid], parent=rw)
    return rw.child, msg

def propagate_into_rw_from_down(rw, msg):
    return rw.parent, msg