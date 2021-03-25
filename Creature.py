import Food
import random
import math

class Creature(object):
    def __init__(self, x, y):
        #position
        self.x = x
        self.y = y
        
        self.direction = 'R'
        self.foraging = False
        
        #performance stats
        self.fitness = 0
        self.foodEaten = 0 
        self.freeMoves = 0
        self.children = 0

        #skill distribution
        energyPool = 500
        a = random.randint(0, energyPool)
        energyPool -= a
        b = random.randint(0, energyPool)
        c = energyPool -b

        self.baseEnergy = a
        self.energy = a
        self.viewDistance = b
        self.movementEfficiency = c

    def move(self, worldSize):

        if (self.energy > 0):
            if (self.direction == 'U' and self.y < (worldSize-1)):
                self.y += 1
                self.fitness += 1
            elif (self.direction == 'D' and self.y > 1):
                self.y -= 1
                self.fitness += 1
            elif (self.direction == 'L' and self.x > 1):
                self.x -= 1
                self.fitness += 1
            elif (self.direction == 'R' and self.x < (worldSize-1)):
                self.x += 1
                self.fitness += 1

            if (self.movementEfficiency < random.randint(0, (self.movementEfficiency + 100))):
                self.energy -= 1
            else:
                self.freeMoves += 1
    
    def checkEat(self, food):
        #check if can eat any food
        for i in range (len(food)):
            distance = math.sqrt( (food[i].x - self.x)**2 + (food[i].y - self.y)**2 )
            #if food is close, eat
            if (distance <= 10):
                self.eat(food[i])
                del food[i]
                self.foraging = False
                break
            #if no food spotted, look for food                
            elif (self.foraging == False):
                self.look(food[i])
        return food

    def eat(self, food):
        #increase energy by nutrition value of the food
        self.energy += food.nutrition
        self.foodEaten += 1

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

    def getInfo(self):
        print ('Energy = {} \n \
                BaseEnergy = {} \n \
                FoodEaten = {} \n \
                ViewDistance = {} \n \
                MovementEfficiency = {} \n \
                FreeMoves = {} \n \
                Children = {} \n \
                Fitness = {}'\
                .format(self.energy,\
                        self.baseEnergy,\
                        self.foodEaten,\
                        self.viewDistance,\
                        self.movementEfficiency,\
                        self.freeMoves,\
                        self.children,\
                        self.fitness))

    def getPosition(self):
       print('x = {} & y = {}'.format(self.x, self.y))
