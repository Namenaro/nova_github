#=====сущности из долгорочной памяти===========
class AndSignature: # коннектор 2 программ действием dx, dy с неопределенностьью dactions
    def __init__(self, name, eid1new, eid2new, dx, dy, dactions, map1, map2):
        self.name=name
        self.eid1new=eid1new
        self.eid2new=eid2new
        self.dx=dx
        self.dy=dy
        self.dactions=dactions # список точк в локальной с.к.
        self.map1=map1#{some_new_eid1:some_old1, some_new_eid2:some_old2...}
        self.map2=map2 #{...}

class ISignature: # идентифицирующий
    def __init__(self, name, old_eid,new_eid, steps):
        self.name=name
        self.old_eid=old_eid
        self.new_eid=new_eid
        self.steps=steps

class ORSignature: # программа ИЛИ других программ,возможно, многих
    def __init__(self):
        self.name=None
        self.or_map={} #  {or_eid1:[eid11, eid21,...],
                       #...,
                       #or_eidn:[eid1n, eid2n,...]}

    def get_num_alternatives(self):
        pass

    def get_alternative_mapping_by_index(self, index):
        pass

# основная интерфейсная функция для таблиц
def get_program_signature_by_eid(eid):
    return ORSignature or ISignature or AndSignature







