class Cat:
    population = 0

    def __init__(self, name):
        self.name = name
        Cat.population += 1

def main():
    cat1 = Cat('Pat')
    cat2 = Cat('Pepper')
    cat3 = Cat('Pouncy')

    print('The cat population is: ', Cat.population) # when using static variables always use the class name
    print('The cat population is: ', cat1.population) # don't use the variable name, creates confusion

main()