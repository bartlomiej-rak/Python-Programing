"""Write a program that computes the sum of an alternating series where each element of the series
is an expression of the form ((−1)k+1)/(2*k−1)((-1)^{k+1})/(2 * k-1) for each value of kk from 1 to
a million, multiplied by 4. Or, in more mathematical notation"""

s = 0
for k in range(1, 1000001):
    single_expression = ((-1) ** (k + 1)) / (2 * k - 1)
    s += single_expression

s = 4 * s
print(s)
