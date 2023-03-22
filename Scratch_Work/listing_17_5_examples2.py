class Person():
    def __init__(self):
        self.name = ''

    def report(self):
        # basic report
        print('Report for', self.name)

class Employee(Person):
    def __init__(self):
        # call the parent/super class constructor first
        super().__init__()

        # now set up the variables
        self.job_title = ''

    def report(self):
        # here we override report and just do this:
        print('Employee report for', self.name)

class Customer(Person):
    def __init__(self):
        super().__init__()
        self.email = ''
        
    def report(self):
        # run the parent report:
        super().report()
        # now add our own stuff to the end so we do both
        print('Customer e-mail:', self.email)

def main():
    john_smith = Person()
    john_smith.name = 'John Smith'

    jane_employee = Employee()
    jane_employee.name = 'Jane Employee'
    jane_employee.job_title = 'Web Developer'
    
    bob_customer = Customer()
    bob_customer.name = "Bob Customer"
    bob_customer.email = 'send_me@spam.com'

    john_smith.report()
    jane_employee.report()
    bob_customer.report()

main()