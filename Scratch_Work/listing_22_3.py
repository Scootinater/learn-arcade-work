''' Sprites moving in circles '''

import random
import arcade
import math

SPRITE_SCALING = 0.5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



class Coin(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        ''' Constructor. '''
        # call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # current angle in radians
        self.circle_angle = 0

        # how far away from the center to orbit, in pixels
        self.circle_radius = 0

        # how fast to orbit, in radian per frame
        self.circle_speed = 0.008

        # set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):
        ''' update the ball's position '''
        # calculate a new x,y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) + self.circle_center_y

        # increase the angle in prep for the next round
        self.circle_angle += self.circle_speed

        self.angle += 1
        if self.angle > 359:
            self.angle -= 360

class MyGame(arcade.Window):
    ''' Main application class '''
    def __init__(self, width, height):
        super().__init__(width, height)

        # sprite lists
        self.player_list = None
        self.coin_list = None

        # set up the player
        self.score = 0
        self.player_sprite = None
        

    def start_new_game(self):
        ''' Set up the game and initialize the variables '''
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # set up the player
        self.score = 0

        # character image from kenney.nl
        self.player_sprite = arcade.Sprite('character.png', 0.10)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70   
        self.player_list.append(self.player_sprite)
        # self.player_sprite.angle = 180 # flips the character 180

        for i in range(50):
            # create the coin instance
            # coin image from kenney.nl
            coin = Coin('coin_01.png', SPRITE_SCALING / 3)

            # position the center of the circle the coin will orbit
            coin.circle_center_x = random.randrange(SCREEN_WIDTH)
            coin.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # random radius from 10 to 200
            coin.circle_radius = random.randrange(10, 200)

            #random start angle from 0 to 2pi
            coin.circle_angle = random.random() * 2 * math.pi

            # add the coin to the lists
            self.coin_list.append(coin)

        # don't show the mouse cursor
        self.set_mouse_visible(False)

        # set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        # this command has to happen before we start drawing
        arcade.start_render()

        # draw all the sprites
        self.coin_list.draw()
        self.player_list.draw()

        # put the text on the screen.
        output = 'Score: ' + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        ''' Movement and game logic '''
        
        # call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()

        # generate a list of all sprites that colided with the player
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # loop through eac colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            self.score += 1
            coin.remove_from_sprite_lists()

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.start_new_game()
    arcade.run()

if __name__ == '__main__':
    main()