# extending the Window class and making your own child class of arcade.Window

import arcade

class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        # call the parent class's init function
        super().__init__(width, height, title)

        # set the background color
        arcade.set_background_color(arcade.color.ASH_GREY)
    
    def on_draw(self):
        ''' Called whenever we need to draw the window. '''
        arcade.start_render()

        arcade.draw_circle_filled(50, 50, 15, arcade.color.AUBURN)

def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()

main()