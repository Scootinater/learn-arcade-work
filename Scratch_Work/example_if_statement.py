# variables used in the example 'if' statements

a = 1
b = 5 
c = 7

# basic comparisons
if a < b:
    print('a is less than b')

if a > b:
    print('a is greater than b')

if a == b:
    print('a and b are equal')

print('Done')

if a <= b:
    print('a is less than or equal to b')

if a >= b:
    print('a is greater than or equal to b')

if a != b:
    print('a and b are not equal')

if a == 1:
    print('If a is one, this will print.')
    print('so will this')
    print('and this')

print('This will always print because it is not indented.')

if a < b and a < c:
    print('a is less than b and c')

if a < b or a < c:
    print('a is less than either b or c (or both)')

a = False
if a:
    print('a is true')

if not a:
    print('a is false')

a = True
b = False

if a and b:
    print('a and b are both true')