from utils.point import *
from globals import *
from utils.get_pixels import sense

class ISignature: # идентифицирующий
    def __init__(self, name, old_eid,new_eid, steps):
        self.name=name
        self.old_eid=old_eid
        self.new_eid=new_eid
        self.steps=steps

    def run(self, points):
        survived_points = []
        for point in points:
            if sense(picture=PIC, point=point) == 1:
               survived_points.apped(point)
        return survived_points

