
class BankAccounts:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if(amount < 0):
            print("Enter valid amount")
            return
        self.balance += amount
    
    def withdraw(self, amount):
        if(amount < 0):
            print("Enter valid amount")
            return
        elif self.balance < amount:
            print("Not enough balance")
            return
        else:
            self.balance -= amount
            print("Money withdrawed successfully")

    def checkBalance(self):
        print("Available balance is : ", self.balance)


if __name__ == "__main__":
    account = BankAccounts()
    try:
        account.deposit(500)
        account.withdraw(100)
        account.checkBalance() 
    except ValueError as e:
        print(e)  
    