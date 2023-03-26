'''
Scroll around a large screen

Artwork from https://kenney.nl
'''

import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 0.75
TILE_SCALING = 0.75
GRAVITY = 0.5


DEFAULT_SCREEN_WIDTH = 1024
DEFAULT_SCREEN_HEIGHT = 768
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# how many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant. 
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 10
JUMP_SPEED = 10

class MyGame(arcade.Window):
    ''' Main application class. '''

    def __init__(self, width, height, title):
        '''
        Initializer
        '''
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None

        # set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Create the cameras. One for the GUI, one for the sprites. 
        # We scroll the 'sprite world but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        ''' set up the game and initialize the variables '''

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite('female_idle.png', scale = 0.75)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        # set up the walls/objects
        map_name = 'level1.json'

        # read in the tiled map
        self.tile_map = arcade.load_tilemap(map_name, scaling=TILE_SCALING)

        # set wall SpriteList and any others that you have.
        self.wall_list = self.tile_map.sprite_lists['Walls']
        #self.coin_list = self.tile_map.sprite_lists['Coins']

        # set the background color to what is specified in the map
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list,
                                                             gravity_constant=GRAVITY)

        # set up the background color... do i need this for a platformer tile?
        # arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        ''' Render the screen '''

        # this command has to happen before we start drawing
        self.clear()
        arcade.start_render()

        # select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()

        # select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # draw the GUI
        arcade.draw_rectangle_filled(self.width // 2, 
                                     20,
                                     self.width, 
                                     40, 
                                     arcade.color.ALMOND)
        text = f'Scroll value: ({self.camera_sprites.position[0]:5.1f}, ' \
                f'{self.camera_sprites.position[1]:5.1f})'
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):
        ''' Called whenever a key is pressed. '''
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
    
    def on_key_release(self, key, modifiers):
        ''' Called when the user release a key. '''

        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        ''' Movement and game logic '''

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        # self.player_sprite.change_y = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # call update on all sprites 
        self.physics_engine.update()

        # scroll the screen to the player
        self.scroll_to_player()
    def scroll_to_player(self):
        ''' 
        Scroll the window to the player.
        If CAMERA_SPEED is 1, the camera will immediately move to the desired position. 
        Anything between 0 and 1 will have the camera move to teh location with a smoother
        pan.
        '''

        position = Vec2(self.player_sprite.center_x - self.width / 2,
                        self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        '''
        Resize window
        Handle the user grabbing the edge and resizing the window.
        '''
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))

def main():
    ''' Main Function '''
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_WIDTH, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()