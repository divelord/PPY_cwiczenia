"""
ZAD02

Mając listę napisów, utwórz słownik, gdzie kluczem jest napis, a wartością jego długość.
"""

lst = ["adsf", "dfsvd", "sadvf", "sadvf", "sacdv"]
dct = {el: len(el) for el in lst}
print(dct)
