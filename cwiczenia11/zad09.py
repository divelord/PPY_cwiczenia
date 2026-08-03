"""
ZAD09

Utwórz klasę TemperatureConverter z dwiema statycznymi metodami:
• celsiusToFahrenheit(c)
• fahrenheitToCelsius(f)
Metody nie powinny korzystać z żadnych atrybutów obiektu ani klasy.

Rozszerz program tak, aby metody mogły działać nie tylko na pojedynczej liczbie,
ale również na liście lub krotce temperatur.
Na przykład użytkownik powinien móc przekazać:
    25
    [10, 20, 30]
    ("15", "18", 21)

Jeśli napis zawiera poprawną liczbę, należy automatycznie przekonwertować go na typ liczbowy.
Dla niepoprawnych wartości należy zgłosić wyjątek ValueError.

Klasa powinna również obsługiwać wczytywanie temperatur z pliku tekstowego.
Załóż, że plik zawiera jedną wartość w każdym wierszu. Puste wiersze należy ignorować.

Dodaj kolejną statyczną metodę:
    saveResults(filename, data)
która zapisuje przekonwertowane temperatury do pliku.

Zaprezentuj działanie programu dla:
• pojedynczej temperatury,
• kolekcji temperatur,
• temperatur wczytanych z pliku.

Wskazówki:
• Użyj isinstance() do sprawdzania typów danych.
• Możesz użyć float() do konwersji napisów na liczby.
• Użyj with open(...) podczas pracy z plikami.
• Metodę statyczną deklaruje się przy użyciu @staticmethod.
"""


class TemperatureConverter:
    @staticmethod
    def _parse(value):
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Niepoprawna wartość {value}")

    @staticmethod
    def celsiusToFahrenheit(c):
        if isinstance(c, (list, tuple)):
            fahrenheit_list = []

            for i in c:
                temp = TemperatureConverter._parse(i)
                result = temp * 9 / 5 + 32

                fahrenheit_list.append(result)

            return fahrenheit_list

        temp = TemperatureConverter._parse(c)

        return temp * 9 / 5 + 32

    @staticmethod
    def fahrenheitToCelsius(f):
        if isinstance(f, (list, tuple)):
            celsius_list = []

            for i in f:
                temp = TemperatureConverter._parse(i)
                result = (temp - 32) * 5 / 9

                celsius_list.append(result)

            return celsius_list

        temp = TemperatureConverter._parse(f)

        return (temp - 32) * 5 / 9

    @staticmethod
    def loadFromFile(filename):
        temperatures = []

        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()

                if clean_line:
                    temperatures.append(clean_line)

        return temperatures

    @staticmethod
    def saveResults(filename, data):
        with open(filename, 'w', encoding="utf-8") as file:
            if isinstance(data, (list, tuple)):
                for i in data:
                    file.write(str(i) + "\n")
            else:
                file.write(str(data) + "\n")


print("Pojedyncze wartości")
single_ctf = TemperatureConverter.celsiusToFahrenheit(25)
single_ftc = TemperatureConverter.fahrenheitToCelsius("77")
print(single_ctf)
print(single_ftc)

print("Wartości z listy")
list_ctf = TemperatureConverter.celsiusToFahrenheit([10, "20"])
list_ftc = TemperatureConverter.fahrenheitToCelsius([14, "50"])
print(list_ctf)
print(list_ftc)

print("Wartości z krotki")
tuple_ctf = TemperatureConverter.celsiusToFahrenheit((10, "20"))
tuple_ftc = TemperatureConverter.fahrenheitToCelsius((14, "50"))
print(tuple_ctf)
print(tuple_ftc)

print("Dane z pliku")
from_file = TemperatureConverter.loadFromFile("temperatures.txt")
file_ctf = TemperatureConverter.celsiusToFahrenheit(from_file)
file_ftc = TemperatureConverter.fahrenheitToCelsius(from_file)
print(file_ctf)
print(file_ftc)

print("Zapis do pliku")
TemperatureConverter.saveResults("temperaturesResSingle.txt", single_ctf)
TemperatureConverter.saveResults("temperaturesResList.txt", list_ftc)
TemperatureConverter.saveResults("temperaturesResTuple.txt", tuple_ctf)
