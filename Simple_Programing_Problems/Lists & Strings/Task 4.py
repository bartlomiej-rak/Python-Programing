"""Write a function that returns the elements on odd positions in a list."""


def odd_positions(L):
    L_odd = []
    for i in range(len(L)):
        if i % 2 == 1:
            L_odd.append(L[i])
    return L_odd


# Test
test_list = [-5, -10, -15, 0, 10, 11, 14, 2, 4, 7]
x = odd_positions(test_list)
print(x)
