import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_grass():
    '''draw the ground'''
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

def draw_snow_person(x, y):
    # draw a snow person


    # draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)

def on_draw(delta_time):
    arcade.start_render()
    
    draw_grass()
    draw_snow_person(on_draw.snow_person1_x, 140)
    draw_snow_person(450, 180)

    on_draw.snow_person1_x += 1

on_draw.snow_person1_x = 150

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'Drawing with Functions')
    arcade.set_background_color(arcade.color.DARK_BLUE)
    
    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()