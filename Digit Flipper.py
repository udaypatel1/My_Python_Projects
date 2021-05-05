

def rev(phrase):

    phraseList = list(phrase) # breaks up all values in a list form
    # print(phraseList)

    indexList = []

    indexes = []
    
    for i in range(len(phraseList)):

        # print(phraseList[i])

        lastOne = False

        try:
            
            if phraseList[i + 1] not in "1234567890":
                lastOne = True

        except:

            lastOne = True   

        if phraseList[i] in "1234567890":

            indexes.append(i)

            # print(indexes)
            
            if lastOne == False:

                continue

            else:


                indexList.append(indexes)

                indexes = []

                
    print(indexList)

    # print(indexList[0][::-1])

    reverseIndexList = []

    for group in indexList:

        reverseIndexList.append(group[::-1])

    print(reverseIndexList)

    refPhraseList = list(phrase)

    for i in range(len(indexList)):

        for j in range(len(indexList[i])):

            phraseList[indexList[i][j]] = refPhraseList[reverseIndexList[i][j]]

    # print(phraseList)
                                                                                                
    return "".join(phraseList)

#print(rev("a123bb456bbsdfjhskdjh987sss1928"))

if __name__ == "__main__":

    print("Welcome to Digit Flipper!")
    x = input("Enter some text: ")
    print("Reversed Text: ")
    print(rev(x))



     
