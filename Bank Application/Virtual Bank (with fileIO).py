import sys as s    

class bankMenu:

    print('Welcome to the Bank of Uday')

    def menuOption(self):
        try:
            print('\n[1] Login')
            print('[2] Create Account')
            print('[3] Forgot Password?')
            print('[4] User Accounts Admin Access (Administrative Password Required)')
            print('[5] Exit')

            prompt = int(input('Select an option: '))
            
            if prompt == 1:
                bankMenu.login(self)
            elif prompt == 2:
                bankMenu.createAccount(self)
            elif prompt == 3:
                bankMenu.forgotPassword(self)
            elif prompt == 4:
                bankMenu.adminOption(self)
            elif prompt == 5:
                bankMenu.leave(self)
            else:
                print('\nInvalid Input')
                bankMenu.menuOption(self)
        except:
            print('\nMainframe Input Error - 171')
            bankMenu.menuOption(self)

    def leave(self):
        print('\nThank You')
        quit

    def forgotPassword(self):
        try:
            
            userBase = open('username.txt','r')
            passBase = open('password.txt','r')

            userData = userBase.read()
            passData = passBase.read()

            userData = userData.split()
            passData = passData.split()

            username = input('\nEnter your username: ')
            if username not in userData:
                print('\nThat is not a valid username in the directory')
                backMenu.menuOption(self)
            
            adminPass = input('Enter the admin password: ')
            if adminPass != 'admin':
                print('\nThat is not the admin password')
                backMenu.menuOption(self)

            spot = userData.index(username)
            password = passData[spot]
            
            if userData.index(username) == passData.index(password):
                print('\nThe password of '+ str(username) + ' is ' + passData[spot])

            userBase.close()
            passBase.close()
            
            bankMenu.menuOption(self)
        except:
            userBase.close()
            passBase.close()
            print('Password Retreival Error - 151')
            bankMenu.menuOption(self)

    def login(self):
        try:

            userBase = open('username.txt','r')
            passBase = open('password.txt','r')

            userData = userBase.read()
            passData = passBase.read()

            userData = userData.split()
            passData = passData.split()

            username = input('\nEnter your username: ')
            if username not in userData:
                print('\nInvalid Input or non-registered user')
                bankMenu.menuOption()

            password = input('Enter your password: ')
            if password not in passData:
                print('\nInvalid Input or incorrect password')
                bankMenu.menuOption()

            if userData.index(username) == passData.index(password):
                print('\nLogin Successful!')

                userBase.close()
                passBase.close()
                
                bankAccount.transactionOption(self,username)
            else:
                print('\nAuthentication error')
                bankMenu.menuOption(self)
            
        except:
            userBase.close()
            passBase.close()
            print('\nLogin Error - 191')
            bankMenu.menuOption(self)

    def createAccount(self):
        try:

            userBase = open('username.txt','a')
            passBase = open('password.txt','a')
            balBase = open('balance.txt','a')

            username = input('\nEnter your first name: ')
            userBase.write('\n')
            userBase.write(username)

            password = input('Enter your password: ')
            passBase.write('\n')
            passBase.write(password)

            balBase.write('\n')
            balBase.write('100')

            print('\nAccount created successfully')

            userBase.close()
            passBase.close()
            balBase.close()

            bankMenu.menuOption(self)

        except:
            userBase.close()
            passBase.close()
            balBase.close()
            print('\nAccunt Creation Error - 299')
            bankMenu.menuOption(self)

    def adminOption(self):
        try:
            internalPass = input('\nEnter the administrative password: ')
            if internalPass != 'admin':
                print('\nIncorrect password')
                bankMenu.menuOption(self)
            else:
                userBase = open('username.txt','r')
                passBase = open('password.txt','r')
                balBase = open('balance.txt','r')

                userData = userBase.read()
                passData = passBase.read()
                balData = balBase.read()

                userData = userData.split()
                passData = passData.split()
                balData = balData.split()

                print('\n| USERNAME | PASSWORD | BALANCE |\n')
                c = 0
                for i in range(len(userData)):
                    print('| ' + userData[c] + ' | ' + passData[c] + ' | ' + balData[c] + ' |')
                    c+=1

                userBase.close()
                passBase.close()
                balBase.close()

                print('\n[1] Return to Bank Menu')
                print('[2] Remove an account')
                selection = int(input('Select an option: '))

                if selection == 1:
                    bankMenu.menuOption(self)
                elif selection == 2:
                    bankMenu.removeAccount(self)
                else:
                    print('\nInvalid Input Error')
                    bankMenu.menuOption()
                    
        except:
            userBase.close()
            passBase.close()
            balBase.close()
            print('\nError Exception - Admin 303')
            bankMenu.menuOption(self)


    def removeAccount(self):
        try:

            account = input('\nEnter the exact name of the account for deletion: ')

            userBase = open('username.txt','r')
            passBase = open('password.txt','r')
            balBase = open('balance.txt','r')

            userData = userBase.read()
            passData = passBase.read()
            balData = balBase.read()

            userData = userData.split()
            passData = passData.split()
            balData = balData.split()

            if account not in userData:
                print('\nInvalid account or incorrect entry')
                bankMenu.menuOption(self)
            else:
                spot = userData.index(account)

                del userData[spot]
                text = open('username.txt','w')
                for i in userData:
                    text.write(i+'\n')
                text.close()

                del passData[spot]
                text = open('password.txt','w')
                for i in passData:
                    text.write(i+'\n')
                text.close()

                del balData[spot]
                text = open('balance.txt','w')
                for i in balData:
                    text.write(i+'\n')
                text.close()

                userBase.close()
                passBase.close()
                balBase.close()

                print('\nAccount successfully deleted')
                bankMenu.menuOption(self)
        except:
            print('\nRemoval Error - 304')
            bankMenu.menuOption(self)
 

class bankAccount():

    def transactionOption(self, username):
        try:
            print('\n[1] View Balance')
            print('[2] Deposit')
            print('[3] Withdraw')
            print('[4] Logout')
            print('[5] Exit')
            select = int(input('Select an option: '))

            if select == 1:
                bankAccount.viewBalance(self, username)
            elif select == 2:
                bankAccount.deposit(self, username)
            elif select == 3:
                bankAccount.withdraw(self, username)
            elif select == 4:
                bankMenu.menuOption(self)
            elif select == 5:
                bankMenu.leave(self)
            else:
                print('\nTransaction Error - 405')
                bankAccount.transactionOption(self, username)
        except:
            print('\nTransaction Error - 402')
            bankAccount.transactionOption(self, username)

    def viewBalance(self, username):
        try:
            userBase = open('username.txt','r')
            balBase = open('balance.txt','r')

            userData = userBase.read()
            balData = balBase.read()

            userData = userData.split()
            balData = balData.split()

            spot = userData.index(username)
            balance = balData[spot]

            print('\nCurrent Balance: $'+balance)

            userBase.close()
            balBase.close()
            bankAccount.transactionOption(self, username)
        except:
            userBase.close()
            balBase.close()
            print('\nBalance Retreival Error - 901')
            bankAccount.transactionOption(self, username)

    def deposit(self, username):
        try:
            userBase = open('username.txt','r+')
            balBase = open('balance.txt','r+')

            userData = userBase.read()
            balData = balBase.read()

            userData = userData.split()
            balData = balData.split()

            spot = userData.index(username)
            balance = balData[spot]

            amount = float(input('\nEnter the deposit amount: '))
            if amount > 0:
                newbalance = str((float(balance)) + amount)

                balData[spot] = newbalance
                text = open('balance.txt','w')
                for i in balData:
                    text.write(str(i)+'\n')
                text.close()  
          
                print('\nDeposit successful!')
                
                userBase.close()
                balBase.close()
                bankAccount.transactionOption(self, username)
            else:
                print('\nInternal Deposit Error - 212')
                bankAccount.transactionOption(self, username)
        except:
            userBase.close()
            balBase.close()
            print('\nDeposit Input Error - 708')
            bankAccount.transactionOption(self, username)

    def withdraw(self, username):
        try:
            userBase = open('username.txt','r+')
            balBase = open('balance.txt','r+')

            userData = userBase.read()
            balData = balBase.read()

            userData = userData.split()
            balData = balData.split()

            spot = userData.index(username)
            balance = balData[spot]

            amount = float(input('\nEnter the withdrawal amount: '))
            if amount <= float(balance):
                newbalance = str((float(balance)) - amount)

                balData[spot] = newbalance
                text = open('balance.txt','w')
                for i in balData:
                    text.write(str(i)+'\n')
                text.close()  
          
                print('\nWithdrawal successful!')
                
                userBase.close()
                balBase.close()
                bankAccount.transactionOption(self, username)
            else:
                print('\nWithdrawal Error - 787')
                bankAccount.transactionOption(self, username)
        except:
            print('\nWithdrawal Error - 788')
            bankAccount.transactionOption(self, username)
                
        

Bank = bankMenu()
Bank.menuOption()



## Some code if I kept one database instead of three. Display all accounts from mainframe text file

## mainBase = open('mainframe.txt','r')
## mainData = mainBase.read()
## mainData = mainData.split('\n')
## c = 0
## print('| USERNAME | PASSWORD | BALANCE |')
## for i in mainData:
##     acc = i.split(',')
##     print('Account '+str(c)+':', acc)
##     c+=1


