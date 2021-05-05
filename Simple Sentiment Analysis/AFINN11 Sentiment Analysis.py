

def open_and_parse_file(fileName):

    f = open(fileName,'r')
    fd = f.read()
    fd = fd.split()

    finalList = []
    newList = []
    c = 0
    
    for i in fd:
        if c == 2:
            c = 0
            finalList.append(newList)
            newList = []
        newList.append(i)
        c+=1

    return finalList

data = open_and_parse_file('AFINN11.txt')

def sentimentAnalysis(sampleText, sentimentBank):

    textList = sampleText.split(" ")

    runningScore = 0

    for i in textList:

        for j in sentimentBank:

            if i == j[0]:
                try:
                    runningScore += int(j[1])
                except:
                    continue

    comparativeScore = runningScore / len(textList)

    return runningScore, comparativeScore

runScore, compScore = sentimentAnalysis("On a sunny spring day, there were beautiful flowers growing in the field. The chirping birds sat on the tall trees while the sun was just beginning to rise. It had just freshly rained and the dew was still on the grass as the ice cream truck drove into town. All the children ran out of their houses in smiles as they apprached the ice cream truck. All the kids were ecstatic because they were all getting the ice cream that they wanted. Everyone was happy and went home to enjoy their ice cream with their families. Every family had a smile on their face on the first day of spring.", data)

print(runScore)
 
