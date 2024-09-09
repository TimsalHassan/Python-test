'''
Problem 6:-
    Explain and demonstrate the use of Python decorators, including a custom decorator that measures the execution time of a function.
'''

import time

def time_calculator(func):
    def included(*args, **kwargs):
        time1 = time.time()
        result = func(*args, **kwargs)
        time2 = time.time()
        execution = time2 - time1
        print("Execution time ", execution)
        return result
    return included

@time_calculator
def second_max(list):
    list1 = [2,3,4,5,8,6]
    firstmax = max(list1)
    list1.remove(firstmax)
    secondmax = max(list1)
    return secondmax
print(second_max(list))

