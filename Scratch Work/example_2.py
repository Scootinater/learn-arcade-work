def a():
    print('A start')
    b()
    print('A end')

def b():
    print('B start')
    c()
    print('B end')

def c():
    print('C start and end')

a()