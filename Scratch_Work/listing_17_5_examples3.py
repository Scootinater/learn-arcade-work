# static vs instanced variables

# example of an instanced variable
class ClassA():
    def __init__(self):
        self.y = 3
    
# example of a static variable
class ClassB():
    x = 7

def main():
    # create class instance
    a = ClassA()
    b = ClassB()

    # two ways to print the static variable
    # the second way is the proper way to do it. 
    print(b.x)
    print(ClassB.x)

    # one way to print an instance variable. 
    # The second generates an error, because we don't know what instance
    # to reference.
    print(a.y)
    #print(ClassA.y)

main()