"""Write a program that prints a multiplication table for numbers up to 12."""

import numpy as np

x = np.arange(1, 11)

y = np.arange(1, 13)


for i in y:
    print("Multiplication table for ", y[i-1], ":")
    for j in x:
        print(y[i-1], "x", x[j-1], "=", y[i-1]*x[j-1])

