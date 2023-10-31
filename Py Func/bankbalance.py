class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print("Account Number:",self.account_number)
        print("Balance: ${:.2f}".format(self.balance))

account1 = BankAccount("1234567890")

account1.deposit(2000)
account1.withdraw(500)

account1.display_balance()
