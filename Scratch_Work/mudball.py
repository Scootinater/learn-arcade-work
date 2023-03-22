"""
MUDBALL text only game
"""

import math
import random

def print_instructions():
    '''this function prints the instructions'''

    print("""
Welcome to Mudball! The idea is to hit the other player with a mudball.
Enter your angle (in degrees) and the amount of PSI to charge your gun
with.
    """)

def calculate_distance(psi, angle_in_degrees):
    ''' Caluculate the distance the mudball flies. '''
    angle_in_radians = math.radians(angle_in_degrees)
    distance = .5 * psi ** 2 * math.sin(angle_in_radians) * math.cos(angle_in_radians)
    return distance

def get_user_input(name):
    ''' Get the user input for psi and angle. Return as a list of two numbers '''
    psi = float(input(name + ' charge the gun with how many psi? '))
    angle = float(input(name + ' move the gun at what angle? '))
    return psi, angle

def get_player_names():
    ''' Get a list of names from the players. '''
    print('Enter player names. Enter as many players as you like.')
    done = False
    players = []
    while not done:
        player = input('Enter player (hit enter to quit): ')
        if len(player) > 0:
            players.append(player)
        else:
            done = True

    print()
    return players

def process_player_turn(player_name, distance_apart):
    ''' The code runs the turn for each player. 
    If it returns False, keep going with the game.
    If it returns True, someone has won, so stop. '''
    psi, angle = get_user_input(player_name)

    distance_mudball = calculate_distance(psi, angle)
    difference = distance_mudball - distance_apart

    if difference > 1:
        print('You went', difference, 'yards too far!')
    elif difference < -1:
        print('You were', difference * -1, 'yards too short!')
    else:
        print('Hit!', player_name, 'wins!')
        return True
    
    print()
    return False

def main():
    '''Main Program.'''

    # get the game started
    print_instructions()
    player_names = get_player_names()
    distance_apart = random.randrange(50, 150)

    # keep looking until someone wins
    done = False
    while not done:
        # loop for each player
        for player_name in player_names:
            # process their turn
            done = process_player_turn(player_name, distance_apart)
            # if someone won, 'break' out of this loop and end the game.
            if done:
                break

if __name__ == '__main__':
    main()