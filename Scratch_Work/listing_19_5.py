''' 
Starting template for having user input control the things in arcade
'''

import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3

class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        # take the parameters of the init function above, 
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        '''' Draw teh balls with the instance variables we have. '''
        arcade.draw_circle_filled(self.position_x,
                                   self.position_y,
                                   self.radius,
                                   self.color)
        
    def update(self):
        # move the ball
        self.position_x += self.change_x
        self.position_y += self.change_y

        # see if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius
        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
        if self.position_y < self.radius:
            self.position_y = self.radius
        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
        
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        
        # call the parent class's init function
        super().__init__(width, height, title)

        # make the mouse disappear when it is over the window.
        # so we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # set the backgound color
        arcade.set_background_color(arcade.color.ASH_GREY)

        # create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

        # check for joysticks attached to computer, if attached, 
        # grab it and make an instance variable out of it. 
        joysticks = arcade.get_joysticks()
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print('There are no joysticks.')
            self.joystick = None

    def on_draw(self):
        ''' called whenever we need to draw the window. '''
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_timer):
        self.ball.update()

        # update the position according to the game controller
        if self.joystick:
            print(self.joystick.x, self.joystick.y)

            self.ball.change_x = self.joystick.x * 5 # multiply by no. to speed up ball movement
            self.ball.change_y = -self.joystick.y * 5 # can also set constant variable at top of program and use instead

    def on_key_press(self, key, modifiers):
        ''' called whenever the user presses a key. '''
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        ''' called whenever a user release a key. '''
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        ''' called to update our objects.
        happens approx 60 times per second'''
        self.ball.position_x = x
        self.ball.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        ''' called when the user presses a mouse button '''

        if button == arcade.MOUSE_BUTTON_LEFT:
            print('Left mouse button pressed at', x, y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print('Right mouse button pressed at', x, y)
    
    

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Drawing Example')
    arcade.run()

main()