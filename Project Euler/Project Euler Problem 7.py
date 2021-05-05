#
# Uday Patel
#
# Project Euler Problem 7
#
# 10001st Prime Number

def isPrime(x):  

    if x < 2:  
        return False
    
    for n in range(2, (x) - 1):  
        if x % n == 0:  
            return False  

    return True

def nthPrime(n):
    prime = 2
    count = 1
    iter = 3
    while count < n:
        if isPrime(iter):
            prime = iter
            count += 1
        iter += 2
    return prime

print('The 10001st prime number is ' + str(nthPrime(10001)))

#
# Algorithmic Complexity (w/ Limited Knowledge)
#
# no idea, took the nth prime code from stackoverflow
#
    
