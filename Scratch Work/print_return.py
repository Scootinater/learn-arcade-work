def sum_print(a, b):
    result = a + b
    print(result)

def sum_return(a, b):
    result = a + b
    return result

sum_print(4, 4)

sum_return(4, 4)

x1 = sum_print(4, 4)
print('x1 = ', x1)

x2 = sum_return(4, 4)
print('x2 =', x2)
