from agent.prop.helpers import *

class OrHub: # на схеме треугольник
    def __init__(self):
        self.top_node = None

        self.alternatives_list=[] #alternative = {new1:old1, ...}
        self.alternatives_exemplars_lists=[]  # у каждой из проверенных альтернатив хранится списко экземпляров

    def is_all_alternatives_checked(self):
        if len(self.alternatives_exemplars_lists)!= len(self.alternatives_list):
            return False
        return True

    def get_current_alternative(self):
        index_of_last_checked = len(self.alternatives_exemplars_lists)
        return self.alternatives_list[index_of_last_checked]

def make_remapping_exemplar(alternative, exemplar):
    return new_exemplar

def make_remapping_exemplars(alternative, exemplars):
    new_exemplars = []
    for exemplar in exemplars:
        new_exemplars.append(make_remapping_exemplar(alternative, exemplar))
    return new_exemplars

def back_remap_of_eid(altern_remap, eid):
    for k in altern_remap.keys():
        if altern_remap[k]==eid:
            return k
    assert False, "prop error 3: absent key in remapper of orhub"

def propagate_into_orhub(orhub, msg):
    if msg.type == FROM_TOP:
        return propagate_into_orhub_from_top(orhub, msg)
    if msg.type == FROM_DOWN:
        return propagate_into_orhub_from_down(orhub, msg)

def propagate_into_orhub_from_top(orhub, msg):
    altern_remap = orhub.get_current_alternative()
    first_old_eid = altern_remap[altern_remap.keys()[0]]
    new_bottom_hub = create_hub_by_eid(first_old_eid, top_hub=orhub)
    msg.eid = back_remap_of_eid(altern_remap, msg.eid)
    return new_bottom_hub, msg


def propagate_into_orhub_from_down(orhub, msg):
    orhub.alternatives_exemplars_lists.append(msg.exemplars)
    altern_remap = orhub.get_current_alternative()
    new_exemplars = make_remapping_exemplars(altern_remap, msg.exemplars)
    msg.exemplars = new_exemplars
    return orhub.top_node, msg
