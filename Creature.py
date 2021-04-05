import Food
import random
import math
import arcade

#CONSTANTS
UP = 0
DOWN = 180
LEFT = 90
RIGHT = 270
MUTATION_RATE = 90

class Creature(arcade.Sprite):
    def __init__(self, image, speed, baseEnergy = None, viewDistance = None, movementEfficiency = None):

        super().__init__(image, 0.5)

        self.direction = 'U'
        self.foraging = False
        self.lastDirection = 'U'
        self.lastDirectionCount = 0
        #performance stats
        self.distanceTravelled = 0
        self.foodEaten = 0 
        self.freeMoves = 0
        self.children = 0

        if (baseEnergy is None):
            self.createValues(speed)
        elif (random.randint(0,100) < MUTATION_RATE):
            self.mutate(baseEnergy, viewDistance, movementEfficiency, speed)
        else:
            self.baseEnergy = baseEnergy
            self.energy = baseEnergy
            self.viewDistance = viewDistance
            self.movementEfficiency = movementEfficiency
            self.speed = speed

    def mutate(self, baseEnergy, viewDistance, movementEfficiency, speed):
        creatureProperties = [baseEnergy, viewDistance, movementEfficiency]
        i = random.randint(0,2)

        mutation = random.randint(0, round(creatureProperties[i]/8))
        creatureProperties[i] -= mutation
        i = random.randint(0,2)
        creatureProperties[i] += mutation

        self.baseEnergy = creatureProperties[0]
        self.energy = self.baseEnergy
        self.viewDistance = creatureProperties[1]
        self.movementEfficiency = creatureProperties[2]
        self.speed = speed


    def createValues(self, speed):
        #skill distribution
        energyPool = 500
        a = random.randint(1, energyPool)
        energyPool -= a
        b = random.randint(0, energyPool)
        c = energyPool -b

        self.baseEnergy = a
        self.energy = a
        self.viewDistance = b
        self.movementEfficiency = c

        self.speed = speed #random.randint(1,2)

    def move(self, worldSize):

        if (self.energy > 0):
            if (self.direction == 'U' and self.center_y < (worldSize-1)):
                self.center_y += self.speed
                self.distanceTravelled += 1
            elif (self.direction == 'D' and self.center_y > 1):
                self.center_y -= self.speed
                self.distanceTravelled += 1
            elif (self.direction == 'L' and self.center_x > 1):
                self.center_x -= self.speed
                self.distanceTravelled += 1
            elif (self.direction == 'R' and self.center_x < (worldSize-1)):
                self.center_x += self.speed
                self.distanceTravelled += 1

            if (self.direction == self.lastDirection):
                self.lastDirectionCount += 1
            else:
                self.lastDirectionCount = 0

            self.lastDirection = self.direction

            if (self.lastDirectionCount >= self.viewDistance):
                self.foraging = False

            if (self.movementEfficiency < random.randint(0, (self.movementEfficiency + 100))):
                self.energy -= 1
            else:
                self.freeMoves += 1
    
    def checkEat(self, food):
        #check if can eat any food
        for i in range (len(food)):
            eaten = arcade.check_for_collision(self, food[i])
            #if no food spotted, look for food                
            if (self.foraging == False):
                self.look(food[i])
            #if food is close, eat
            elif (eaten):
                self.eat(food[i])
                food[i].remove_from_sprite_lists()
                self.foraging = False
                break
            
        return food

    def eat(self, food):
        #increase energy by nutrition value of the food
        self.energy += food.energy
        self.foodEaten += 1

    def look(self, food):
        if ((self.center_y <= food.center_y <= (self.center_y + self.viewDistance)) and ((self.center_x - 5) <= food.center_x <= (self.center_x + 5))):
            self.direction = 'U'
            self.foraging = True
            self.angle = UP
        elif (((self.center_y - self.viewDistance) <= food.center_y <= self.center_y) and ((self.center_x - 5) <= food.center_x <= (self.center_x + 5))):
            self.direction = 'D'
            self.foraging = True
            self.angle = DOWN
        elif (((self.center_x - self.viewDistance) <= food.center_x <= self.center_x) and ((self.center_y - 5) <= food.center_y <= (self.center_y + 5))):
            self.direction = 'L'
            self.foraging = True
            self.angle = LEFT
        elif ((self.center_x <= food.center_x <= (self.center_x + self.viewDistance)) and ((self.center_y - 5) <= food.center_y <= (self.center_y + 5))):
            self.direction = 'R'
            self.foraging = True
            self.angle = RIGHT
        else:
            self.foraging = False
        

    def getInfo(self):
        print ('Energy = {} \n \
                Speed = {} \n \
                BaseEnergy = {} \n \
                ViewDistance = {} \n \
                MovementEfficiency = {} \n \
                FoodEaten = {} \n \
                DistanceTravelled = {} \n \
                FreeMoves = {} \n \
                Children = {} \n \
                Fitness = {}\n'\
                .format(self.energy,\
                        self.speed, \
                        self.baseEnergy,\
                        self.viewDistance,\
                        self.movementEfficiency,\
                        self.foodEaten,\
                        self.distanceTravelled,\
                        self.freeMoves,\
                        self.children,\
                        ((self.foodEaten + 1) * self.distanceTravelled)))
    
    def getFitness(self):
        #fitness = (self.foodEaten + 1) * self.distanceTravelled
        fitness = self.foodEaten
        print(fitness)
        if (self.speed == 1):
            f = open('dataOutput/HerbivoreStat.txt', 'a+')
            f.write('{}\n'.format(fitness))
            f.close()
        else:
            f = open('dataOutput/PredatorStat.txt', 'a+')
            f.write('{}\n'.format(fitness))
            f.close()

    def getPosition(self):
       print('x = {} & y = {}'.format(self.x, self.y))
