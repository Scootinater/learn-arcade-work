''' selection sort'''

import random

def selection_sort(my_list):
    ''' Sort a list using the selection sort'''

    # loop through the entire array
    for cur_pos in range(len(my_list)):
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos

        # scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(my_list)):
            # is this position smallest?
            if my_list[scan_pos] < my_list[min_pos]:
                # it is, mark this position as the smallest
                min_pos = scan_pos

        # swap the two valuse
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp

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
selection_sort(my_list)
print_list(my_list)