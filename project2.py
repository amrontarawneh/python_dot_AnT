class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def check_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)
account.check_balance()