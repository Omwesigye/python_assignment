#bank accounts:savingaccount current account inherit from bank account
#deposit,withdrawals,display balance,types of accounts

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit (self, ammount):
        self.balance +=ammount
        print(f'deposited {ammount} New balance:{self.balance}')
        
    def withdraw (self, ammount):
        if ammount <=self.balance:
             self.balance -=ammount
             print(f'withdraw {ammount} New balance:{self.balance}')
        else:
            print('insufficient funds')  
    def display_balance(self):
        print(f'Account {self.account_number} Balance:{self.balance}')
        
class SavingAccount(BankAccount):
    def __init__(self, account_number, balance,interest_rate):
        super().__init__(account_number, balance)  
        self.interest_rate = interest_rate #store the interest rate      
    
    def add_interest(self):
        interest = self.balance * self.interest_rate/100
        #add interest
        self.balance += interest
        print(f'interest of {interest}added. New Balance:{self.balance}')
        
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance,overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit     #store overdraft
        
    def withdraw(self, ammount):
        if ammount <= self.balance + self.overdraft_limit:
            self.balance -=ammount  
            print(f'withdrew {ammount}.New balance:{self.balance}')
        else:
            print("exceeded the overdraft limit")  
            
            #objects
saving = SavingAccount("SAV055555",100000,5)  
current = CurrentAccount("CUR05777",50000,10) 

#test method      
saving.display_balance()
saving.add_interest()
saving.withdraw(20000)
print("LB-----------------------")
current.display_balance()
current.withdraw(70000)
current.withdraw(45000)