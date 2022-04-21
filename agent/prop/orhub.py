class OrHub: # на схеме треугольник
    def __init__(self):
        self.parentRW = None

        self.alternatives_list=[]
        self.alternatives_flags=[]
        self.current_alternative_index=None

    def on_msg_from_top(self, top_eid, points):
        pass

    def on_msg_from_bottom(self, exemplars):
        pass

    def switch_alternative(self):
        pass

    def is_all_alternatives_checked(self):
        pass
