''' Handling number conversion errors '''
try:
    x = int('fred')
except:
    print('Error converting fred to a number')