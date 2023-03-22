class Address:
    ''' Hold all the fields for a mailing address '''
    def __init__(self):
        ''' Set up the address fields '''
        self.name = ''
        self.line1 = ''
        self.line2 = ''
        self.city = ''
        self.state = ''
        self.zip = ''

def main():
    # create an address
    home_address = Address()

    # set the fields in the address
    home_address.name = 'Scott Denny'
    home_address.line1 = '7350 Walnut Cove Rd'
    home_address.line2 = ''
    home_address.city = 'Walkertown'
    home_address.state = 'NC'
    home_address.zip = '27051'

    vacation_home_address = Address()
    vacation_home_address.name = 'Scott'
    vacation_home_address.line1 = '123 Main St'
    vacation_home_address.line2 = ''
    vacation_home_address.city = 'Destin'
    vacation_home_address.state = 'Florida'
    vacation_home_address.zip = '12345'

    print('My main home is in ' + home_address.city)
    print('My vacation home is in ' + vacation_home_address.city)
main()