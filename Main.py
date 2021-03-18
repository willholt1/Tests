import numpy as np
import enum

def main():
    worldSize = 15
    world = np.zeros(shape = (worldSize, worldSize), dtype = 'int')

    #can be U, D, L, R  (up, down, left, right)
    direction = "R"

    x = 2
    y = 2

    world[y][x] = 1

    render(world)
    while True:
        direction = input("direction: ")
        world, x, y = move(world, worldSize, x, y, direction.upper())
        

def render(world):
    for row in world:
        print(*row)
    print("-------------------------------")

def move(world, worldSize, x, y, direction):
    world[y][x] = 0

    if (direction == "U" and y > 0):
        y -= 1
    elif (direction == "D" and y < (worldSize-1)):
        y += 1
    elif (direction == "L" and x > 0):
        x -= 1
    elif (direction == "R" and x < (worldSize-1)):
        x += 1
    else:
        print("invalid direction")

    world[y][x] = 1
    render(world)
    return world, x, y

if __name__ == "__main__":
    main()