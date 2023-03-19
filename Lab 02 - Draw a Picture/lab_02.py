'''Drawing a Picture

review questions-> my answers
1. module
2. statement
3.period '.'
4. after a comma
5.arcade.open_window()
6. API - application program interface
7. arcade.set_background_color()
8. arcade.start_render()
9. arcade.finish_render()
10. RGB red green blue
11. 0, 0, 0
12. 255, 255, 255
13. 0 and 1
14. 8 bits
15. 256
'''
import arcade

width = 800
height = 600
title = "Drawing Lab 2"


arcade.open_window(width, height, title)

arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

arcade.start_render()

arcade.draw_circle_outline(center_x = 400, center_y = 300, radius = 100,
                            color = arcade.color.ANDROID_GREEN, border_width = 5)

arcade.draw_circle_outline(center_x = 325, center_y = 400, radius = 25,
                            color = arcade.color.ANDROID_GREEN, border_width = 5)

arcade.draw_circle_outline(center_x = 475, center_y = 400, radius = 25,
                            color = arcade.color.ANDROID_GREEN, border_width = 5)
arcade.draw_circle_outline(center_x = 365, center_y = 350, radius = 25,
                            color = arcade.color.ANDROID_GREEN, border_width = 5)
arcade.draw_circle_outline(center_x = 435, center_y = 350, radius = 25,
                            color = arcade.color.ANDROID_GREEN, border_width = 5)

arcade.draw_ellipse_outline(center_x = 400, center_y = 250, width =100, height = 50,
                             color = arcade.color.ANDROID_GREEN, border_width = 5)

arcade.draw_line(start_x = 400, start_y = 200, end_x = 400, end_y = 100, 
                 color = arcade.color.ANDROID_GREEN, line_width = 5)
arcade.draw_line(start_x = 350, start_y = 150, end_x = 450, end_y = 150, 
                 color = arcade.color.ANDROID_GREEN, line_width = 5)

                         



arcade.finish_render()

arcade.run()
