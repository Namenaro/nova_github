from utils.get_pictures import *
from tables import *

class Globals:
    def __init__(self):
        self.pic = get_numbers_of_type(3)[0]
        self.ltm = LongTermMemory()

globals = Globals()


