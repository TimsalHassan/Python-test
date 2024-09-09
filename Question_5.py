'''
Problem 5:- 
    Explain the concept of recursion and write a recursive function to calculate the factorial of a number.
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))