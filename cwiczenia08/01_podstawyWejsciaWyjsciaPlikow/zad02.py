"""
ZAD02

Policz, ile linii znajduje się w pliku hobbit.txt.
"""

line_count = 0

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    for line in file:
        line_count += 1

print(line_count)
