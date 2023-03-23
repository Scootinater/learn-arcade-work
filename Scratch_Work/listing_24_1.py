''' Starting program for shooting sprites '''

import arcade
import random

SPRITE_SCALING_PLAYER = 0.10
SPRITE_SCALING_COIN = 0.2
SPRITE_LASER_SCALING = 0.8
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED = 5

class MyGame(arcade.Window):
    ''' main application '''

    def __init__(self):
        ''' Initializer '''
        # call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'Sprites and Bullets Demo')

        # variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None

        # set up the player info
        self.player_sprite = None
        self.score = 0

        # don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        ''' set up the game and initialize the variables '''

        # sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # set up the player
        self.score = 0

        # image from ...
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # create the coins
        for i in range(COIN_COUNT):

            # create the coin instance
            # coin image from kenney.nl
            coin = arcade.Sprite('coin_01.png', SPRITE_SCALING_COIN)

            # position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(150, SCREEN_HEIGHT)

            # add the coins to the list
            self.coin_list.append(coin)

            arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        ''' Render the screen '''

        # this command has to happen before we start drawing
        arcade.start_render()

        # draw all the sprites
        self.coin_list.draw()
        self.player_list.draw()
        self.bullet_list.draw()
    

        # render the text
        arcade.draw_text(f'Score: {self.score}', 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        ''' Called whenever the mouse moves. '''
        self.player_sprite.center_x = x
        # self.player_sprite.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        ''' called whenever the mouse button is clicked '''
        bullet = arcade.Sprite('laserBlue01.png', SPRITE_LASER_SCALING)

        bullet.center_x = self.player_sprite.center_x
        bullet.center_y = self.player_sprite.center_y + 30
        bullet.change_y = BULLET_SPEED
        bullet.angle = 90


        # add the bullet to the appropriate list
        self.bullet_list.append(bullet)


    def update(self, delta_time):
        ''' movement and game logic '''

        # call update on all sprites
        self.coin_list.update()
        self.bullet_list.update()

        # loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)

            # if it did get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
            
            # for every coin we hit, add to teh score and remove the coin
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1

            # if the bullet flies off the scree, remove it. 
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ =="__main__":
    main()
    