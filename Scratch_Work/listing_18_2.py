# open arcade.Window with an object

import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = 'Drawing Example'

def main():
    window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE) #this line makes it an object

    arcade.run()

main()