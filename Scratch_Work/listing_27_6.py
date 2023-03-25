# --- Linear search
key = 'Morgiana the Shrew'

# start at the beginning of the list
current_list_position = 0
# loop until you reach the end of the list, or the value at the
# current positon is equal to the key
while current_list_position < len(name_list) and name_list[current_list_position]:

    # advance to the next item in the list
    current_list_position += 1
 
if current_list_position < len(name_list):
    print("The name is at position", current_list_position)
else:
    print('The name was not in the list.')