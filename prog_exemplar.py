class ProgExemplar: # экземпляр активации программы
    def __init__(self, events_exemplars):
        self.events_exemplars=events_exemplars # {eid->abs_coord} # какие события были обнаружены в каких абсолютных координатах