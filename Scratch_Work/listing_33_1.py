def f():
    g()
    print('f')

def g():
    print('g')

f()
g()