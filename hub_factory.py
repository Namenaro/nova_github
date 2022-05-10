from signature_and import *
from signature_or import *
from signature_i import *
from globals import *
from hub_i import *
from hub_and import *
from hub_or import *
from hub_rw import *

def create_hub_by_eid(eid, parent):
    print("create hub")
    signature = globals.ltm.get_program_signature_by_eid(eid)
    if type(signature) == AndSignature:
        hub = AndHub(signature, parent)
        # и сразу создаем 2 rw-детей ему
        hub.rightRW = RemapperWrapper(signature.map2, hub)
        hub.leftRW = RemapperWrapper(signature.map1, hub)
        return hub
    if type(signature) == ORSignature:
        hub = OrHub(signature.alternatives_list, parent)
        return hub
    if type(signature) == ISignature:
        hub = IHub(signature, parent)
        return hub
    assert False, "Err: attempt to create wrong type of hub!"

