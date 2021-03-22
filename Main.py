import arcade
import Creature

class myWindow (arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400,200)
        arcade.set_background_color(arcade.color.WHEAT)

        self.x = 100
        self.y = 100

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.x, self.y, 5, arcade.color.BLUE_GREEN)

    def on_update(self, delta_time):
        self.x += 1
        self.y += 1

worldSize = 500
myWindow(worldSize, worldSize, "Test")

arcade.run()