''' sprite sample program '''

import random
import arcade

# --- constants ---
SPRITE_SCALING_PLAYER = 0.10
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Coin(arcade.Sprite):
    '''
    This class represents the coins on our screen. It is a child class of
    the arcade library's 'Sprite' class.
    '''

    def reset_pos(self):

        # reset the coin to a random spot above the screen 
        
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)
    
    def update(self):
        
        # move the coin
        self.center_y -= 1

        # see if the coin has fallen off the bottome of the screen.
        # if so, reset it. 
        if self.top < 0:
            self.reset_pos()

       

class MyGame(arcade.Window):
    ''' Our Custom Window Class '''

    def __init__(self):
        # call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # variables that will hold sprite lists.
        self.player_list = None
        self.coin_list = None
        
        # set up the player info
        self.player_sprite = None
        self.score = 0

        # don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        ''' set up the game and initialize the variables '''

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # set up the player
        # character image from kenney.nl
        self.player_sprite = arcade.Sprite('character.png', SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # create the coins
        for i in range(COIN_COUNT):

            # create the coin instance
            coin = Coin('coin_01.png', SPRITE_SCALING_COIN)

            # position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # add the coins to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()

        ''' 
        Draw the sprite lists here. Typically sprites are divided into
        different groups. Other game engines might call these 'sprite layers'
        or 'sprite groups'. Sprites that don't move should be drawn in their 
        own group for the best performance, as Arcade can tell the graphics
        card to just redraw them at the same spot.
        Try to avoid drawing sprites on their own, use a SpriteList
        because there are many performance improvements in that code.
        '''
        self.coin_list.draw()
        self.player_list.draw()

        # put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        ''' Handle Mouse Motion '''

        # move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_timer):
        ''' Movement and game logic '''
        
        # call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()

        # generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, 
                                                              self.coin_list)
        
        # loop through each colliding sprite, remove it, an dadd to the score. 
        for coin in hit_list:
            coin.reset_pos()
            self.score += 1


def main():
    ''' Main Method '''
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()