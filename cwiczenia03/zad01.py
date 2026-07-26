"""
ZAD01

Napisz program symulujący koszyk zakupowy.
Możesz zmodyfikować kod napisany na poprzednich zajęciach, ale tym razem użyć słownika.
Program powinien:
• umożliwić użytkownikowi dodawanie produktów wraz z ich cenami,
• zakończyć wprowadzanie danych po spełnieniu określonego warunku,
• obliczyć całkowitą wartość zakupów,
• znaleźć najdroższy produkt,
• obliczyć średnią cenę produktu.
Na końcu program powinien wyświetlić podsumowanie koszyka.
"""

shopping_cart = {}

while True:
    user_input = input("Wprowadź produkt do koszyka (wprowadź '0' aby zakończyć): ")

    if user_input == "0":
        break

    price = int(input("Wprowadź cenę: "))
    shopping_cart[user_input] = price

if shopping_cart:
    total_price = sum(shopping_cart.values())
    avg_price = total_price / len(shopping_cart)
    most_expensive_product = max(shopping_cart, key=shopping_cart.get)
    most_expensive_price = shopping_cart[most_expensive_product]

    print(f"Całkowita wartość: {total_price}")
    print(f"Najdroższy produkt: {most_expensive_product}")
    print(f"Średnia cena: {total_price / len(shopping_cart)}")

    for key, value in shopping_cart.items():
        print(f"{key}: {value}")
else:
    print("Koszyk jest pusty")
