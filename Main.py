import arcade
import random
import math
import os
#classes
import Creature
import Food

class myWindow (arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHEAT)

        self.worldSize = width
        self.startup()
        

    def startup(self):
        #number of creatures
        population = 100
        
        #food spawn variables
        self.foodDensity = 20
        foodMultiplier = 1
        
        #how far from the edge of the screen entities must spawn
        self.spawnBorder = 50

        #create herbivores
        self.herbivores = arcade.SpriteList()
        for i in range(round(population * 0.9)):
            animat = Creature.Creature('sprites/creature_blue.png', 1)
            animat.center_x = random.randint(self.spawnBorder, (self.worldSize - self.spawnBorder))
            animat.center_y = random.randint(self.spawnBorder, (self.worldSize - self.spawnBorder))
            
            self.herbivores.append(animat)
        
        #create predators
        self.predators = arcade.SpriteList()
        for i in range(round(population * 0.05)):
            animat = Creature.Creature('sprites/creature_red.png', 2)
            animat.center_x = random.randint(self.spawnBorder, (self.worldSize - self.spawnBorder))
            animat.center_y = random.randint(self.spawnBorder, (self.worldSize - self.spawnBorder))

            self.predators.append(animat) 

        #create food
        self.foodList = arcade.SpriteList()
        for i in range(population * foodMultiplier):
            self.replenishFood()

    #create food clumps
    def replenishFood(self):
        x = random.randint(self.spawnBorder, (self.worldSize - self.spawnBorder))
        y = random.randint(self.spawnBorder, (self.worldSize - self.spawnBorder))
        for j in range(random.randint(1, 6)):
            foodSprite = Food.Food('sprites/plant.png')
            foodSprite.center_x = x + random.randint(-self.foodDensity,self.foodDensity)
            foodSprite.center_y = y + random.randint(-self.foodDensity,self.foodDensity)
            self.foodList.append(foodSprite)

    def on_draw(self):

        arcade.start_render()
        #render food
        self.foodList.draw()
        #render herbivores
        self.herbivores.draw()
        #render predators
        self.predators.draw()
        
        
        #population counters
        arcade.draw_text("Food Count:    {}".format(len(self.foodList)), 5, 5, arcade.color.BLACK, 12)
        arcade.draw_text("H Population:  {}".format(len(self.herbivores)), 5, 20, arcade.color.BLACK, 12)
        arcade.draw_text("P Population:  {}".format(len(self.predators)), 5, 35, arcade.color.BLACK, 12)
        

    def on_update(self, delta_time):
        #chance more food is generated. if more creatures, greater chance for food to be generated
        if ((random.randint(0,100) < (30 - round(len(self.herbivores)/4))) and (len(self.foodList) < 500)):
            self.replenishFood()

        self.updatePredators()

        self.updateHerbivores()

        if ((len(self.herbivores) == 0) or (len(self.predators) == 0)):
            self.startup()

    def updatePredators(self):
        for i in range(len(self.predators)):
            self.predators[i].move(self.worldSize)

            #check if any food is close enough to eat, if so eat it
            self.herbivores = self.predators[i].checkEat(self.herbivores)

            #creatures die if they run out of energy and reproduce if they meet a threshold
            #reproduction costs 300 energy
            if (self.predators[i].energy <= 0):
                self.die(self.predators[i])
                break
            elif (self.predators[i].energy > 1200):
                self.reproduce(self.predators[i])
                
    def updateHerbivores(self):
        for i in range(len(self.herbivores)):
            #move the creatures
            self.herbivores[i].move(self.worldSize)

            #check if any food is close enough to eat, if so eat it
            self.foodList = self.herbivores[i].checkEat(self.foodList)

            #creatures die if they run out of energy and reproduce if they meet a threshold
            #reproduction costs 300 energy
            if (self.herbivores[i].energy <= 0):
                self.die(self.herbivores[i])
                break
            elif (self.herbivores[i].energy > 450):
                self.reproduce(self.herbivores[i])
    
    def die(self, creature):
        creature.getFitness()
        if (creature.speed == 1):
            self.herbivores.remove(creature)
        else:
            self.predators.remove(creature)

    def reproduce(self, creature):
        if (creature.speed == 1):
            image = 'sprites/creature_blue.png'
        else:
            image = 'sprites/creature_red.png'
        
        animat = Creature.Creature(image, \
                                    creature.speed, \
                                    creature.baseEnergy, \
                                    creature.viewDistance, \
                                    creature.movementEfficiency)
        animat.center_x = creature.center_x
        animat.center_y = creature.center_y
        creature.children += 1
        if (creature.speed == 1):
            creature.energy -= 300
            self.herbivores.append(animat)
        else:
            creature.energy -= 600
            self.predators.append(animat)


def main():
    worldSize = 800
    win = myWindow(worldSize, worldSize, 'Test')

    os.remove('dataOutput/HerbivoreStat.txt')
    os.remove('dataOutput/PredatorStat.txt')
    f = open('dataOutput/HerbivoreStat.txt', 'a+')
    f.close()
    f = open('dataOutput/PredatorStat.txt', 'a+')
    f.close()

    arcade.run()

if __name__ == '__main__':
    main()