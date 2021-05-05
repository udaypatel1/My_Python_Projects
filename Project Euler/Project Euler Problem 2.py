#
# Uday Patel
#
# Project Euler Problem 2
# 
# Sum of Even Fibonacci Numbers Below 4 Million

from math import sqrt

evenFib = []

def fib(n):

    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

def fibSum():

    global evenFib

    for i in range(0,34):
        rem = fib(i) % 2
        if rem == 0:
            evenFib.append(fib(i))

    return evenFib

print(fibSum())
print("The sum of all even fibonacci numbers below 4 million is " + str(sum(evenFib)))

# Algorithmic Complexity (w/ Limited Knowledge)
#
# (n^2) + (2)
#
# O(n^2)
