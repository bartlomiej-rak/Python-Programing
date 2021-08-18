"""Write a function that rotates a list by k elements. For example [1,2,3,4,5,6] rotated by two becomes
[3,4,5,6,1,2]. Try solving this without creating a copy of the list. How many swap or move operations do you need?"""


def rotate_list(L, k):
    if k == 0: return L
    x = L[0]
    L = L[1:]
    L.append(x)
    return rotate_list(L, k-1)


a = [1,2,3,4,5,6]
print(rotate_list(a,6))