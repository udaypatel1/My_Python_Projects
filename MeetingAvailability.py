import math as m

pOneSchedule = [
                ["09:00", "10:30"],["12:00", "13:00"],["16:00", "18:00"],
                ]

pOneBounds = ["09:00", "20:00"]

####################################

pTwoSchedule = [
                ["10:00", "11:30"],["12:30", "14:30"],["14:30", "15:00"],["16:00", "17:00"]
                ]

pTwoBounds = ["10:00", "18:30"]

####################################

meetingDuration = 30

####################################

'''
dataset 2
'''

p1 = [
        ["07:35", "11:22"],["12:00", "13:10"],["14:00", "16:48"]
        ]

p1Bound = ["6:55", "18:00"]

p2 = [
        ["10:00", "10:45"],["12:00", "13:30"],["17:45", "20:00"],["20:30", "21:30"]
        ]

p2Bound = ["8:30", "21:30"]

meetTime = 15
        

def addTimes(time1, time2):

    totalMin1 = toMinutes(time1)
    totalMin2 = toMinutes(time2)

    bothTotal = totalMin1 + totalMin2

    finalTime = toTimeFormat(bothTotal)

    return finalTime

def toTimeFormat(minutes):

    hour = minutes // 60
    minute = minutes % 60
    
    strMinute = ""
    strHour = ""

    if minute == 0:

        strMinute = "00"

    else:

        if len(str(minute)) == 1:

            strMinute = "0" + str(minute)

        else:

            strMinute = str(minute)
        
    if hour == 0:

        strHour = "00"

    else:

        if len(str(hour)) == 1:

            strHour = "0" + str(hour)
        else:

            strHour = str(hour)

    final = strHour + ":" + strMinute

    return final

def toMinutes(time):

    intHour1 = int(time.split(':')[0])
    totalMin1 = (intHour1 * 60) + int(time.split(':')[1])
    #print(time.split(':')[1])
    return totalMin1

def compareTimes(time1, time2):

    totalMin1 = toMinutes(time1)
    totalMin2 = toMinutes(time2)

    if totalMin1 < totalMin2:

        return -1

    elif totalMin1 > totalMin2:

        return 1

    else:

        return 0

def differenceBetween(time1,time2):

    # returns difference between two times in minutes

    totalMin1 = toMinutes(time1)
    totalMin2 = toMinutes(time2)

    return totalMin1 - totalMin2


def meetingAvailability(pOneSchedule, pOneBounds, pTwoSchedule, pTwoBounds, meetingDuration):
    
    mergedSchedules = []

    ptr1 = 0
    ptr2 = 0

    ptr1Status = True
    ptr2Status = True
    
    while ptr1 != len(pOneSchedule) or ptr2 != len(pTwoSchedule):

        if ptr1 == len(pOneSchedule):
            
            mergedSchedules.append(pTwoSchedule[ptr2])
            ptr2 += 1
            ptr1Status = False
            continue

        elif ptr2 == len(pTwoSchedule):
        
            mergedSchedules.append(pOneSchedule[ptr1])
            ptr1 += 1
            ptr2Status = False
            continue
            
        if ptr1Status == True and ptr2Status == True:
            
            endCross = pOneSchedule[ptr1][1]
            startCross = pTwoSchedule[ptr2][0]

        if compareTimes(endCross, startCross) == -1 or compareTimes(endCross, startCross) == 0 and (ptr1Status == True and ptr2Status == True): #endCross is less than startCross OR endCross is equal to startCross

            # append them to merged schedule in order
    
            mergedSchedules.append(pOneSchedule[ptr1])
            mergedSchedules.append(pTwoSchedule[ptr2])

        elif compareTimes(endCross, startCross) == 1 and (ptr1Status == True and ptr2Status == True): #endCross is greater than startCross

            # take start of endCross block and end of startCross block and append the pair

            tempList = []
            
            startOfEndCross = pOneSchedule[ptr1][0]
            endOfStartCross = pTwoSchedule[ptr2][1]

            exception = False
            
            if toMinutes(endCross) >= toMinutes(endOfStartCross):

                tempList.append(startOfEndCross)
                tempList.append(endCross)
                exception = True
                

            if compareTimes(startOfEndCross, endOfStartCross) == 1 and (exception == False): # reorder in appending

                tempList.append(endOfStartCross)
                tempList.append(startOfEndCross)

            else:

                if(exception == False):

                    tempList.append(startOfEndCross)
                    tempList.append(endOfStartCross)

            mergedSchedules.append(tempList)

        if ptr1Status == True and ptr2Status == True:

            ptr1+=1
            ptr2+=1

    # mergedSchedules should be populated after this while loop
    # parse the bounds and add them to the mergedSchedules

    beginBound = []
    endBound = []

    if compareTimes(pOneBounds[0],pTwoBounds[0]) == -1 or compareTimes(pOneBounds[0], pTwoBounds[0]) == 0: # if start time of pOneBound is less than or equal to start time of pTwoBound

        beginBound = ["0:00", pOneBounds[0]]

    else:

        beginBound = ["0:00", pTwoBounds[0]]

    if compareTimes(pOneBounds[1], pTwoBounds[1]) == 1 or compareTimes(pOneBounds[1], pTwoBounds[1]) == 0:

        endBound = [pOneBounds[1], "24:00"]

    else:

        endBound = [pTwoBounds[1], "24:00"]

    mergedSchedules.insert(0,beginBound)
    mergedSchedules.append(endBound)

    # mergedSchedule is a complete with bounds

    # print(mergedSchedules)

    freeSlots = []

    for elem in range(len(mergedSchedules)):

        tempList = []
        
        start = mergedSchedules[elem][1]
        
        try:
            end = mergedSchedules[elem + 1][0]
        except:
            break

        tempList.append(start)
        tempList.append(end)

        freeSlots.append(tempList)
        
    #print("Merged: ", mergedSchedules)
    #print('Unparsed Free Slots', freeSlots)
        
    # parse through freeSlots and find ones that are of meetingDuration

    validMeetingSlots = []

    for elem in range(len(freeSlots)): # remove invalid free slots with respect to meeting duration

        try:
            meetingDifference = differenceBetween(freeSlots[elem][1], freeSlots[elem][0])
        except:
            break

        if meetingDifference < meetingDuration:

            del freeSlots[elem]

    #print("Parsed Free Slots ", freeSlots)

    for elem in range(len(freeSlots)):

        meetingDifference = differenceBetween(freeSlots[elem][1], freeSlots[elem][0])

        if meetingDifference == meetingDuration:

            validMeetingSlots.append(freeSlots[elem])

        elif meetingDifference > meetingDuration:

            lenOfLoop = meetingDifference // meetingDuration # floor division

            firstRun = True
            
            for i in range(lenOfLoop):

                tempList = []

                if firstRun == False:

                    tempList.append(validMeetingSlots[-1][-1])
                    #print(validMeetingSlots[-1])

                    toMin = toMinutes(validMeetingSlots[-1][-1])
                    newTime = toMin + meetingDuration
                    formattedTime = toTimeFormat(newTime)

                    tempList.append(formattedTime)

                else:

                    tempList.append(freeSlots[elem][0])

                    toMin = toMinutes(freeSlots[elem][0])
                    newTime = toMin + meetingDuration
                    formattedTime = toTimeFormat(newTime)

                    tempList.append(formattedTime)
                    

                    firstRun = False

                validMeetingSlots.append(tempList)

    #print("Valid Meeting Slots in Time Duration: ", validMeetingSlots)

    return mergedSchedules, freeSlots, validMeetingSlots


'''

    @parameters
        - person one schedule (in format)
        - person one working bounds (in format)
        - person two schedule (in format)
        - person two working bounds (in format)
        - time of meeting (in minutes)

    @return (in order)
        - merged busy schedules of both persons
        - all possible free slots among merged schedules
        - valid free slots with respect to the length of meeting

'''

mergedSchedules, allFreeSlots, durationalFreeSlots = meetingAvailability(pOneSchedule, pOneBounds, pTwoSchedule, pTwoBounds, meetingDuration)
#mergedSchedules, allFreeSlots, durationalFreeSlots = meetingAvailability(p1, p1Bound, p2, p2Bound, meetTime)

print("Merged Schedules: \n")
print(mergedSchedules)
print()
print("All Free Slots: \n")
print(allFreeSlots)
print()
print("Durational Free Slots \n")
print(durationalFreeSlots)
              
             
    
