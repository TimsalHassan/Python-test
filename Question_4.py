'''
Problem 4:- 
    Write a Python function that removes all duplicate elements from a list while maintaining the order of elements.
'''

list1 = [4,4,4,1,1,1,2,2,3,3,3,5,6]
def rem_duplicate(list):
    list2 = set(list)
    l1 = []
    for i in list2:
        l1.append(i)
    return l1
list = list1
print(rem_duplicate(list))