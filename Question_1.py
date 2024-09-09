'''
Problem 1:-
    Write a function to generate the Fibonacci sequence up to n terms using a loop.
'''

def fibonacci(n):
    l1 = [0,1]
    while (len(l1)<n):
        l1.append(l1[-1]+l1[-2])
    return l1

n = int(input("Enter the number: "))
print(fibonacci(n))