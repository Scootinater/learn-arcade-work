"""This is a sample program.

Multi-line comments are surrounded by three double quotes
"""

# imprt the "arcade library"
import arcade
arcade.open_window(600, 600, "Drawing Example")


# set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# get ready to draw
arcade.start_render()

# draw a rectangle
# left of 0, right of 599
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

# tree trunk
# center of 100, 320
# Width of 20
# height of 60
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

#tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

# another tree, with an ellipse for the top
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

# another tree, with a trunk and arc for the top
# arc is centered at (300, 340) with a width of 60 and height of 100.
#The starting angle is 0, and ending angle is 180.
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(center_x = 300,
                       center_y = 340,
                       width = 60,
                       height = 100,
                       color = arcade.csscolor.DARK_GREEN,
                        start_angle = 0,
                        end_angle = 180)

#another tree, with a trunk and triangle for the top
#triangle is made of these points
#(400, 400), (370, 320) (430, 320)
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

#draw a tree using a polygon with a list of points
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                            arcade.csscolor.DARK_GREEN)
#draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

# rays to the left, right, up and down
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW)

#diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

arcade.draw_text("Arbor Day - Plant a Tree!", 
                 150, 230, 
                 arcade.color.BLACK, 24)
#Finish drawing
arcade.finish_render()

# keep the window open
arcade.run()