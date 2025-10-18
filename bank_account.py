
class BankAccount:
    
    #initilize Bank Account attribute
    def __init__(self, account_holder:str, initial_balance:int = 0):
        self.account_holder = account_holder
        self.initial_balance = initial_balance
    
    #add amount to balance account
    def depoist (self, amount:int)->int:
        self.initial_balance += amount
        return self.initial_balance
    
    #subtract amount from balance account
    def withdraw(self,amount:int)->int:
        #check if the balance account more than or equal amount
        if self.initial_balance >= amount:
            self.initial_balance -= amount
            return self.initial_balance
        else: raise ValueError ("the balance amount is not enugh.")

    #return current initial balance acount
    def get_balance(self):
        return self.initial_balance
    
    #return account holder name
    def get_account_holder(self):
        return self.account_holder
    