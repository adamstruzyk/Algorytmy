#założenie:
#1. tablica musi byc posortowana
#algorytm zwraca index szukanej liczby lub  fałsz jesli szukanej nie znajdzie

def wyszukiwanie_binarne(tablica, szukana):
    lewa = 0
    prawa = len(tablica)-1
    while lewa <= prawa:
        srodek = (lewa + prawa) // 2
        if tablica[srodek] == szukana:
            return srodek
        elif tablica[srodek] < szukana:
            lewa = srodek + 1
        elif tablica[srodek] > szukana:
            prawa = srodek - 1
    return False

liczby = [3,2,6,5,3,9,10]
liczby.sort()

print(liczby)
print(wyszukiwanie_binarne(liczby, 6))
