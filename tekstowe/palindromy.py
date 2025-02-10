#palindrom - wyraz ktory jest czytany tak samo od początku i końca
#np: kajak
def czy_palindrom(slowo):
    dlugosc = len(slowo)
    for i in range(dlugosc):
        if(slowo[i]==slowo[-i-1]): continue
        else: return False
    return True
print(czy_palindrom("11211"))