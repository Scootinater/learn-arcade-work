number_entered = False
while not number_entered:
    number_string = input('Enter an integer: ')
    try:
        n = int(number_string)
        number_entered = True
    except:
        print('Error, invalid integer.')