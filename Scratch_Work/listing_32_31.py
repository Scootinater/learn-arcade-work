import arcade

def on_draw(self):
    ''' Use this function to draw everything to the screen '''

    # Start the render. This must happen before any drawing
    # commands. We do NOT need a stop render command.
    arcade.start_render()

    # calculate minutes
    minutes = int(self.total_time) // 60

    # calculate seconds by using a mudulus (remainder)
    seconds = int(self.total_time) % 60

    # figure out our output
    output = f"Time: {minutes:02d}:{seconds:02d}"

    # output the time text
    arcade.draw_text(output, 300, 300, arcade.color.BLACK, 30)

def update(self, delta_time):
    ''' all the logic to move and the game logic goes here. '''
    self.total_time += delta_time