''' array backed grid '''
import arcade

WIDTH = 20
HEIGHT = 20
MARGIN = 5
ROW_COUNT = 10
COLUMN_COUNT = 10

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    '''
    Main application class
    '''
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        '''
        Render the screen
        '''

        arcade.start_render()
    
    def on_mouse_press(self, x, y, button, key_modifiers):
        '''
        Called when the user presses a button.
        '''
        pass

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()