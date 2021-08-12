"""Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17"""

x = int(input("Please enter a number:"))

s = 0
for i in range(1, x+1):
    if i % 3 == 0 or i % 5 == 0:
        print(i)  # to check the numbers
        s += i

print("The sum of the numbers from 1 to", x, "is", s)