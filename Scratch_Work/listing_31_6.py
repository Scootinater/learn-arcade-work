''' 
Show how to use exceptions to save a high score for a game. 
'''

def get_high_score():
    # default high score
    high_score = 0

    # try to read the high score from a file
    try:
        high_score_file = open('high_score.txt', 'r')
        high_score = int(high_score_file.read())
        high_score_file.close()
        print('The hgigh score is: ', high_score)
    except IOError:
        # error reading file, no high score
        print('There is no high score yet.')

    except ValueError:
        # There's a file there but we dont understand the number
        print("I'm confused. Sarting with no high score.")

    return high_score

def save_high_score(new_high_score):
    try:
        # write the file to disk
        high_score_file = open('high_score.txt', 'w')
        high_score_file.write(str(new_high_score))100
        high_score_file.close()
    except IOError:
        # Hm, can't write it
        print('Unable to save the high score.')

def main():
    ''' Main program is here. '''
    # get the high score
    high_score = get_high_score()

    # get the score form the current game
    current_score = 0 
    try:
        # ask the user for his/her score
        current_score = int(input('What is your score? '))
    except ValueError:
        # error, can't turn what they typed into a number
        print("I don't understand what you typer.")

    # see if we have a new higg score
    if current_score > high_score:
        # we do save to disk
        print('Yea! New high score')
        save_high_score(current_score)
    else:
        print('Better luck next time!')

# call the main function
if __name__ == "__main__":
    main()