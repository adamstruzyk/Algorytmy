def NWD(a,b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
liczba1 = 282
liczba2 = 78
print(NWD(liczba1,liczba2))