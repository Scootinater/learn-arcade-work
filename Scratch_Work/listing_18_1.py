# opening arcade.Window with a function

import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example") # this line calls the function

    arcade.run()

main()