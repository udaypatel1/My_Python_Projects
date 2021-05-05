


def binarySum(x,y):

    if len(x) != len(y):
        return "Cannot Add!"
    
    carryOverList = [i-i for i in range(len(x))]

    print(carryOverList)

    xList = [int(i) for i in x]
    yList = [int(i) for i in y]

    resultList = []
    
    print(xList)
    print(yList)
    print("-----")

    for i in range(len(x)-1,-1,-1):


        print("carryOver[",i,"] =",carryOverList[i])
        print("xList[",i,"]=",xList[i])
        print("yList[",i,"]=",yList[i])
        print("Equation: ",carryOverList[i]," + ",xList[i]," + ",yList[i])
        
        ans = 0

        if carryOverList[i] == 0 and xList[i] == 0 and yList[i] == 0:
            ans = 0
            resultList.append(ans)
        elif carryOverList[i] == 0 and xList[i] == 0 and yList[i] == 1:
            ans = 1
            resultList.append(ans)
        elif carryOverList[i] == 0 and xList[i] == 1 and yList[i] == 0:
            ans = 1
            resultList.append(ans)
        elif carryOverList[i] == 1 and xList[i] == 0 and yList[i] == 0:
            ans = 1
            resultList.append(ans)

            
        elif carryOverList[i] == 0 and xList[i] == 1 and yList[i] == 1:
            print("value of i-1 is: ", i-1)
            if (i-1) < 0:
                ans = 10
                resultList.append(ans)
                break
            else:
                carryOverList[i-1] = 1
                ans = 0
                resultList.append(ans)
        elif carryOverList[i] == 1 and xList[i] == 1 and yList[i] == 0:
            if (i-1) < 0:
                ans = 10
                resultList.append(ans)
                break
            else:
                carryOverList[i-1] = 1
                ans = 0
                resultList.append(ans)
        elif carryOverList[i] == 1 and xList[i] == 0 and yList[i] == 1:
            if (i-1) < 0:
                ans = 10
                resultList.append(ans)
                break
            else:
                carryOverList[i-1] = 1
                ans = 0
                resultList.append(ans)
        elif carryOverList[i] == 1 and xList[i] == 1 and yList[i] == 1:
            if (i-1) < 0:
                ans = 11
                resultList.append(ans)
                break
            else:
                carryOverList[i-1] = 1
                ans = 1
                resultList.append(ans)

    revResultList = resultList[::-1]
    
    print(carryOverList)
    print(xList)
    print(yList)
    print(revResultList)

    if len(str(revResultList[0])) == 2:
        temp = str(revResultList[0])
        temp = list(temp)
        print(temp)
        replace = temp[1]
        revResultList[0] = int(replace)
        print(revResultList)
    
    
    return "".join([str(i) for i in revResultList])

if __name__ == "__main__":

    print("Welcome to Binary Addition!")
    print("Enter two binary digits or enter exit to quit")

    x = 0

    while(x != 'exit'):

        x = input("Enter a binary digit: ")
        if x == 'exit':
            exit()
        y = input("Enter a binary digit: ")
        if y == 'exit':
            exit()

        print(binarySum(x,y))
    

# print(binarySum('0010011010010001','0000010010110001'))
