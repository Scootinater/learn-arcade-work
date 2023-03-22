import arcade

arcade.open_window(300, 300, 'Sound Demo')
nutz_sound = arcade.load_sound("deez_nutz_dad.wav")
arcade.play_sound(nutz_sound)
arcade.run()