"""
ZAD04

Utwórz klasę BankAccount zawierającą:
• atrybut klasowy bankName,
• metodę klasową changeBankName(newName).
Pokaż, że zmiana nazwy banku wpływa na wszystkie konta.
"""


class BankAccount:
    bankName = "Bank1"

    @classmethod
    def changeBankName(cls, newName):
        cls.bankName = newName


b1 = BankAccount()
b2 = BankAccount()

print(b1.bankName)
print(b2.bankName)

BankAccount.changeBankName("Bank2")

print(b1.bankName)
print(b2.bankName)
