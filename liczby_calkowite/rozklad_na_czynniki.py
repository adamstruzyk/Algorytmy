def czynniki_liczby(liczba):
     czynniki = []
     i = 2
     while liczba > 1:
        if liczba % i == 0:
            czynniki.append(i)
            liczba = liczba/i
        else: i+=1
     return czynniki

print(czynniki_liczby(100))