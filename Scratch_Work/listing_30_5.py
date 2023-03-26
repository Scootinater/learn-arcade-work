''' Full Sorting Example '''

import random

def selection_sort(my_list):
    ''' Sort a list using the selection sort '''

    # loop through the entire array
    for cur_pos in range(len(my_list)):
        # find the position that has the smallest number
        # start with the current position
        min_pos = cur_pos

        # scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(my_list)):

            # is the position smallest?
            if my_list[scan_pos] < my_list[min_pos]:
                # it is, mark this position as the smallest
                min_pos = scan_pos
        
        # swap the two values
        temp = my_list
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp

def insertion_sort(my_list):
    ''' Sort a list using insertion sort '''
    # start at the second element (pos 1)
    # use this element to insert in to the list.
    for key_pos in range(1, len(my_list)):

        # get the value of the element to insert
        key_value = my_list[key_pos]

        # scan from right to the left (start of list)
        scan_pos = key_pos - 1

        # loop each element, moving them up until
        # we reach the positon the 
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1
        
        # everything's been moved out of the way, insert
        # the key into the correct location
        my_list[scan_pos + 1 ] = key_value

# This will print out a list
def print_list(my_list):
    for item in my_list:
        print(f"{item:3}", end="")
    print()

def main():
    # create two lists of the same random numbers
    list_for_selection_sort = []
    list_for_insertion_sort = []
    list_size = 10
    for i in range(list_size):
        new_number = random.randrange(100)
        list_for_selection_sort.append(new_number)
        list_for_insertion_sort.append(new_number)

    # print the original list
    print('Original List')
    print_list(list_for_selection_sort)

    # use the selection sort and print the result
    print('Selection Sort')
    selection_sort(list_for_selection_sort)
    print_list(list_for_selection_sort)

    # use the insertion sort and print the result
    print('Insertion Sort')
    insertion_sort(list_for_insertion_sort)
    print_list(list_for_insertion_sort)

main()