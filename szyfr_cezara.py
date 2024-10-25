#funkcja kodująca znak z zadanym kluczem

def koduj(znak,klucz):
    znak = znak.upper()
    if(ord(znak)+klucz<=90):
        return chr(ord(znak)+klucz)
    else:
        return chr((ord(znak)+klucz)-26)

def dekoduj(znak, klucz):
    znak = znak.upper()
    if(ord(znak)-klucz >= 65):
        return chr(ord(znak)-klucz)
    else:
        return chr((ord(znak)-klucz)+26)