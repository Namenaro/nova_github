from agent.prop.helpers import *
from agent.prop.andhub import *
from agent.prop.orhub import *
from agent.prop.ihub import *
from agent.prop.rw import *

def progagate(target, msg):
    if type(target) == RemapperWrapper:
        new_target, new_msg = propagate_into_rw(target, msg)
    else:
        if type(target) == IHub:
            new_target, new_msg = propagate_into_ihub(target, msg)
        else:
            if type(target) == AndHub:
                new_target, new_msg = propagate_into_andhub(target, msg)
    return new_target, new_msg


def make_propagation(eid, points):
    top_hub = create_hub_by_eid(eid)
    target = top_hub
    msg = Msg1(eid, points)
    return_hubs = []
    while True:
        target, msg = progagate(target, msg)
        if msg is None:
            if len(return_hubs) ==0:
                break
            else:
                #TODO restart from last return hub
        if target is None:
            break
    return top_hub.exemplars