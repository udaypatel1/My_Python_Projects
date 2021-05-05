
script = "A vacation is when you take a trip to some [adjective] place with your [adjective] family. Usually you go to some place that is near a/an [noun] or up on a/an [noun]. A good vacation place is one where you can ride [plural-noun] or play [game] or go hunting for [plural-noun]. I like to spend my time [verb-ending-in-ing] or [verb-ending-in-ing]. When parent go on a vacation, they spend their time eating three [plural-noun] a day, and fathers play golf, and mothers sit around [verb-ending-in-ing]. Last summer, my little brother fell in a/an [noun] and got poison [plant] all over his [part-of-the-body]. My family is going to go to (the) [place], and I will practice [verb-ending-in-ing]. Parents need vacations more than kids because parents are always very [adjective] and because they have to work [number] hours every day all year making enough [plural-noun] to pay for the vacation."

def madLibs(textFile):

    finalScript = []

##    rawText = open(textFile,'r')
##    rawText = rawText.read()
##    data = rawText.split()

    data = textFile.split(' ') # <--- DELETE THIS
    #print(data)
    for i in data:
        #print(i)
        if '[' not in i:
            finalScript.append(i)
        else:
            gui = ''

            suffix = False
            suffixValue = None
            endBracket = False
            
            for j in range(len(i)):
                
                if i[j] == ']':
                    endBracket = True
                    try:
                        if i[j+1] != None:
                            suffix = True
                            suffixValue = i[j+1]
                            break
                            
                        else:
                            break
                    except:
                        break
                            
                if i[j] == '[':
                    continue
                else:
                    if endBracket == True:
                        continue
                    gui = gui + i[j]

            article = ''
            if gui[0] in 'aeiou':
                article = 'an'
            else:
                article = 'a'

            gui = gui.replace('-',' ')
            print(gui)
    
            ans = input("Please give " + article + " " + gui)

            if suffix == True:
                #print(suffix)
                ans = ans + suffixValue
            
            finalScript.append(ans)

    #print(finalScript)
    print("Here is your story:")
    print("--------------------")
    return " ".join(finalScript)

#madLibs(script)
print(madLibs(script))


if __name__ == "__main__":

    try:
        print('Welcome to a fun word replacement game.')
        textFile = input("Enter the name of the file to use:\n")
        print(madLibs(textFile))
        
    except:
        print("Error Bad File Name")
        return



    
