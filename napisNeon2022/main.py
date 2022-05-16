"""
DOPISZ - dopisz na koncu litere
ZMIEN - zmien ostania litere
usun - usuwa ostatnia litere
przesun - zmienia litere na kolejna w alfabecie
"""


def zadanie():
    plik = open('instrukcje.txt', 'r')
    napis = ''
    alfabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    ciag = []
    poprzednia_instrukcja = ''
    najdluzszy_ciag = 0
    najczestsza_instrukcja = ''
    litery = dict()
    for linia in plik:
        instrukcja, wartosc = linia.split()

        # 4.3
        if wartosc not in litery.keys():
            litery[wartosc] = 0
        else:
            litery[wartosc] += 1

        #4.2
        if len(ciag) <= 0:
            ciag.append(instrukcja)
        elif len(ciag) > 0:
            if instrukcja != poprzednia_instrukcja:
                if len(ciag) > najdluzszy_ciag:
                    najdluzszy_ciag = len(ciag)
                    najczestsza_instrukcja = poprzednia_instrukcja
                ciag = []
                poprzednia_instrukcja = instrukcja
            ciag.append(instrukcja)

        # tworzenie napisu
        if instrukcja == 'DOPISZ':
            napis += wartosc
        if instrukcja == 'ZMIEN':
            napis_lista = list(napis)
            napis_lista[-1] = wartosc
            napis = ''.join(napis_lista)
        if instrukcja == 'USUN':
            napis_lista = list(napis)
            napis_lista.pop()
            napis = ''.join(napis_lista)
        if instrukcja == 'PRZESUN':
            napis_lista = list(napis)
            if wartosc == 'Z':
                napis_lista[napis_lista.index(wartosc)] = alfabet[0]
            else:
                napis_lista[napis_lista.index(wartosc)] = alfabet[alfabet.index(wartosc) + 1]
            napis = ''.join(napis_lista)

    litery_sortowane = list(sorted(litery.items(), key=lambda item: item[1], reverse=True))[0]
    dlugosc_napisu = len(napis)
    print(dlugosc_napisu)
    print(najczestsza_instrukcja, najdluzszy_ciag)
    print(litery_sortowane[0], litery_sortowane[1])
    print(napis)
    plik.close()

zadanie()