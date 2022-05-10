from signatures import *
from hubs import *
from globals import *

def create_hub_by_eid(eid, parent):

    signature = globs.ltm.get_program_signature_by_eid(eid)
    if type(signature) == AndSignature:
        hub = AndHub(signature, parent)
        # и сразу создаем 2 rw-детей ему
        hub.rightRW = RemapperWrapper(signature.map2, hub)
        hub.leftRW = RemapperWrapper(signature.map1, hub)
        print ("AND hub created:" + str(signature.name))
        return hub
    if type(signature) == ORSignature:
        hub = OrHub(signature.alternatives_list, parent)
        print("Or hub created:" + str(signature.name))
        return hub
    if type(signature) == ISignature:
        hub = IHub(signature, parent)
        print("I hub created:" + str(signature.name))
        return hub
    assert False, "Err: attempt to create wrong type of hub!"

