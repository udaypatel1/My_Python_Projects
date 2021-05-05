#
# Uday Patel
#
# Project Euler Problem 4
#
# Largest Palindrome Product of two 3-digit integers

palindromes = []

def isPalindrome(n):
    n = str(n)
    if n[::-1] == n:
        return True
    else:
        return False

def largestPalindrome():

    global palindromes
    
    for i in range(100,1000):
        for j in range(100,1000):
            num = i * j
            if isPalindrome(num) == True:
                palindromes.append(num)

    return palindromes                

largestPalindrome()
print("The largest palindrome of the product of two 3-digit integers (995, 583) is " + str(palindromes[-1]))

#
# Algorithmic Complexity (w/ Limited Knowledge)
#
# (n^2) + (n) + (3)
#
# O(n^2)
