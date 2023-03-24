''''
Scroll around a large screen.

Artwork from kenney.nl

'''

import random
import arcade

SPRITE_SCALING = 0.5


DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 6000
SCREEN_TITLE = 'Sprite Move with Scrolling Screen Example'

# how many pixels to keep as a minimum margin between the character
# and the edge of the screen. 
VIEWPORT_MARGIN = 200

# How fast the camera pans to the player. 1.0 is instant
CAMERA_SPEED = 0.1

# How fast the character moves
MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    ''' Main application class. '''

    def __init__(self, width, height, title):
        '''
        Initializer
        '''
        super().__init__(width, height, title, resizable=True)

        # sprite lists
        self.player_list = None
        self.wall_list = None

        # set up the player
        self.player_sprite = None

        self.physics_engine = None

        # used in scrolling
        self.view_bottom = 0
        self.view_left = 0

        # track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        ''' set up the game and initialize the variables '''

        # sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # set up the player
        self.player_sprite = arcade.Sprite("female_idle.png", scale = 0.4)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # set up severl columns of walls
        for x in range(200, 1650, 210):
            for y in range(0, 1600, 64):
                # randomly skip a box so the player can find a way through
                if random.randrange(5) > 0:
                    wall = arcade.Sprite('grassCenter.png', SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)
        
        #  set the physics engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # set the viewport boundaries
        # these numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        '''
        Render the screen
        '''
        # this command has to happen before we start drawing
        self.clear()
        arcade.start_render()
        # select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()

        # select the (unscrolled) camera for our GUI.
        self.camera_gui.use()

        # draw the GUI
        arcade.draw_rectangle_filled(self.width // 2, 20, self.width, 40, arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, {self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

        # Draw the box that we work to make sure the user stays inside of.
        # This is just for illustration purposes. You'd want to remove this 
        # in your game.
        left_boundary = VIEWPORT_MARGIN
        right_boundary = self.width - VIEWPORT_MARGIN
        top_boundary = self.height - VIEWPORT_MARGIN
        bottom_boundary = VIEWPORT_MARGIN
        arcade.draw_lrtb_rectangle_outline(left_boundary, right_boundary, top_boundary, bottom_boundary, 
                                           arcade.color.RED, 2)
    def on_key_press(self, key, modifiers):
        ''' called whenever a key is pressed '''

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
    
    
    def on_key_release(self, key, modifiers):
     
        ''' called when the user release a key '''

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        ''' Movement and game logic '''

        # call update on all sprites(the sprites don't do much in this example though)
        self.physics_engine.update()

        # scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        '''
        Scroll the window to the player.
        This method will attempt to keep the player at lease VIEWPOINT_MARGIN
        pixels away form the edge. 

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a 
        smooth pan.
        '''

        # --Manage Scrolling--
        
        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
        
        # Scroll right
        right_boundary = self.view_left + self.width - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary

        # Scroll up
        top_boundary = self.view_bottom + self.height - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
        
        # Scroll to the proper location
        position = self.view_left, self.view_bottom
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        '''
        Resize window
        Handle the user grabbing the edge and resizing the window. 
        '''
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))

def main():
    ''' main function '''
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()