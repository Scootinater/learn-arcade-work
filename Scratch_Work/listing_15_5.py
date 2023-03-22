# copy of the array to modify
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# loop from 0 up to the number of elements
# in the array
for index in range(len(my_list)):
    # modify the element by doubling it 
    my_list[index] = my_list[index] * 2

# print the result
print(my_list)