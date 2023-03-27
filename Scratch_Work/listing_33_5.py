# This program calculates a factorial
# WITHOUT using recursion
def factorial_nonrecursive(n):
    answer = 1
    for i in range(2, n + 1):
        answer = answer * i
    return answer