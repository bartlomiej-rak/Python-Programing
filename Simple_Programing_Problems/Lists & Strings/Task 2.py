"""Write function that reverses a list, preferably in place."""
#can be done using built-in function list.reverse()


def reverse_list(l):
    l_rev = []
    for i in range(len(l)):
        l_rev.append(l[len(l)-i-1])
    return l_rev


# Test
test_list = [-5, -10, -15, 0, 10, 11, 14, 2, 4, 7]
x = reverse_list(test_list)
print(x)
