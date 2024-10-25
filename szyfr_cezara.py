#funkcja kodująca znak z podanym kluczem
def koduj(znak,klucz):
    znak = znak.upper()
    if(ord(znak)+klucz<=90): return chr(ord(znak)+klucz)
    else: return chr((ord(znak)+klucz)-26)

#funkcja dekodująca znak z podanym kluczem
def dekoduj(znak, klucz):
    znak = znak.upper()
    if(ord(znak)-klucz >= 65): return chr(ord(znak)-klucz)
    else: return chr((ord(znak)-klucz)+26)


#przykład działania
text = input("Tekst przed szyfrowaniem: ")
klucz = int(input("Klucz: "))
print()

text_zaszyfrowany = ""
for litera in text:
    text_zaszyfrowany += koduj(litera, klucz)
print("Text po szyfrowaniu: ", text_zaszyfrowany)

text_odszyfrowany = ""
for litera in text_zaszyfrowany:
    text_odszyfrowany += dekoduj(litera, klucz)

print("Tekst po odszyfrowaniu: ", text_odszyfrowany, "\n")
