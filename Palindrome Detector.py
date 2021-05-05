
# palindrome detector

def palindromeDetector():
    
    word = input("Choose a word? ")

    word = list(word) # one of my favorite python ways to split string lists to individual characters (so useful)
    rev = (word[::-1]) # important python syntax of list manipulation
 
    print(word)
    print(rev)

    if rev == word:
        print("The word is the same forward and backward")
        print("The word is a palindrome")
    else:
        print("The word is not the same forward and backward")
        print("The word is not a palindrome")

palindromeDetector()
    
    
    


    



