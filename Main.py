import numpy as np
import enum
import Creature

def main():
    worldSize = 15
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