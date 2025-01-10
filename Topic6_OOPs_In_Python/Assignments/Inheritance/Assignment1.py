
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

class SavingsAccount(BankAccounts):
    def __init__(self, interest_rate = 0.02, transaction_limit = 5):
        super().__init__()
        self.interest_rate = interest_rate
        self.transaction_limit = transaction_limit
        self.transactions = 0

    def deposit(self, amount):
        isPossible = self.check_transaction_limit()
        if(isPossible):
            super().deposit(amount)
            self.transactions += 1

    def withdraw(self, amount):
        isPossible = self.check_transaction_limit()
        if(isPossible):
            super().withdraw(amount)
            self.transactions += 1
            self.check_transaction_limit()

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Interest: ${interest:.2f}")
        return interest

    def check_transaction_limit(self):
        if self.transactions >= self.transaction_limit:
            print("Transaction limit exceeded!")
            return False
        else: return True

    def check_loan_eligibility(self):
        if self.balance >= 1000:
            print("Eligible for a loan")
        else:
            print("Not eligible for a loan")


class CheckingAccount(BankAccounts):
    def __init__(self, reward_points=0):
        super().__init__()
        self.reward_points = reward_points

    def deposit(self, amount):
        super().deposit(amount)
        self.add_reward_points(amount)

    def add_reward_points(self, amount):
        points = int(amount / 10)
        self.reward_points += points
        print(f"Earned {points} reward points. Total: {self.reward_points} points")

if __name__ == "__main__":
    account = BankAccounts()
    try:
        # account.deposit(500)
        # account.withdraw(100)
        # account.checkBalance() 

        savings_account = SavingsAccount(interest_rate=0.03)
        savings_account.deposit(500)
        savings_account.withdraw(100)
        savings_account.checkBalance()
        savings_account.calculate_interest()
        savings_account.check_loan_eligibility()

        checking_account = CheckingAccount()
        checking_account.deposit(1000)
        checking_account.checkBalance()

    except ValueError as e:
        print(e)  
    