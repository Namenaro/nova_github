from utils.point import *

class ProgExemplar: # экземпляр активации программы
    def __init__(self, events_exemplars):
        self.events_exemplars=events_exemplars # {eid->abs_coord} # какие события были обнаружены в каких абсолютных координатах


def extract_cloud_from_exemplars_list_by_eid(eid, exemplars_list):
    points_cloud = []
    for prog_exemplar in exemplars_list:
        points_cloud.append(prog_exemplar.events_exemplars[eid])
    return points_cloud
