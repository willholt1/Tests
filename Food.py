import arcade

class Food(arcade.Sprite):
    def __init__(self, image):
        
        super().__init__(image, 0.5)

        self.energy = 50

    def getPosition(self):
       print('x = {} & y = {}'.format(self.center_x, self.center_y))