''' insertion sort '''
import random

def insertion_sort(my_list):

    # start at the second element (pos 1).
    # use this element to insert into the list.
    for key_pos in range(1, len(my_list)):

        # get the balue of the element to insert
        key_value = my_list[key_pos]

        # scan from the right to the left (start of list)
        scan_pos = key_pos - 1
        
        # loop each element, moving them up until
        # we reach the position the 
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1

        # everything's been move out of the way, insert
        # the keyinto the correct location
        my_list[scan_pos + 1] = key_value

def print_list(my_list):
    for item in my_list:
        print('{:3}'.format(item), end='')
    print()

# create a list of random numbers
my_list = []
for i in range(10):
    my_list.append(random.randrange(100))

# try out the sort
print_list(my_list)
insertion_sort(my_list)
print_list(my_list)