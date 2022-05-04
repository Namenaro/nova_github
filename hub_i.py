class IHub: # на схеме обведенный кружочек
    def __init__(self, i_signature, parent):
        self.i_signature=i_signature
        self.parent = parent  #  RW or OrHub or None

    def run(self, points):
        return new_eid, survived_points
###################################################################
def i_points_to_exemplars(eid, points):
    exemplars = []
    for point in points:
        exemplar = ProgExemplar({eid:point})
        exemplars.append(exemplar)
    return exemplars

def propagate_into_ihub(target, msg):
    assert msg.type!=FROM_TOP, "propagator error 1: wrong type of msg into IHub"
    new_eid, survived_points = target.run(msg.points)
    exemplars = i_points_to_exemplars(new_eid, survived_points)
    msg = Msg2(exemplars)
    return target.top_node, msg