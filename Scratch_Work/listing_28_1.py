'''
array backed grid
show how to use a two-dimensional list/array to back the display of a 
grid on-screen
'''
import arcade

# this sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets teh margin between each cell
# and on the edges of the screen.
MARGIN = 5

# set how many rows and columns we will have
ROW_COUNT = 10
COLUMN_COUNT = 10

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    '''
    Main application class
    '''
    def __init__(self, width, height):
        super().__init__(width, height)

        self.grid = []
        for row in range(ROW_COUNT):
            # add an empty array that will hold each cell
            #in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0) # append a cell

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        '''
        Render the screen
        '''
        arcade.start_render()

        # draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE
                
                #do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    
    
    def on_mouse_press(self, x, y, button, key_modifiers):
        '''
        Called when the user presses a button.
        '''
        # Change the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        print(f'Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})')
        
        # make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:
            
            # flip the locatoin bewtween 1 and 0
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0
                

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()