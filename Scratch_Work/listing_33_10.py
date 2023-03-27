'''
Recursive H's
'''
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

RECURSION_DEPTH = 5

def draw_h(x, y, width, height, count):
    ''' Recursively draw a H, each one half as big '''

    # draw the H
    # draw the cross-bar
    arcade.draw_line(x + width * .25, height /2 + y,
                     x + width * .75, height / 2 + y, arcade.color.BLACK)
    
    # draw left side
    arcade.draw_line(x + width * .25, height * .5 /2 +y,
                     x + width * .25, height * 1.5 /2 + y, arcade.color.BLACK)
    
    # draw right side
    arcade.draw_line(x + width * .75, height * .5 / 2 + y, 
                     x + width * .75, height * 1.5 /2 +y, arcade.color.BLACK)
    
    # as long as we have a width bigger than 1, recursively call this function with a smaller H
    if count > 0:
        count -= 1
        # draw the line 90% of our current size
        # draw the lower left
        draw_h(x, y, width / 2, height /2, count)
        # draw the lower right
        draw_h(x + width /2, y, width /2, height /2, count)
        # draw upper left
        draw_h(x, y + height /2, width /2, height /2, count)
        # draw upper right
        draw_h(x + width /2, y + height /2, width /2, height /2, count)

class MyWindow(arcade.Window):
    ''' main app class. '''
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        ''' render the screen '''
        arcade.start_render()

        # start our recursive calls
        draw_h(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, RECURSION_DEPTH)

def main():
    MyWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()

if __name__ == '__main__':
    main()