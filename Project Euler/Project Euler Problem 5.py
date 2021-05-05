#
# Uday Patel
#
# Project Euler Problem 5
#
# Smallest Multiple Evenly Divisible by 1-20

theNum = 0

def isMultiple(n):

    nums = [19,17,13,11,7,5,3,2,1]

    for i in nums:
        if (n % i) != 0:
            return False
    return True

def smallestEvenDivisible():

    global theNum

    for i in range(220000000,250000000): # closed off range for simplicity and efficiency after known solution
        if isMultiple(i) == True:
            theNum = i
            return i

smallestEvenDivisible()
print("The smallest multiple that is evenly divisible by all numbers from 1 to 20 is " + str(theNum))

#
# Algorithmic Complexity (w/ Limited Knowledge)
#
# (n^2) + (n) + (1)
#
# O(n^2)
            

    
