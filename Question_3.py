'''
Problem 3:-
    Given a list of integers, write a function to find the second largest number without using built-in functions like sorted().
'''

list1 = [2,3,4,5,8,6]
def second_max(list):
    firstmax = max(list1)
    list1.remove(firstmax)
    secondmax = max(list1)
    return secondmax
list = list1
print(second_max(list))