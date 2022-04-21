FROM_TOP = "from_top"
FROM_DOWN = "from_down"

class ProgExemplar: # экземпляр активации программы
    def __init__(self, events_exemplars):
        self.events_exemplars=events_exemplars # {eid->abs_coord} # какие события были обнаружены в каких абсолютных координатах

class Msg1:
    def __init__(self, eid, points):
        self.type = FROM_TOP
        self.eid = eid
        self.points = points

class Msg2:
    def __init__(self, exemplars):
        self.type = FROM_DOWN
        self.exemplars = exemplars