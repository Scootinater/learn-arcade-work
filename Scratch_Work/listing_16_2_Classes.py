# defining a class
class Character:
    '''
    This is a class that represents the player character
    '''
    def __init__(self):
        ''' This is a method that sets up the variables in the object. '''
        self.name = ''
        self.outfit = ''
        self.max_hit_points = 0
        self.current_hit_points = 0
        self.armor_amount = 0
        self.max_speed = 0