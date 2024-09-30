#do wyznaczenia nww służy wzór -> (a/nwd(a,b))*b
def NWD(a,b):
    while a!=b:
        if a>b:
            a -= b
        else:
            b -= a
    return a

def NWW(a,b):
    dzielnik = NWD(a,b)
    return int((a/dzielnik)*b)

liczba1 = 282
liczba2 = 78

print("NWW liczb "+str(liczba1)+" "+str(liczba2)+" wynosi: "+str(NWW(liczba1,liczba2)))
