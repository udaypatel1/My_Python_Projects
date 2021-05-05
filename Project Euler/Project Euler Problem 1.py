#
# Uday Patel
# Problem 1
# Sum of Multiples of 3 or 5 below 1000
#

def mySum(n):

    mult = []

    for i in range(0,n):
        threeRem = i % 3
        fiveRem = i % 5

        if threeRem == 0:
            mult.append(i)
        elif fiveRem == 0:
            if threeRem == 0:
                pass
            else:
                mult.append(i)
    return mult

print(mySum(1000))
print("The sum of multiples of 3 and 5 below 1000 is " + str(sum(mySum(1000))))

# Algorithmic Complexity (w/ Limited Knowledge)
#
# (n) + (3)
#
# O(n)
