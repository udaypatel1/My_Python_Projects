# Euler Problem 42

# delete the unnecessary print(' ') if need be. This is done for
# code appearance in compiler and commpand prompt.

import string as s

trinum = []
for n in range(0,100):   #trinum is creating list with first 100 triangle numbers
    tn = ((.5*n)*(n+1))
    trinum.append(tn)
#print(trinum)

letters = []
asci = s.ascii_lowercase  #create a lowercase alphabet list for identifying input word value
letters.extend(asci)    #put alphabet list in list named letters
letters.insert(0,'0')     #insert a zero in letters list to allign proper indexes (could even add 1 to final index instead of inputting a 0)
#print(letters)

print("A triangle number is the output of the function (n/2)(n+1). In this problem, an input word will be entered and given an aggregated value by the individual letters in the input word (a = 1, b =2, c = 3 and so on). This program will check if the input word is indeed a triangle word (Please make sure the input word is in lowercase)")
print(' ')
print('Example of triangle numbers: 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55')
print(' ')

triword = input('Input word: ')
print(' ')
triword = list(triword)    #asking for input word and splitting it into individual characters within the list
print(triword)
print(' ')

total = 0 #initialization of running total

for i in range(0,len(triword)): #for loop to the extent of the word length
    
    if triword[i] in letters: #of course a letter in word will be alphabetical
        
        #(letters.index(triword[i]))
        ans = letters.index(triword[i]) #assign the index value of the input word from letters list into ans
        total = total + ans #running counter of input word sum

print('Numerical value of the word: ',total)

if total in trinum:
    print('The word is a triangle number')
else:
    print('The word is not a triangle number')
        

        

