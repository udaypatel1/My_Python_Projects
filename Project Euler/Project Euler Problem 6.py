#
# Uday Patel
#
# Project Euler Problem 6
#
# Difference Between the sum of the squares of the first hundrend natural numbers and the square of the sum

def sumSquareDifference():

    squares = [x*x for x in range(1,101)]
    sumSquare = sum(squares)

    regInts = [x for x in range(1,101)]
    squareSum = (sum(regInts))**2

    return squareSum - sumSquare

print(sumSquareDifference())

#
# Algorithmic Complexity (w/ Limited Knowledge)
#
# (4n) + (1)
#
# O(n)
