"""
ZAD03

Napisz klasę Product z polami takimi jak nazwa, cena, kategoria oraz klasę Cart przechowującą produkty.
Funkcjonalności:
• Przeciąż:
    – __len__ - liczba produktów w koszyku.
    – __iter__ - iterator po produktach.
    – __getitem__ - możliwość dostępu do produktów po indeksach wg. kolejności dodawania do koszyka.
• Dodaj rabat na 10% do kategorii food.
• Dodaj rabat na 15% na cały koszyk.
• Podwyższ cenę produktów z kategorii "elektronika" o 100%
Dodatkowe metody:
    – total_price() - zwraca całkowitą cenę po dodaniu rabatów.
    – show_items() - drukuje cały koszyk.
    – clear() - usuwa wszystko z koszyka.
"""


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} {self.price} {self.category}"


class Cart:
    def __init__(self):
        self.product_list = []

    def __len__(self):
        return len(self.product_list)

    def __iter__(self):
        return iter(self.product_list)

    def __getitem__(self, index):
        return self.product_list[index]

    def add_product(self, product):
        self.product_list.append(product)

    def total_price(self):
        total = 0

        for prod in self.product_list:
            price = prod.price

            if prod.category == "food":
                price *= 0.9
            elif prod.category == "elektronika":
                price *= 2

            total += price

        total *= 0.85

        return round(total, 2)

    def show_items(self):
        if not self.product_list:
            print("Koszyk jest pusty")
            return

        for item in self:
            print(item)

    def clear(self):
        self.product_list.clear()


p1 = Product("mleko", 3, "food")
p2 = Product("monitor", 100, "elektronika")

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)

print("Zawartość koszyka:")
print("1 sposób")
for item in cart:
    print(item)
print("2 sposób")
cart.show_items()

print("\nPodsumowanie")
print(f"Liczba produktow w koszyku: {len(cart)}")
print(f"Łączna cena: {cart.total_price()}")
print(f"Pierwszy produkt: {cart[0]}")

print("\nCzyszczenie koszyka:")
cart.clear()
cart.show_items()
