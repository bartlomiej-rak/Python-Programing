"""Write a function that returns the largest element in a list."""


def largest_elem(l):
    elem = l[0]
    for i in l:
        if i > elem:
            elem = i
    return elem


# Test
test_list = [-5, -10, -15, 0, 10, 11, 14, 2, 4, 7]
x = largest_elem(test_list)
print(x)
