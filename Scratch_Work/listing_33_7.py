# This program calculates a factorial 
# WITHOUT using recursion

def factorial_nonrecursive(n):
    answer = 1
    for i in range(2, n +1):
        print(i, '*', answer, '=', i * answer)
        answer = answer * i
    return answer
print('I can caluclate a Factorial!')
user_input = input("Enter a number: ")
n = int(user_input)
answer = factorial_nonrecursive(n)
print(answer)

# This prgram calculates a factorial
# WITH recursion

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        x = factorial_recursive(n-1)
        print(n, '*', x, '=', n * x)
        return n * x
print('I can calculate a factorial!')
user_input = input('Enter a number: ')
n = int(user_input)
answer = factorial_recursive(n)
print(answer)