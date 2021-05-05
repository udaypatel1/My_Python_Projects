#problem 211

# compiling / efficiency issue for this problem
# this problem can and should be done in a more efficient manner so that one can see all the perfect squares in below 64 million along with their sum

import math as m

num = []
number = int(input('Choose a number: '))
for i in range(0,number):  # dictates numbers that are affected by problem
    num.append(i)

totals = []
    
def divisor():  # does the computing until the sum of one number's divisors
    
    for n in num: # for loop so it does it for each number listed above
    
        divisors = [] # empty list of one number's divisors
        for i in range(1,n+1):
            if n%i == 0:
                divisors.append(i)
        sqdivi = []                 # empty list of one number's squared divisors
        for i in range(0,len(divisors)):
            sq = (m.pow(divisors[i],2))
            sqdivi.append(sq)
        totals.append((sum(sqdivi))) # puts each finished value in list named totals
    print(totals)  # prints the entire list with sums of squared divisors of each number given in range
    
divisor() # calling the function

perfs = [] # empty list with perfect squares that appear in list named totals

for h in range(0,len(totals)):
    if ((totals[h])**0.5 == int((totals[h])**0.5)):  # checks if a number is a perfect square (if a number's square root to the 2nd power is equal to original number)
        perfs.append(totals[h]) # add them in list named perfs
print(perfs) # print the list of perfect squares (for gui)
print(sum(perfs)) # print the sum of the list directly above



    



        
    


        


