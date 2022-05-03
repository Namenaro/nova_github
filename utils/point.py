class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self, other):
        if other.x == self.x and other.y==self.y:
            return True
        return False



