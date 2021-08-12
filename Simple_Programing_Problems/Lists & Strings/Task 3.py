"""Write a function that checks whether an element occurs in a list."""


def check_if_occurs(l, elem):
    for i in l:
        if elem == l[i]:
            return True
        else:
            return False


# Test
test_list = [-5, -10, -15, 0, 10, 11, 14, 2, 4, 7]
element = 17
x = check_if_occurs(test_list, element)
if x:
    print("The element", element, "occurs in the list")
else:
    print("The element", element, "does not occur in the list")
