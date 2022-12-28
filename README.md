# Bank-Domain
Input bank info and deposit and withdrawl


# Programming – Course-End Project (Banking Domain)
You need to complete and submit this project to successfully complete the course. 
Software Requirements: To perform the steps in this project, you need to install Python in your 
local system first. You can refer to Programming Basics - Demo Install Python in the course for 
more information on installation.

# Problem Statement:
(Use parameterized constructors in all classes to initialize default values)
## Create a bank class with the following attributes:
- IFSC_Code
- bankname
- branchname
- loc
## Create a customer class with the following attributes:
- CustomerID
- custname
- address
- contactdetails
## Create an account class that inherits from bank class with the following attributes (Use Super () to pass 
## value to the base class):
- AccountID
- Cust Object of Customer
- balance
### Add the following methods to get account information, withdraw, and deposit:
- getAccountInfo()
- deposit(2000,'true')
- widthraw(500)
- getBalance()

## Create a SavigsAccount class that inherits from the account with the following attributes (Use Super () to 
## pass valued to the base class):
● SMinBalance
### Add the following methods to get account information, withdraw, and deposit:
- getSavingAccountInfo()
- deposit(2000,'true')
- widthraw(500)
- getBalance()
### Validate MinBalance before allowing withdrawals. 
### Create a class that runs the program and accepts input from the end user to create respective class 
### objects and print details. Add a method to perform deposit and withdrawal transaction based on the 
### end user input.
