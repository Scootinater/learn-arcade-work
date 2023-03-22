class Address:
    def __init__(self, line1, line2, city, state, zip, country):
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country

def main():
    # this creates the address
    my_address = Address('7350 Walnut Cove Rd', None, 'Walkertown', 'NC', '27051', 'USA')

    

main()