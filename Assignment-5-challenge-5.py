class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
        
    def getBalance(self):
        return self.balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdrawal(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate
        
    def interestAmount(self):
        return self.balance * self.interestRate / 100
savings_account = SavingsAccount("Ashish", 2000, 5)

balance = savings_account.getBalance()
print(balance)
savings_account = SavingsAccount("Ashish", 2000, 5)
savings_account.deposit(500)
balance = savings_account.getBalance()
print(balance)
savings_account = SavingsAccount("Ashish", 2000, 5)
savings_account.withdrawal(500)
balance = savings_account.getBalance()
print(balance)
savings_account = SavingsAccount("Ashish", 2000, 5)
interest_amount = savings_account.interestAmount()
print(interest_amount)
