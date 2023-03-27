def f(level):
    # Print the level we are at
    print('Recursion call, level', level)
    # If we havent' reached level ten...
    if level < 10:
        # call this function again
        # and add one to the level
        f(level +1)

# start the recursive calls at level 1
f(1)