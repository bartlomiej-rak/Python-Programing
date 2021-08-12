"""Write a program that asks the user for a number n and prints the sum of the numbers 1 to n"""

x = int(input("Please enter a number:"))

s = 0
for i in range(1, x+1):
    s += i

print("The sum of the numbers from 1 to", x, "is", s)
