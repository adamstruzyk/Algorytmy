#iteracyjnie
def fibo(n):
    if n < 3: return 1
    else:
        p1, p2, wynik = 1, 1, 0
        for i in range(3, n+1):
            wynik = p1 + p2
            p2 = p1
            p1 = wynik
        return wynik

#ciąg fibonacciego:
# 1,1,2,3,5,8,13,21
print(fibo(8))