# ball class example- I improved upon the randomness of where the balls start :)

import arcade
import random

random_x = random.randint(0, 640)
random_y = random.randint(0, 480)

random_x_2 = random.randint(0, 640)
random_y_2 = random.randint(0, 480)

random_x_3 = random.randint(0, 640)
random_y_3 = random.randint(0, 480)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ball:
    ''' This class manages a ball bouncing on the screen. '''

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        ''' Constructor. '''

        # take the parameters of the init function above, and create instance variables out of them. 
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        ''' Draw the balls with the instance variables we have. '''
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        ''' Code to control the ball's movement. '''
        
        # move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # see if the balls hit the screen, if so, change direction.
        if self.position_x < self.radius:
            self.change_x *= -1
        
        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1
        
        if self.position_y < self.radius:
            self.change_y *= -1
        
        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1

class MyGame(arcade.Window):
    ''' My window class '''
    def __init__(self, width, height, title):
        ''' Constructor. '''

        # call the parent class's init function
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

        # create a list for the balls
        self.ball_list = []

        # add three balls to the list
        ball = Ball(random_x, random_y, 3, 3, 15, arcade.color.AUBURN)
        self.ball_list.append(ball)

        ball = Ball(random_x_2, random_y_2, 2, 3, 15, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
        self.ball_list.append(ball)

        ball = Ball(random_x_3, random_y_3, -3, -3, 15, arcade.color.FOREST_GREEN)
        self.ball_list.append(ball)

    def on_draw(self):
        ''' Called whenever we need to draw the window. '''
        arcade.start_render()
        
        # Use a "for" loop to pull each ball from the list, then call the draw
        # method on that ball. 
        for ball in self.ball_list:
            ball.draw()
            
    def update(self, delta_time):
        ''' Called to update our objects. Happens at approx 60 times per second. '''
        
        # Use a "for" loop to pull each ball from the list, then call the update
        # method on that ball.
        for ball in self.ball_list:
            ball.update()

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    arcade.run()

main()