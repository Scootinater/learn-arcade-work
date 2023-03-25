def main():
    ''' read in lines from a file '''

    # open the file for reading, and store a pointer to it in the new
    # variable 'file'

    my_file = open('super_villians.txt')

    # create an empty list to store our names
    name_list = []

    # loop through each linein the file like a list
    for line in my_file:
        # remove anyline feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # add the name to the list
        name_list.append(line)

    my_file.close()

    print('There were', len(name_list), 'names in the file.')

    # --- Linear search
    key = "Morgiana the Shrew"

    # start at the beginning of the list
    current_list_position = 0

    # loop until you reach the end of the list, or the value at the 
    # current position iis equal to the key.
    while current_list_position < len(name_list) and name_list[current_list_position] != key:
        # advance to the next item in the list
        current_list_position += 1
    
    if current_list_position < len(name_list):
        print('The name is at position', current_list_position)
    else:
        print('THe name was not in the list.')

main()