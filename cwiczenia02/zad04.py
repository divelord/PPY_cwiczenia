"""
ZAD 4

Napisz program symulujący koszyk zakupowy.
Program powinien:
• przechowywać ceny produktów w liście,
• umożliwić dodawanie produktów w pętli,
• zakończyć dodawanie produktów, gdy użytkownik wprowadzi 0.
Następnie program powinien:
• obliczyć całkowitą wartość zakupów,
• znaleźć najdroższy produkt,
• obliczyć średnią cenę produktu,
• wyświetlić produkty w odwrotnej kolejności używając slicing.
"""

shopping_cart = []
prices = []

while True:
    product = input("Podaj produkt (0 aby zakończyć): ")

    if product == "0":
        break

    price = int(input(f"Podaj cenę {product}: "))

    shopping_cart.append(product)
    prices.append(price)

if len(shopping_cart) > 0:
    total_price = sum(prices)
    avg_price = total_price / len(prices
                                  )
    most_expensive = 0

    for i in range(len(prices)):
        if prices[i] > prices[most_expensive]:
            most_expensive = i

    print(f"Łączna cena: {total_price}")
    print(f"Najdroższy produkt: {shopping_cart[most_expensive]} {prices[most_expensive]}")
    print(f"średnia cena: {avg_price}")
    print(f"Produkty w odwrotnej kolejności: {shopping_cart[::-1]}")
else:
    print("Koszyk jest pusty")
