class Food(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nutrition = 15

    def getPosition(self):
       print('x = {} & y = {}'.format(self.x, self.y))