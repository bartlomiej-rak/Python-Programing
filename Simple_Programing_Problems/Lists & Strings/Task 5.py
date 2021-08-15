"""Write a function that computes the running total of a list."""


def total_of_list(L):
    total = 0
    for i in L:
        total += i
    return total


# Test
test_list = [-5, -10, -15, 1, 10, 11, 14, 2, 4, 7]
x = total_of_list(test_list)
print(x)
