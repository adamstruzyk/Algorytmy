def czy_pierwsza(n):
    if n == 1: return False
    else:
        i = 2
        while i*i<=n: 
            if n%i==0: return False
            i += 1
        return True

liczba = 113
if czy_pierwsza(liczba):
    print(str(liczba)+" jest liczbą pierwszą")
else:
    print(str(liczba)+" nie jest liczbą pierwszą")