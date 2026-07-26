"""
ZAD05

Utwórz listę imion (mogą się powtarzać).
Program powinien:
• utworzyć i wydrukować listę długości tych imion,
• utworzyć słownik, w którym kluczami są długości imion,
a wartościami listy imion o tej długości,
• utworzyć słownik, w którym kluczami są długości imion,
a wartościami zbiory imion o tej długości,
• utworzyć słownik, w którym kluczami są imiona,
a wartościami liczby wystąpień danego imienia.
"""

names = ["John", "Mary", "Kitty", "Alice", "John", "Mary", "Al", "Bill", "John", "Alice", "Al"]

name_len_list = []
dict_name_len_list = {}
dict_name_len_set = {}
dict_name_count = {}

for name in names:
    name_len = len(name)

    name_len_list.append(name_len)

    if name_len not in dict_name_len_list:
        dict_name_len_list[name_len] = []
    dict_name_len_list[name_len].append(name)

    if name_len not in dict_name_len_set:
        dict_name_len_set[name_len] = set()
    dict_name_len_set[name_len].add(name)

    if name not in dict_name_count:
        dict_name_count[name] = 0
    dict_name_count[name] += 1

print(name_len_list)
print(dict_name_len_list)
print(dict_name_len_set)
print(dict_name_count)
