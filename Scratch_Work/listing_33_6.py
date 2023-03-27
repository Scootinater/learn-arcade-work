# This program calculates a factorial
# WITH recursion
def factorial_recursive(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * factorial_recursive(n - 1)