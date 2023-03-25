def main():
    object_list = []
    object_list.append(AdventureObject('Key', 5))
    object_list.append(AdventureObject('Bear', 5))
    object_list.append(AdventureObject('Food', 8))
    object_list.append(AdventureObject('Sword', 2))
    object_list.append(AdeventureObject('Wand', 10))

    result = check_if_one_item_has_property_v1(object_list, 5)
    print('Result of test check_if_one_item_has_property_v1:', result)

    result = check_if_one_item_has_property_v2(object_list, 5)
    print('Result of test check_if_one_item_has_property_v2:', result)

    result= check_if_all_items_have_property(object_list, 5)
    print('Result of test check_if_all_items_have_property:', result)

    result = get_matching_items(object_list, 5)
    print('Number of items returned from test get_matching_items:', result)

main()