from prog_exemplar import *
from messages import *
from globals import *
from prop_visualiser import VIS


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
    new_eid, survived_points = ihub.run(msg.points,pic=globs.pic)
    exemplars = points_to_exemplars(new_eid, survived_points)
    msg1 = MsgExemplars(exemplars)
    VIS.EVENT_i_hub_run(ID=ihub.ID, uncertainty_msg=msg, exemplars_msg=msg1)
    return ihub.parent, msg1