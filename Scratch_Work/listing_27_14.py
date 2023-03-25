class AdventureObject:
    ''' Class that defines an object in a tet adventure game '''

    def __init__(self, description, room):
        ''' Constructor. '''

        # Description of the object
        self.description = description

        # The number of the room that the object is in
        self.room = room

def check_if_one_item_is_in_room_v1(my_list, room):
    '''
    Return true if at least one item has a property.
    '''
    i = 0
    while i < len(my_list) and my_list[i].room != room:
        i += 1

    if i < len(my_list):
        # found an item with the property
        return True
    
    else:
        # There is no item with the property
        return False
    
def check_if_one_item_is_in_room_v2(my_list, room):
    '''
    Return true if at least one item has a
    property. Works the same as v1, but less code.
    '''
    for item in my_list:
        if item.room == room:
            return True
    return False

def check_if_all_items_are_in_room(my_list, room):
    '''
    Return true if ALL items have a property.
    '''
    for item in my_list:
        if item.room != room:
            return False
    return True

def get_items_in_room(my_list, room):
    '''
    Build a brand new list that holds all teh items 
    that match our property.
    '''
    matching_list = []
    for item in my_list:
        if item.room == room:
            matching_list.append(item)
    return matching_list

