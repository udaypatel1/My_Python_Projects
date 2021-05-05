#
# Uday Patel
#
# Project Euler Problem 3
#
# Largest Prime Factor of 600851475143

from math import sqrt

primes = []
primeFactors = []

def primeListCompilation(n):
    global primes
    
    for i in range(0,n):
        if isPrime(i) == True:
            primes.append(i)

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def largestPrime(n):

    global primeFactors

    for i in primes:
        if i == 0:
            continue
        rem = int(n % i)
        if rem == 0:
            primeFactors.append(i)

    return primeFactors
    
primeListCompilation(8000)
print(largestPrime(600851475143))
print("The largest prime factor of 600851475143 is " + str(primeFactors[-1]))

#
# Algorithmic Complexity (w/ Limited Knowledge)
#
# (n^2) + (n) + (4)
#
# O(n^2)




    
