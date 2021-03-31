import arcade
import random
import math

#classes
import Creature
from Food import Food

class myWindow (arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHEAT)

        self.worldSize = width
        
        #number of creatures
        population = 10
        
        #food spawn variables
        self.foodDensity = 20
        foodMultiplier = 1
        
        #how far from the edge of the screen entities must spawn
        self.spawnBorder = 50

        #create creatures
        self.creatures = arcade.SpriteList()
        for i in range(population):
            animat = Creature.Creature("sprites/creature_blue.png")
            animat.center_x = random.randint(self.spawnBorder, (self.worldSize - self.spawnBorder))
            animat.center_y = random.randint(self.spawnBorder, (self.worldSize - self.spawnBorder))
            
            self.creatures.append(animat)

        #create food
        self.foodList = arcade.SpriteList()
        for i in range(population * foodMultiplier):
            self.replenishFood()

    #create food clumps
    def replenishFood(self):
        x = random.randint(self.spawnBorder, (self.worldSize - self.spawnBorder))
        y = random.randint(self.spawnBorder, (self.worldSize - self.spawnBorder))
        for j in range(random.randint(1, 6)):
            foodSprite = Food("sprites/plant.png")
            foodSprite.center_x = x + random.randint(-self.foodDensity,self.foodDensity)
            foodSprite.center_y = y + random.randint(-self.foodDensity,self.foodDensity)
            self.foodList.append(foodSprite)

    def on_draw(self):
        arcade.start_render()
        #render creatures
        self.creatures.draw()
        #render food
        self.foodList.draw()
        

    def on_update(self, delta_time):
        #2% chance more food is generated
        if (random.randint(0,100) < 2):
            self.replenishFood()

        for i in range(len(self.creatures)):

            #move the creatures
            self.creatures[i].move(self.worldSize)

            #check if any food is close enough to eat, if so eat it
            self.foodList = self.creatures[i].checkEat(self.foodList)

            #creatures die if they run out of energy and reproduce if they meet a threshold
            #reproduction costs 300 energy
            if (self.creatures[i].energy <= 0):
                #print ('dead')
                self.creatures[i].getFitness()
                self.creatures.remove(self.creatures[i])
                break
            elif (self.creatures[i].energy > 600):
                animat = Creature.Creature("sprites/creature_blue.png", self.creatures[i].baseEnergy, self.creatures[i].viewDistance, self.creatures[i].movementEfficiency, self.creatures[i].speed)
                animat.center_x = self.creatures[i].center_x
                animat.center_y = self.creatures[i].center_y
                self.creatures.append(animat)
                self.creatures[i].energy -= 300
                self.creatures[i].children += 1

def main():
    worldSize = 750
    win = myWindow(worldSize, worldSize, 'Test')

    arcade.run()

if __name__ == '__main__':
    main()