"""Write three functions that compute the sum of the numbers in a list: using a
 for-loop, a while-loop and recursion. (Subject to availability of these constructs
 in your language of choice.)"""


def sum_using_for_loop(L):
    sum = 0
    for i in L:
        sum += i
    return sum

def sum_using_while_loop(L):
    sum = 0
    idx = 0
    while idx < len(L):
        sum += L[idx]
        idx += 1
    return sum

def sum_using_recursion(L):
    if len(L) == 0: return 0
    else: return L[0] + sum_using_recursion(L[1:])


# Test
test_list = [-5, -10, -15, 1, 10, 11, 14, 2, 4, 7]
y = sum_using_for_loop(test_list)
print(y)

z = sum_using_while_loop(test_list)
print(z)

k = sum_using_recursion(test_list)
print(k)
