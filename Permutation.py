
def perm(itemsList):

    if len(itemsList) == 1:
        return itemsList

    elif len(itemsList) == 0:
        return None

    resultList = []

    for i in range(len(itemsList)):

        restList = itemsList[:i] + itemsList[i+1:]

        for j in perm(restList):

            
            resultList.append(itemsList[i] + ',' + j)

    return resultList

final = []

for i in perm(['lebron','kobe','giannis']):
    
    final.append(i.split(','))

print(final)
    
    


