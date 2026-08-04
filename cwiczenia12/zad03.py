"""
ZAD03

Napisz klasę Theatre opisującą rzędy oraz miejsca na widowni teatru.
Dla użytkownika klasy rzędy i miejsca są numerowane od 1. Konstruktor klasy
przyjmuje dowolną liczbę liczb całkowitych oznaczających liczbę miejsc w kolejnych rzędach.

Klasa powinna udostępniać następującą funkcjonalność:
• Metoda display wyświetla wszystkie miejsca w konsoli, wskazując,
  które są wolne, a które zostały sprzedane.
• Metoda buy_ticket wywołana z dwoma argumentami całkowitymi, row oraz seat,
  oznacza zakup biletu na miejsce seat w rzędzie row.
• Ta sama metoda wywołana z trzema argumentami: row, seat1 oraz seat2,
  oznacza zakup biletów na miejsca od seat1 do seat2 (włącznie) w rzędzie row.
• Metoda show_free wywołana z jednym argumentem row wypisuje listę wolnych miejsc w rzędzie row.
• Ta sama metoda wywołana bez argumentów wyświetla listy wolnych miejsc we wszystkich rzędach.
• Metoda show_summary, wywołana z ceną jednego biletu jako argumentem,
  wypisuje liczbę sprzedanych biletów, całkowitą liczbę miejsc oraz przychód teatru.
"""


class Theatre:
    def __init__(self, *rows):
        self.seats = [[True] * count for count in rows]

    def display(self):
        for i in range(len(self.seats)):
            row = []

            for j in range(len(self.seats[i])):
                if self.seats[i][j]:
                    row.append(str(j + 1))
                else:
                    row.append("xx")

            print(f"{i + 1}: {' '.join(row)}")

    def buy_ticket(self, row, seat1, seat2=None):
        if seat2 is None:
            start_seat = seat1
            end_seat = seat1
        else:
            start_seat = seat1
            end_seat = seat2

        for seat in range(start_seat, end_seat + 1):
            self.seats[row - 1][seat - 1] = False

    def show_free(self, row=None):
        if row is not None:
            seats = []

            for i in range(len(self.seats[row - 1])):
                if self.seats[row - 1][i]:
                    seats.append(i + 1)

            if len(seats) > 0:
                print(f"Row {row}, free seats: {seats}")
            else:
                print(f"Row {row}, free seats: No free seats")
        else:
            for i in range(1, len(self.seats) + 1):
                self.show_free(i)

    def show_summary(self, price):
        seats = 0
        free_seats = 0

        for i in self.seats:
            seats += len(i)
            for j in i:
                if j:
                    free_seats += 1

        sold_tickets = seats - free_seats
        income = sold_tickets * price

        print(f"Tickets sold: {sold_tickets}/{seats}, Income: {income}")


th = Theatre(4, 8, 10, 10)

th.display()

th.buy_ticket(1, 4)
th.buy_ticket(4, 1, 6)
th.buy_ticket(4, 10)
th.buy_ticket(2, 1, 8)
th.buy_ticket(3, 5, 10)

th.display()

th.show_free()
th.show_summary(5)
