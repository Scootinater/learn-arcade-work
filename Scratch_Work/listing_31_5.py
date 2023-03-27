# Multiple Errors
try:
    # open the file
    filename = 'myfile.txt'
    my_file = open(filename)

    # read from the file and strip any trainling line feeds
    my_line = my_file.readline()
    my_line = my_line.strip()

    # convert to a number
    my_int = int(my_line)
    
    # do a calculaton
    my_calculated_value = 101 / my_int

except FileNotFoundError:
    print(f"Count not find the file '{filename}'.")
except IOError:
    print(f"Input/Output error when accessing the file '{filename}'.")
except ValueError:
    print('Could not convert data to an integer.')
except ZeroDivisionError:
    print('Division by zero error.')
except:
    print('Unexpected error.')