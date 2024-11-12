import arcade
import random
class Comp151Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.score = 0
        self.player = None
        self.target = None
        self.dX = 0
        self.dY = 0

    def setup(self):
        arcade.set_background_color(arcade.color.LIGHT_GRAY)
        self.player = arcade.Sprite("grim.png")
        self.target = arcade.SpriteList()
        self.player.center_x = 1000
        self.player.center_y = 1000
        self.setupGoblins()

    def setupGoblins(self):
        for i in range(10):
            newX = random.randint(60, 1940)
            newY = random.randint(60, 1940)
            newGoblin = arcade.Sprite("goblin.png")
            newGoblin.center_x = newX
            newGoblin.center_y = newY
            self.target.append(newGoblin)


    def on_update(self, time_since_update):
        self.player.center_y += self.dY
        self.player.center_x += self.dX
        if self.player.center_x > 1940:
            self.player.center_x = 1940
        elif self.player.center_y > 1940:
            self.player.center_y = 1940
        elif self.player.center_y < 60:
            self.player.center_y = 61
        elif self.player.center_x < 60:
            self.player.center_x = 61

    def on_draw(self):
        arcade.start_render()

        self.player.draw()
        self.target.draw()
        arcade.finish_render()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.dY= 5
        elif key == arcade.key.DOWN:
            self.dY= -5
        elif key == arcade.key.LEFT:
            self.dX= -5
        elif key == arcade.key.RIGHT:
            self.dX= 5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.dY= 0
        elif key == arcade.key.DOWN:
            self.dY = 0
        elif key == arcade.key.LEFT:
            self.dX = 0
        elif key == arcade.key.RIGHT:
            self.dX = 0