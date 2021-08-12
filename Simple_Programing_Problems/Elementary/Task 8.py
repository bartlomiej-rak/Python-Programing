"""Write a program that prints all prime numbers. (Note: if your programming language
 does not support arbitrary size numbers, printing all primes up to the largest number
 you can easily represent is fine too.)"""

lower_bound = int(input("Please enter a lower bound:"))
upper_bound = int(input("Please enter an upper bound:"))

print("All prime numbers between",lower_bound,"and",upper_bound,"are: ")

for num in range(lower_bound, upper_bound + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)