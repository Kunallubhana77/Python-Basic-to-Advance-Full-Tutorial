class account:
    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance += amount

def show__balance(self):
    print("balance is", self.__balance)

a1 = account()
a1.deposit(1000)
a1.show__balance()


