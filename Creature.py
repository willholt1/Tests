import Food
import random

class Creature(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 200
        self.viewDistance = random.randint(50,100)
        self.direction = 'R'
        self.foraging = False
        self.fitness = 0

    def move(self, worldSize):

        if (self.energy > 0):
            if (self.direction == 'U' and self.y < (worldSize-1)):
                self.y += 1
            elif (self.direction == 'D' and self.y > 1):
                self.y -= 1
            elif (self.direction == 'L' and self.x > 1):
                self.x -= 1
            elif (self.direction == 'R' and self.x < (worldSize-1)):
                self.x += 1

            self.energy -= 1
            self.fitness += 1
    
    def eat(self, food):
        #increase energy by nutrition value of the food
        self.energy += food.nutrition
        print('Energy = {}  ViewDistance = {}  Fitness = {}'.format(self.energy, self.viewDistance, self.fitness))

    def look(self, food):
        if ((self.y <= food.y <= (self.y + self.viewDistance)) and ((self.x - 5) <= food.x <= (self.x + 5))):
            self.direction = 'U'
            self.foraging = True
        elif (((self.y - self.viewDistance) <= food.y <= self.y) and ((self.x - 5) <= food.x <= (self.x + 5))):
            self.direction = 'D'
            self.foraging = True
        elif (((self.x - self.viewDistance) <= food.x <= self.x) and ((self.y - 5) <= food.y <= (self.y + 5))):
            self.direction = 'L'
            self.foraging = True
        elif ((self.x <= food.x <= (self.x + self.viewDistance)) and ((self.y - 5) <= food.y <= (self.y + 5))):
            self.direction = 'R'
            self.foraging = True
        else:
            self.foraging = False


    def getPosition(self):
       print('x = {} & y = {}'.format(self.x, self.y))
