

class register():

    def getChange(self,num):
        
        billNames = ["Twenty Dollar Bill(s)","Ten Dollar Bill(s)","Five Dollar Bill(s)","One Dollar Bill(s)","Quarter(s)","Dime(s)","Nickel(s)","Penny(ies)"]
        bills = [20,10,5,1,.25,.1,.05,.01]
        numOfBills = [0,0,0,0,0,0,0,0]
        i = 0
        
        while num != 0: # conditional loop
            if len(numOfBills) == i: # termination of loop if counter i runs through array
                break
            if num / bills[i] > 1: # if the bill goes into the number at least once
                numOfBills[i] += 1 # push the bill counter once
                num -= bills[i] # subtract that bill from the number
            else:
                i+=1 # if the bill does not go into the number fully
        
        for i in range(0,len(bills)):
            if numOfBills[i] == 0:
                continue
            else:
                print(str(numOfBills[i])+" "+billNames[i])

    def transaction(self,costOfItem,amountGiven):
        print(' ')
        change = amountGiven - costOfItem
        if change == 0 or change < 0:
            return 0
        else:
            self.getChange(change)


register = register()

try:
    costOfItem = float(input("What is the cost of the item: "))
    amountGiven = float(input("What is the amount given to the cashier: "))
    register.transaction(costOfItem,amountGiven)
except:
    print('\nSystem.ErrorInput')

## No costOfItem or amountGiven error checking implemented


    
    



        
