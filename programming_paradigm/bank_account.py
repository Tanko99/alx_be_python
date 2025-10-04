class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        else: 
            return False


    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True 

    def display_balance(self):
        print(f"Current balance: ${self.account_balance}")
        return self.account_balance