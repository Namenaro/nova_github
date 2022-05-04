from utils.point import *

class ProgExemplar: # экземпляр активации программы
    def __init__(self, events_exemplars):
        self.events_exemplars=events_exemplars # {eid->abs_coord} # какие события были обнаружены в каких абсолютных координатах


def extract_cloud_from_exemplars_list_by_eid(eid, exemplars_list):
    points_cloud = []
    for prog_exemplar in exemplars_list:
        points_cloud.append(prog_exemplar.events_exemplars[eid])
    return points_cloud

def remap_exemplar_old_to_new(map, exemplar):
    new_exemplar = {}
    for new_eid, old_eid in map.items():
        new_exemplar[new_eid]=exemplar[old_eid]
    return new_exemplar

def remap_exemplars_old_to_new(map, exemplars):
    new_exemplars = []
    for exemplar in exemplars:
        new_exemplars.append(remap_exemplar_old_to_new(map, exemplar))
    return new_exemplars