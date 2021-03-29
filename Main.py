import arcade
import random
import math

#classes
import Creature
import Food


class myWindow (arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHEAT)

        self.worldSize = width
        
        #number of creatures
        population = 10
        
        #food spawn variables
        self.foodDensity = 15
        foodMultiplier = 16
        
        #how far from the edge of the screen entities must spawn
        self.spawnBorder = 50

        #create creatures
        self.creatures = []
        for i in range(population):
            x = random.randint(self.spawnBorder, (self.worldSize - self.spawnBorder))
            y = random.randint(self.spawnBorder, (self.worldSize - self.spawnBorder))
            animat = Creature.Creature(x,y)
            self.creatures.append(animat)

        #create food
        self.food = []
        for i in range(population * foodMultiplier):
            self.replenishFood()

    #create food clumps
    def replenishFood(self):
        x = random.randint(self.spawnBorder, (self.worldSize - self.spawnBorder))
        y = random.randint(self.spawnBorder, (self.worldSize - self.spawnBorder))
        for j in range(random.randint(2, 7)):
            x = x + random.randint(-self.foodDensity,self.foodDensity)
            y = y + random.randint(-self.foodDensity,self.foodDensity)
            plant = Food.Food(x,y)
            self.food.append(plant)

    def on_draw(self):
        arcade.start_render()
        #render creatures
        for i in range(len(self.creatures)):
            arcade.draw_circle_filled(self.creatures[i].x, self.creatures[i].y, 5, arcade.color.BLUE_GREEN)
        
        #render food
        for i in range(len(self.food)):
            arcade.draw_circle_filled(self.food[i].x, self.food[i].y, 5, arcade.color.GO_GREEN)

    def on_update(self, delta_time):
        #2% chance more food is generated
        if (random.randint(0,100) < 3):
            self.replenishFood()

        for i in range(len(self.creatures)):

            #move the creatures
            self.creatures[i].move(self.worldSize)

            #check if any food is close enough to eat, if so eat it
            self.food = self.creatures[i].checkEat(self.food)

            #creatures die if they run out of energy and reproduce if they meet a threshold
            #reproduction costs 300 energy
            if (self.creatures[i].energy <= 0):
                #print ('dead')
                self.creatures[i].getFitness()
                del self.creatures[i]
                break
            elif (self.creatures[i].energy > 600):
                animat = Creature.Creature(self.creatures[i].x, self.creatures[i].y, self.creatures[i].baseEnergy, self.creatures[i].viewDistance, self.creatures[i].movementEfficiency)
                self.creatures.append(animat)
                self.creatures[i].energy -= 300
                self.creatures[i].children += 1

def main():
    worldSize = 750
    win = myWindow(worldSize, worldSize, 'Test')

    arcade.run()

if __name__ == '__main__':
    main()