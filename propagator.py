from hub_and_prop import *
from hub_or_prop import *
from hub_i_prop import *
from hub_rw_prop import *
from hub_factory import *



def propagate_step( target, msg):
    if type(target) == RemapperWrapper:
        new_target, new_msg = propagate_into_rw( target, msg)
    else:
        if type(target) == IHub:
            new_target, new_msg = propagate_into_ihub( target, msg)
        else:
            if type(target) == AndHub:
                new_target, new_msg = propagate_into_andhub( target, msg)
            else:
                if type(target) == OrHub:
                    new_target, new_msg = propagate_into_orhub( target, msg)
                else:
                    assert False, "error in prop 2: unknown type of target"
    return new_target, new_msg


def make_propagation(eid, points):
    print("start propagation...")
    top_hub = create_hub_by_eid( eid, parent=None)
    target = top_hub
    msg = MsgUncertainty(eid, points)

    while True:
        target, msg = propagate_step(target, msg)
        if target is None:
            return msg.exemplars