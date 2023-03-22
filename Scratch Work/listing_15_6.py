# copy of the array to modify
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# loop throught each element in myArray
for item in my_list:
    # this doubles item, but does not change the array
    # because item is a copy of a single element.
    item = item * 2

# print the result
print(my_list)