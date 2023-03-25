def main():
    ''' read in lines from a file '''
    name_list = []
    # open file, and automatically close when we exit this block.

    with open('super_villians.txt') as my_file:
        # loop through each line in thee file like a list
        for line in my_file:
        # remove any line feed, carriage reurns or spaces at teh end of the line
            line = line.strip()
        
        # add the nameto the list
            name_list.append(line)
    
    print("There were", len(name_list), "names in the file.")
    for name in name_list:
        print(name)

main()