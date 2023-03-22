''' 
Triggering a sound using arcade's builtin sounds support
Triggers with space bar press
'''

import arcade

class MyApplication(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, "Trigger Sound With Key")

        # load the sound when the application starts
        self.laser_sound = arcade.load_sound('laser.wav')
        self.explosion_sound = arcade.load_sound(':resources:sounds/explosion2.wav')
        self.explosion_sound_player = None
        if not self.explosion_sound_player or not self.explosion_sound_player.playing:
            self.explosion_sound_player = arcade.play_sound(self.explosion_sound)

    def on_key_press(self, key, modifiers):

        # if the user hits the space bar, play the sound that we loaded
        if key == arcade.key.SPACE:
            arcade.play_sound(self.laser_sound)

def main():
    window = MyApplication(300, 300)
    arcade.run()

main()