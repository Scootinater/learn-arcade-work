class Dog():
    def __init__(self, new_name):
        ''' Constructor '''
        self.name = new_name
        print('A new dog is born!')

def main():
    # This creates the dog
    my_dog = Dog('Fluffy')
    print(f'The dog\'s name is: {my_dog.name}')
main()