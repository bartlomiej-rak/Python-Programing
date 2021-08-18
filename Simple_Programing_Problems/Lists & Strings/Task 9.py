"""Write a function that concatenates two lists. [a,b,c], [1,2,3] → [a,b,c,1,2,3]"""


def conc(L1, L2):
    L = L1 + L2
    return L


a = ['a','b','c']
b = [1,2,3]
print(conc(a,b))