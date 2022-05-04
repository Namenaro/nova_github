from prog_exemplar import *
from messages import *

class IHub: # на схеме обведенный кружочек
    def __init__(self, i_signature, parent):
        self.i_signature=i_signature
        self.parent = parent  #  RW or OrHub or None

    def run(self, points):
        new_eid = self.i_signature.new_eid
        survived_points = self.i_signature.run(points)
        return new_eid, survived_points


#### Логика распространения сообщений через этот узел ###########
# - У него не может быть детей
# - У него один родитель.
# Получать он может только сообщение типа TYPE_CONDITION (только от родителя).
# В ответ посылает родителю сообщение типа TYPE_EXEMPLARS

def points_to_exemplars(eid, points):
    exemplars = []
    for point in points:
        exemplar = ProgExemplar({eid:point})
        exemplars.append(exemplar)
    return exemplars

def propagate_into_ihub(ihub, msg):
    assert msg.type == TYPE_CONDITION, "ERR: wrong type of msg into IHub"
    new_eid, survived_points = ihub.run(msg.points)
    exemplars = points_to_exemplars(new_eid, survived_points)
    msg = MsgExemplars(exemplars)
    return ihub.parent, msg