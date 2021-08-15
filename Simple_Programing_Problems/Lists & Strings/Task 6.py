"""Write a function that tests whether a string is a palindrome."""


def is_palindrome(string):
    answer_positive = 'String is a palindrome'
    answer_negative = 'String is not a palindrome'
    # even
    if len(string) % 2 == 0:
        c = len(string) / 2
        idx = 0
        while idx <= c:
            if string[idx] != string[-1-idx]:
                return answer_negative
            idx += 1
        return answer_positive
    else:
        c = len(string) / 2
        idx = 0
        while idx < c:
            if string[idx] != string[-1-idx]:
                return answer_negative
            idx += 1
        return answer_positive


# Test
test_list_string = ['abcdeedcba', 'abcdefedcba', 'abcdefdcba', 'abcdefedcxa']
for i in test_list_string:
    x = is_palindrome(i)
    print(x)
