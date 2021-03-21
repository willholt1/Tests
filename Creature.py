class Creature(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, worldSize, direction):

        if (direction == "U" and self.y > 0):
            self.y -= 1
        elif (direction == "D" and self.y < (worldSize-1)):
            self.y += 1
        elif (direction == "L" and self.x > 0):
            self.x -= 1
        elif (direction == "R" and self.x < (worldSize-1)):
            self.x += 1
        else:
            print("invalid direction")

        print("x = {} & y = {}".format(self.x, self.y))
   
    def getPosition(self):
       print("x = {} & y = {}".format(self.x, self.y))
