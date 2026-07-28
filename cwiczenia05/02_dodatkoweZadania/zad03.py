"""
ZAD03

Napisz funkcję, która przyjmuje listę i zwraca krotkę zawierającą:
• najczęściej występujący element,
• liczbę jego wystąpień.
W przypadku remisu dowolna poprawna odpowiedź jest akceptowana.
Ograniczenia:
• użyj tylko jednej pętli,
• nie używaj collections.Counter.
"""


def most_frequent(lst):
    freq = {}
    el = lst[0]
    count = 1

    for i in lst:
        freq[i] = freq.get(i, 0) + 1

        if freq[i] > count:
            count = freq[i]
            el = i

    return el, count


lst = [1, 2, 3, 3, 2, 'a', 'a', 'c', 'd', 'a']
print(most_frequent(lst))
