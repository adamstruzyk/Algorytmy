liczba1 = 1
liczba2 = 0

def NWD(a,b):
    while a != b:
        if a > b:
            a -= b
        elif a < b:
            b -= a
    return a

print("największy wspólny dzielnik liczb "+str(liczba1)+" "+str(liczba2)+" to: "+str(NWD(liczba1,liczba2)))