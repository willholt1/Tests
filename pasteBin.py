
def main():
    worldSize = 500
    world = np.zeros(shape = (worldSize, worldSize), dtype = 'int')

    #can be U, D, L, R  (up, down, left, right)
    direction = "R"

    x = 5
    y = 5
        
    animat = Creature.Creature(x,y)
    animat.getPosition()
    animat.move(worldSize, direction)

if __name__ == "__main__":
    main()


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

        if ((self.x - 5 < food.x < self.x + 5) and (food.y < self.y + self.viewDistance)):
            self.direction = 'D'
            self.forage = True
            print("found Down")
        elif ((self.x - 5 < food.x < self.x + 5) and (food.y > self.y - self.viewDistance)):
            self.direction = 'U'
            self.forage = True
            print("found Up")
        elif ((self.y - 5 < food.y < self.y + 5) and (food.x > self.x - self.viewDistance)):
            self.direction = 'L'
            self.forage = True
            print("found Left")
        elif ((self.y - 5 < food.x < self.y + 5) and (food.x < self.x + self.viewDistance)):
            self.direction = 'R'
            self.forage = True
            print("found Right")
        else:
            print("Looking")