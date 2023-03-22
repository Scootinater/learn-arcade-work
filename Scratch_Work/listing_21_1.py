''' sprite sample program '''

import random
import arcade

# --- constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    ''' Our Custom Window Class '''

    def __init__(self):
        # call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

    def on_draw(self):
        arcade.start_render()

def main():
    ''' Main Method '''
    window = MyGame()
    arcade.run()