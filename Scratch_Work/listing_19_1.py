''' 
Starting template for having user input control the things in arcade
'''

import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ball:
    def __init__(self, position_x, position_y, radius, color):
        # take the parameters of the init function above, 
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        '''' Draw teh balls with the instance variables we have. '''
        arcade.draw_circle_filled(self.position_x,
                                   self.position_y,
                                   self.radius,
                                   self.color)
        
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        
        # call the parent class's init function
        super().__init__(width, height, title)

        # set the backgound color
        arcade.set_background_color(arcade.color.ASH_GREY)

        # create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)

    def on_draw(self):
        ''' called whenever we need to draw the window. '''
        arcade.start_render()
        self.ball.draw()

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Drawing Example')
    arcade.run()

main()