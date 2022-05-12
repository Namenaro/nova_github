
class RemapperWrapper:  # на схеме прямоугольник с 2 рядами цифр
    def __init__(self,ID, map, parent):
        self.ID = ID
        self.eid_map = map # {new_eid1: old_eid1, new_eid2:old_eid2,...}
        self.parent = parent
        self.child = None

    def get_old_eid_by_new(self, new_eid):
        return self.eid_map[new_eid]



class OrHub: # на схеме треугольник
    def __init__(self, ID, alternatives_list, parent):
        self.ID = ID
        self.parent = parent
        self.alternatives_list=alternatives_list  #alternative = {new1:old1, ...}, и вот их таких список []
        self.child = None
        self.last_condition_msg = None

    def is_all_alternatives_checked(self):
        if len(self.alternatives_list)>0:
            return False
        return True

    def remove_current_alternative(self):
        del self.child
        self.child = None
        self.alternatives_list.pop(0) # удаляем первый элемент списка

    def get_actual_alternative(self):
        return self.alternatives_list[0]


class IHub: # на схеме обведенный кружочек
    def __init__(self,ID,  i_signature, parent):
        self.ID = ID
        self.i_signature=i_signature
        self.parent = parent  #  RW or OrHub or None

    def run(self, points, pic):
        new_eid = self.i_signature.new_eid
        survived_points = self.i_signature.run(points, pic)
        return new_eid, survived_points


class AndHub: # на схеме кружок
    def __init__(self, ID, and_signature, parent):
        self.ID = ID
        self.and_signature=and_signature

        self.leftRW=None
        self.rightRW=None

        self.parent=parent  # либо OrHub либо RemapperWrapper

        self.left_pre_exemplars =[]
        self.right_pre_exemplars=[]

        self.current_RW_is_left = True


    def is_runnable(self):
        if len(self.left_pre_exemplars) != 0 and len(self.right_pre_exemplars) != 0:
            return True
        return False

    def run(self):
        new_exemplars = []
        for pre_left in self.left_pre_exemplars:
            for pre_right in self.right_pre_exemplars:
                new_exemplar = self.and_signature.run(pre_left, pre_right)
                if new_exemplar is not {}:
                    new_exemplars.append(new_exemplar)
        return new_exemplars
