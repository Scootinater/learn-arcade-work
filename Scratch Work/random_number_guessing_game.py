'''
Random number guessing game
'''
import random

def main():
    print("Hi! I'm thinking of a random number between 1 and 100.")

    # NEW CONCEPT
    # Create a secret number
    secret_number = random.randrange(1, 101)

    # initialize our attempt count, we start with attemp 1.
    user_attempt_number = 1

    # set user guess to something secret number can't be, so we can
    # get our 'while' loop started.
    user_guess = 0

    # NEW CONCEPT
    # Loop until user_guess our secret number, or we run out of attempts. 
    while user_guess != secret_number and user_attempt_number < 8:
        
        # tell the user what attempt we are on, and get their guess:
        print("--- Attempt", user_attempt_number)
        user_input_text = input("Guess what number I am thinking of: ")
        user_guess = int(user_input_text)

        # print if we are too high or low, or we got it.
        if user_guess > secret_number:
            print('Too high.')
        elif user_guess < secret_number:
            print('Too low.')
        else:
            print('You got it!')
        
        # add to the attempt count
        user_attempt_number += 1
    
    # here, check to see if the user didn't guess the answer, and ran out of tries.
    # let her know what the number was, so she doesn't spend the rest of her life wondering.
    if user_guess != secret_number:
        print('Aw, you ran our of tries. The secret number was ' + str(secret_number) + '.')

# call the main function
main()