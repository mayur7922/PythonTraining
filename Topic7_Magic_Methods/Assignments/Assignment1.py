class Transaction:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description
    

    def __str__(self):
        return f"{self.description}: ${self.amount}"

    def __eq__(self, other):
        return self.amount == other.amount and self.description == other.description

    def __add__(self, other):
        new_amount = self.amount + other.amount
        new_description = f"{self.description} + {other.description}"
        return Transaction(new_amount, new_description)

if __name__ == "__main__":

    t1 = Transaction(100, "Deposit")
    t2 = Transaction(50, "Deposit")
    t3 = Transaction(100, "Deposit")

    print(t1 == t2)
    print(t1 + t2)
