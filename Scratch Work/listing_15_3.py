# copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# initial sum should be zero
list_total = 0

# loop from 0 up to the number of elements in the array:
for index in range(len(my_list)):
    # add element 0, next 1, then 2, etc.
    list_total += my_list[index]

# print the result
print(list_total)