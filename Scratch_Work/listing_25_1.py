''' Sprite Sample Program including walls '''

import arcade

# Constants
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    ''' This class represents the main window of the game '''

    def __init__(self):
        ''' Initializer '''
        # call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites With Walls Example")

        # sprite lists
        self.player_list = None
        self.wall_list = None

        # set up the player
        self.player_sprite = None

        # this variable hold our simple physics engine
        self.physics_engine = None

        # create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)



    def setup(self):
        # set up the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # reset the score
        self.score = 0

        # create the player
        self.player_sprite = arcade.Sprite('character.png', SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # manually create and position a box at 300, 200
        wall = arcade.Sprite('boxCrate_double.png',SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        # manually create and position a box at 364, 200
        wall = arcade.Sprite('boxCrate_double.png',SPRITE_SCALING_BOX)
        wall.center_x = 364
        wall.center_y = 200
        self.wall_list.append(wall)

        # place boxes inside a loop
        for x in range(173, 650, 64):
            wall = arcade.Sprite('boxCrate_double.png', SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        # --- place wall with a list
        coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                           [470, 570]]
        
        # loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite('boxCrate_double.png', SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)


    def on_draw(self):
        arcade.start_render()

        # select the scrolled camer for our sprites
        self.camera_for_sprites.use()

        # draw the sprites
        self.wall_list.draw()
        self.player_list.draw()

        # select the (unscolled) camera for our GUI
        self.camera_for_gui.use()
        arcade.draw_text(f'Score: {self.score}', 10, 10, arcade.color.WHITE, 24)

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

        self.physics_engine.update()
        self.player_sprite.update()
        
        ''' need to find out what this does...'''
        # scroll the screen to the player
        #self.scroll_to_player()

        # Scroll the window to the player
        #
        # If CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        # Anything between 0and 1 will have the camera move to the location with a smooth
        # pan.
        CAMERA_SPEED = 1
        lower_left_corner = (self.player_sprite.center_x - self.width / 2,
                             self.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)


def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()