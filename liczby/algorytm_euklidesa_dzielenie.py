def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = 282
b = 78

wynik = nwd(a, b)
print(f"NWD({a}, {b}) = {wynik}")
