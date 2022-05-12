from signatures import *
from hubs import *
from globals import *

def create_hub_by_eid(eid, parent):
    ID = globs.hub_id_gen.get_id()
    signature = globs.ltm.get_program_signature_by_eid(eid)
    if type(signature) == AndSignature:
        hub = AndHub(ID,signature, parent)
        # и сразу создаем 2 rw-детей ему
        ID1 = globs.hub_id_gen.get_id()
        ID2 = globs.hub_id_gen.get_id()
        hub.rightRW = RemapperWrapper(ID1,signature.map2, hub)
        hub.leftRW = RemapperWrapper(ID2,signature.map1, hub)
        print ("AND hub created:" + str(signature.name))
        return hub
    if type(signature) == ORSignature:
        hub = OrHub(ID, signature.alternatives_list, parent)
        print("Or hub created:" + str(signature.name))
        return hub
    if type(signature) == ISignature:
        hub = IHub(ID, signature, parent)
        print("I hub created:" + str(signature.name))
        return hub
    assert False, "Err: attempt to create wrong type of hub!"

