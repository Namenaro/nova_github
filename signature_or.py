class ORSignature: # программа ИЛИ других программ,возможно, многих
    def __init__(self, name, alternatives_list):
        self.name = name
        self.alternatives_list = alternatives_list # [ {eid1: eid1v1, eid2:eid2v1,...}, {eid1:eid1v2, eid2:eid2v2,...},... ]

