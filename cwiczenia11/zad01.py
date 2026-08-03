"""
ZAD01

Utwórz klasę PasswordValidator ze statyczną metodą isStrong(password),
która zwraca True, jeśli:
• hasło ma co najmniej 8 znaków,
• zawiera co najmniej jedną cyfrę,
• zawiera co najmniej jedną wielką literę.
"""


class PasswordValidator:
    @staticmethod
    def isStrong(password):
        if len(password) < 8:
            return False

        if not any(ch.isdigit() for ch in password):
            return False

        if not any(ch.isupper() for ch in password):
            return False

        return True


print(PasswordValidator.isStrong(""))
print(PasswordValidator.isStrong(" "))
print(PasswordValidator.isStrong("asfdg345dsfg"))
print(PasswordValidator.isStrong("ASFGHadszfg"))
print(PasswordValidator.isStrong("ASFGHadsz456yfg"))
