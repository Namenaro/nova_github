from agent.prop.helpers import *

class AndHub: # на схеме кружок
    def __init__(self):
        self.and_signature=None

        self.leftRW=None
        self.rightRW=None

        self.top_receiver=None  # либо OrHub либо RemapperWrapper

        self.left_pre_exemplars =[]
        self.right_pre_exemplars=[]

        self.current_RW_is_left = True


    def is_runnable(self):
        if len(self.left_pre_exemplars)!=0 and len(self.right_pre_exemplars)!=0:
            return True
        return False

    def run(self):
        new_exemplars = []
        for pre_left in self.left_pre_exemplars:
            for pre_right in self.right_pre_exemplars:
                new_exemplar = try_run_signature(self.and_signature, pre_left, pre_right)
                if new_exemplar is not None:
                    new_exemplars.append(new_exemplar)
        return new_exemplars

def try_run_signature(signature, left_exemplar, right_exemplar):
    return new_exemplar or None

def propagate_into_andhub(andhub, msg):
    if msg.type == FROM_TOP:
        return propagate_into_andhub_from_top(andhub, msg)
    if msg.type == FROM_DOWN:
        return propagate_into_andhub_from_down(andhub, msg)

def propagate_into_andhub_from_top(andhub, msg):
    pass

def propagate_into_andhub_from_down(andhub, msg):
    pass
