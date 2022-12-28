class bank:
    #inial parent class
    def __init__(self, IFSC_Code, bankname, branchname, loc):
        
        self.IFSC_Code = IFSC_Code
        self.bankname = bankname
        self.branchname = branchname
        self.loc = loc
        
    def print_info(self):
        print('IFSC_Code    :', self.IFSC_Code)
        print('bankname     :', self.bankname)
        print('branchname   :', self.branchname)
        print('location     :', self.loc)

class customer:
    def __init__(self, CustomerID, custname, address, contactdetails):
        self.CustomerID = CustomerID
        self.custname = custname
        self.address = address
        self.contactdetails = contactdetails
        
class account(bank):
    def __init__(self, IFSC_Code, bankname, branchname, loc, AccountID, CustObjCustumer, balance):
        super().__init__(IFSC_Code, bankname, branchname, loc)
        self.AccountID = AccountID
        self.CustObjCustomer = CustObjCustumer
        self.balance = balance

    def getAccountInfo(self):
        print('IFSC_Code    :', self.IFSC_Code)
        print('bankname     :', self.bankname)
        print('branchname   :', self.branchname)
        print('location     :', self.loc)
        print('AccountID    :', self.AccountID)
        print('Obj of Cust  :', self.CustObjCustomer)
        print('balance      :', self.balance)
    
    def deposit(self, amount, forReal):
        if forReal == 'True':
            self.balance += amount
        
    def withdral(self, amount):
        self.balance -= amount

    def getBalance(self):
        print('Balance      :', self.balance)

class SavingsAccount(account):
    def __init__(self, IFSC_Code, bankname, branchname, loc, AccountID, CustObjCustumer, balance, SMinBalance):
        super().__init__(IFSC_Code, bankname, branchname, loc, AccountID, CustObjCustumer, balance)
        self.SMinBalance = SMinBalance

    def getSavingsAccountInfo(self):
        print('IFSC_Code    :', self.IFSC_Code)
        print('bankname     :', self.bankname)
        print('branchname   :', self.branchname)
        print('location     :', self.loc)
        print('balance      :', self.balance)
        print('min Balance  :', self.SMinBalance)

    def deposit(self, amount, forReal):
        if forReal == 'True':
            self.balance += amount
    def withdral(self, amount):
        if self.balance-amount > self.SMinBalance:
            self.balance -= amount
        else:
            print('Not enough funds')
        

    def getBalance(self):
        print('Balance      :', self.balance)

class main():
    def main():
        print('enter 1 for checking')
        print('enter 2 for savings')
        print('enter 0 to exit')
        
        action = input('Action: ')
        action = int(action)
        
        
        if action == 1:
            print('\nStart a checking account:\n')
            IFSC_Code = input('IFSC_Code:')
            bankname = input('bankname: ')
            branchname = input('branchname: ')
            location = input('location: ')
            AcountID = input('AccountID: ')
            custObjCustumer = input('cust Object of Customer: ')
            balance = input('balance: ')
            checking = account(IFSC_Code, bankname, branchname, location, AcountID, custObjCustumer, balance) 
            print('\n')
            print(account.getAccountInfo(checking))
            print('\n')
            action = input('enter 3 to deposit and 4 to withdrawl: ')
            action = int(action)
            if action == 3:
                print('\nDeposit into checking account\n')   
                depo = input('How much would you like to deposit? ')
                depo = int(depo); balance = int(balance)
                balance += depo
                print('Checking account balance: ', balance)
            if action == 4:
                print('\nWithdrawl from checking accout\n')
                withd = input('How much would you like to withdrawl? ')
                withd = int(withd); balance = int(balance)
                balance -= withd
                print('Checking account balance: ', balance)


        if action == 2:
            print('\nStart a savings account:\n')
            IFSC_Code = input('IFSC_Code:')
            bankname = input('bankname: ')
            branchname = input('branchname: ')
            location = input('location: ')
            AcountID = input('AccountID: ')
            custObjCustumer = input('cust Object of Customer: ')
            balance = input('balance: ')
            minSaving = input('minumum Savings deposit: ')
            savings = SavingsAccount(IFSC_Code, bankname, branchname, location, AcountID, custObjCustumer, balance, minSaving)
            print('\n')
            print(SavingsAccount.getSavingsAccountInfo(savings))
            print('\n')

            action = input('enter 3 to deposit and 4 to withdrawl: ')
            action = int(action)
            if action == 3:
                print('\nDeposit into savings account\n')   
                depo = input('How much would you like to deposit? ')
                depo = int(depo); balance = int(balance)
                balance += depo
                print('Savings account balance: ', balance)
            if action == 4:
                print('\nWithdrawl from savings accout\n')
                withd = input('How much would you like to withdrawl? ')
                withd = int(withd); balance = int(balance); minSaving = int(minSaving)
                print(type(withd), type(balance),type(minSaving))
                if minSaving > balance - withd:
                    print('Below minumum balance of', minSaving)
                    exit
                balance -= withd
                print('Checking account balance: ', balance)
    
        if action == 0:
            exit
Banking = main
Banking.main()