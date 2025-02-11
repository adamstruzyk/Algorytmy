#wyszukiwanie wzorca w tekście
def znajdz_wzorzec(tekst, wzorzec):
    liczba_wystapien = 0
    dl1 = len(tekst)
    dl2 = len(wzorzec)
    for i in range(dl1-dl2+1):
        for j in range(dl2):
            if tekst[i+j] != wzorzec[j]: break
        else:
            print("Znaleziono wzorzec: ",wzorzec," na pozycji ", i)
            liczba_wystapien += 1

    if liczba_wystapien == 0: print("Nie znaleziono wzorca.")
    else: print("Wzorzec: '",wzorzec,"' znaleziono ", liczba_wystapien, " razy")

slowo = "matematyka"
znajdz_wzorzec(slowo, "mat")