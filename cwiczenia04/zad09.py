"""
ZAD09

Stwórz klasę Song z polami name, duration, author i Playlist, która zawiera me
tody:
• add_song- dodaje piosenkę do playlisty.
• remove_song- usuwa piosenkę z playlisty.
• __iter__- iteruje po piosenkach.
• __len__- liczba utworów.
• __getitem__- dostęp po indeksie.
Dodaj generator long_songs() zwracający tylko utwory trwające powyżej 200s.
"""


class Song:
    def __init__(self, name, duration, author):
        self.name = name
        self.duration = duration
        self.author = author

    def __str__(self):
        return f"{self.name} {self.duration} {self.author}"


class Playlist:
    def __init__(self):
        self.song_list = []

    def __iter__(self):
        return iter(self.song_list)

    def __len__(self):
        return len(self.song_list)

    def __getitem__(self, index):
        return self.song_list[index]

    def add_song(self, song):
        self.song_list.append(song)

    def remove_song(self, song):
        if song in self.song_list:
            self.song_list.remove(song)

    def long_songs(self):
        for song in self.song_list:
            if song.duration > 200:
                yield song


s1 = Song("a", 234, "x")
s2 = Song("b", 125, "y")
s3 = Song("c", 421, "z")

playlist = Playlist()
playlist.add_song(s1)
playlist.add_song(s2)
playlist.add_song(s3)

print(f"Liczba piosenek: {len(playlist)}")
print(f"Pierwsza piosenka: {playlist[0]}")

print("\nPiosenki na playliście:")
for song in playlist:
    print(song)

print(f"\nUsuwanie piosenki {s2}")
playlist.remove_song(s2)
print(f"Aktualna liczba piosenek: {len(playlist)}")

print("\nPiosenki dłuższe niż 200s:")
for song in playlist.long_songs():
    print(song)
