from messages import *

class RemapperWrapper:  # на схеме прямоугольник с 2 рядами цифр
    def __init__(self):
        self.eid_map = {}  # верхний ряд цифр на схеме -> нижний ряд цифр на схеме

        self.top_hub = None
        self.bottom_hub = None

    def get_bottom_eid_by_top(self, top_eid):
        return self.eid_map[top_eid]

##############################################################
def propagate_into_rw(rw, msg):
    if msg.type == TYPE_UNSERTAINTY:
        return propagate_into_rw_from_top(rw, msg)
    if msg.type == TYPE_EXEMPLARS:
        return propagate_into_rw_from_down(rw, msg)

def propagate_into_rw_from_top(rw, msg):
    new_eid = rw.get_bottom_eid_by_top(msg.eid)
    msg = MsgUncertainty(new_eid, msg.points)
    if rw.bottom_hub is None:
        rw.bottom_hub = create_hub_by_eid(new_eid)
    return rw.bottom_hub, msg

def propagate_into_rw_from_down(rw, msg):
    return rw.top_hub, msg