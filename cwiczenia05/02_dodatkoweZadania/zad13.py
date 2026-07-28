"""
ZAD13

Utwórz klasę BankAccount z:
• saldem
• metodą deposit(amount)
• metodą withdraw(amount)
• zabezpieczeniem przed debetem
"""


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Brak wystarczających środków")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Bank account: {self.balance}"


account = BankAccount(100)
print(account)
account.deposit(50)
print(account)
account.withdraw(200)
account.withdraw(100)
print(account)
