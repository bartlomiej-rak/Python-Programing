"""Write a program that prints the next 20 leap years."""

current_year = int(input("What is the current year? "))


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Year", year, "is a leap year.")
        return True
    else:
        return False


c = 0
while c <= 19:
    year_check = is_leap_year(current_year)
    if year_check:
        c += 1
    current_year += 1

