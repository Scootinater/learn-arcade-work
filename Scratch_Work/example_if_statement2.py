# example program that runs through all code talked about earlier

# variables used in example if statements
a = 4
b = 5
c = 6

# basic comparisons
if a < b:
    print('a is less than b')

if a > b:
    print('a is greater than b')

if a <= b:
    print('a is less than or equal to b')

if a >= b:
    print('a is greater than or equal to b')

# NOTE! it is very easy to mix up when to use == and =.
# use == if you are asking if they are equal, use =
# if you are assigning a value.

if a == b:
    print('a is equal to b')

# not equal
if a != b:
    print('a is not equal to b')

# and
if a < b and a < c:
    print('a is less than b and c')

# non-exclusive or
if a < b or a < c:
    print('a is less than either b or c (or both)')

# boolean data type. This is legal!
a = True
if a:
    print('a is true')

if not a:
    print('a is false')

a = True
b = False

if a and b:
    print('a and b are both true')

a = 3
b = 3
c = a == b
print(c)

# these are also legal and will trigger as being true because
# the values are not zero
if 1:
    print('1')
if 'A':
    print('A')

# this will not trigger as true because it is zero.
if 0:
    print('Zero')

# comparing variables to multiple values.
# the first if statement appears to work, but it will always 
# trigger as true even if the variable a is not equal to b
# this is because 'b' by itself is considered true
a = 'c'
if a == 'B' or 'b':
    print('a is equal to b. Maybe.')

# proper way to do the if statement.
if a == 'B' or a == 'b':
    print('a is equal to b.')

# example 1 if statement
temperature = int(input('What is the temperature in Farenheit? '))
if temperature > 90:
    print('It is hot outside!')
print('Done')

# example 2 if statement
temperature = int(input('What is the temperature in Farenheit? '))
if temperature > 90:
    print('It is hot outside!')
else:
    print('It is not hot outside.')
print('Done')

# example 3 else if statement
temperature = int(input('What is the temperature in Farenheit? '))
if temperature > 90:
    print('It is hot outside!')
elif temperature > 100:
    print('Oh man! You could fry eggs on the pavement!')
elif temperature < 30:
    print('It is cold outside.')
else:
    print('It is ok outside.')
print('Done.')

# comparisons using string/text
# the input statement will ask the user for input and put it in user_name
user_name = input('What is your name? ')
if user_name == "Paul":
    print('You have a nice name.')
else:
    print('Your name is ok.')
