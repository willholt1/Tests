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
        
        population = 10
        
        #how far from the edge of the screen entities must spawn
        spawnBorder = 15

        #create creatures
        self.creatures = []
        for i in range(population):
            x = random.randint(spawnBorder, (self.worldSize - spawnBorder))
            y = random.randint(spawnBorder, (self.worldSize - spawnBorder))
            animat = Creature.Creature(x,y)
            self.creatures.append(animat)

        #create food
        self.food = []
        for i in range(population * 20):
            x = random.randint(spawnBorder, (self.worldSize - spawnBorder))
            y = random.randint(spawnBorder, (self.worldSize - spawnBorder))
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
        for i in range(len(self.creatures)):
            #move the creatures in a random direction
            ranNum = random.randint(1,4)
            if ranNum == 1:
                direction = 'U'
            elif ranNum == 2:
                direction = 'D'
            elif ranNum == 3:
                direction = 'L'
            elif ranNum == 4:
                direction = 'R'

            self.creatures[i].move(self.worldSize, direction)

            #check if can eat any food
            for j in range (len(self.food)):
                distance = math.sqrt( (self.food[j].x - self.creatures[i].x)**2 + (self.food[j].y - self.creatures[i].y)**2 )
                if distance <= 10:
                    print('Chomp')
                    self.creatures[i].eat(self.food[j])
                    del self.food[j]
                    break

def main():
    worldSize = 500
    win = myWindow(worldSize, worldSize, 'Test')

    arcade.run()

if __name__ == '__main__':
    main()