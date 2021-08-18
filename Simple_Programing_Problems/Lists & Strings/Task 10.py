"""Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3]."""


def combine_two_lists_alternatingly(L1, L2):
    L = []
    for i, j in zip(L1, L2):
        L.append(i)
        L.append(j)
    return L


a = ['a','b','c']
b = [1,2,3]
print(combine_two_lists_alternatingly(a,b))