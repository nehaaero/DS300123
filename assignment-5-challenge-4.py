class Account:

    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance 

class SavingsAccount(Account):

    def __init__(self, title, balance, intrestRate):
        super().__init__(title, balance)
        self.intrestRate= intrestRate

s=SavingsAccount("ashish" ,5000, 5)
print(s.title, s.balance, s.intrestRate)


    
    