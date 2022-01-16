#
#

class BankAccount:
    def __init__(self, name):
        self.owner_name_ = name
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def getbalance(self):
        return self.balance


account_1 = BankAccount("Arif Eker")

print(account_1.owner_name_)  # Arif Eker

account_1.deposit(2750)
print(account_1.getbalance())  # 2750.0

account_1.withdraw(735)
print(account_1.getbalance())  # 2015.0
