"""Write a program that asks the user for a number n and gives them the possibility to choose between computing the
sum and computing the product of 1,…,n."""

x = int(input("Please enter a number:"))

y = int(input("To compute the sum of 1,...,n type 1:\nTo compute the product of 1,...,n type 2:"))

while y != 1 or 2:
    if y == 1:
        s = 0
        for i in range(1, x + 1):
            s += i
        print("Sum of 1,...,n equals", s)
        break
    elif y == 2:
        p = 1
        for i in range(1, x + 1):
            p = p * i
        print("Product of 1,...,n equals", p)
        break
    else:
        print("You have to choose between 1 and 2")
        y = int(input("To compute the sum of 1,...,n type 1:\nTo compute the product of 1,...,n type 2:"))
