"""
Simple animation example shows boucing rectangle

This can also be run from the command line with:
python3 -m arcade.examples.bouncing_rectangle
"""

import arcade

# --- Set up the constants 

# size of the screen

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Bounching Rectangle Example'

# rectangle info
RECT_WIDTH = 50
RECT_HEIGHT = 50
RECT_COLOR = arcade.color.DARK_BROWN

BACKGROUND_COLOR = arcade.color.ALMOND

class Item:
    """ This class represents our triangle"""
    def __init__(self):


        # set up attribute variables. 
    
        # where we are
        self.center_x = 0
        self.center_y = 0

        # where we are going
        self.change_x = 0
        self.change_y = 0

    def update(self):
        # move the rectangle
        self.center_x += self.change_x
        self.center_y += self.change_y
        # check to see if we need to bounce off right edge
        if self.center_x > SCREEN_WIDTH - RECT_WIDTH / 2:
            self.change_x *= -1
        # check to see if we need to bounce off top edge
        if self.center_y > SCREEN_HEIGHT - RECT_HEIGHT / 2:
            self.change_y *= -1
        # check to see if we need to bounce off left edge
        if self.center_x < RECT_WIDTH / 2:
            self.change_x *= -1
        # check to see if we need to bounce off bottom edge
        if self.center_y < RECT_HEIGHT / 2:
            self.change_y *= -1
        
    def draw(self):
        # draw the rectangle
        arcade.draw_rectangle_filled(self.center_x,
                                     self.center_y,
                                     RECT_WIDTH, 
                                     RECT_HEIGHT, 
                                     RECT_COLOR)
        
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # create our rectangle
        self.item = Item()
        self.item.center_x = 200
        self.item.center_y = 300
        self.item.change_x = 2
        self.item.change_y = 3

        # set background color
        self.background_color = BACKGROUND_COLOR

    def on_update(self, delta_time):
        # move the triangle
        self.item.update()

    def on_draw(self):
        # Render the screen

        # clear the screen
        self.clear()
        # draw the rectangle
        self.item.draw()

def main():
    '''Main Function'''
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == '__main__':
    main()