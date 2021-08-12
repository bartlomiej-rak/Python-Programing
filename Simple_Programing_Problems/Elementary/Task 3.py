"""Modify the previous program such that only the users Alice and Bob are greeted with their names."""

x = input("Please enter your name:")

if x == "Alice" or x == "Bob":
    print("Hello", x)
