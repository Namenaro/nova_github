TYPE_UNSERTAINTY = "from_top"
TYPE_EXEMPLARS = "from_down"

class MsgUncertainty:
    def __init__(self, eid, points):
        self.type = TYPE_UNSERTAINTY
        self.eid = eid
        self.points = points

class MsgExemplars:
    def __init__(self, exemplars):
        self.type = TYPE_EXEMPLARS
        self.exemplars = exemplars

    def is_failed(self):
        return len(self.exemplars) == 0



