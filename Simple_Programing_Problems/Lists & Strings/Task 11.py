"""Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6].
You can do this quicker than concatenating them followed by a sort."""


def merge_list(L1, L2):
    L = L1 + L2
    L.sort()
    return L


a = [1,4,6]
b = [2,3,5]
print(merge_list(a,b))