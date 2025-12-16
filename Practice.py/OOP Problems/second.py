# Create a BankAccount class with deposit, withdraw, and balance check.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"Current Balance for {self.owner}: ${self.balance}")

# Testing the class
account = BankAccount("Kunal", 1000)
account.check_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(2000) # Should fail
