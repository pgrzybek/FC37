from Nauczyciele import Nauczyciele
from Uczniowie import Uczniowie
from Wychowawcy import Wychowawcy




def sprawdz_czy_to_liczba(wartosc):
    while 1:
        try:
            wartosc = int(wartosc)
            break
        # this will raise a ValueError
        except ValueError:
            print("To nie jest liczba")
            wartosc = input("Podaj liczbe \n")
            #if wartosc =="":
              #  return
    return wartosc


def wyswietl_klasy():
    nazwa_klasy=input("Podaj nazwe klasy ")
    print(f"Uczniowie klasy {nazwa_klasy} to")
    for uczen in Uczniowie.lista:
        if nazwa_klasy == uczen.klasa:
            #klasa.add(uczen.imie_i_nazwisko)
            print(uczen.imie_i_nazwisko)
    else:
        print("Nie znaleziono uczniow")
    print("Wychowawca to ")
    for wychowawca in Wychowawcy.lista:
        if wychowawca.klasa == nazwa_klasy:
            print(wychowawca.imie_i_nazwisko)
            break
    else:
        print("Nie znaleziono wychowawcy")


def utworz():
    while 1:
        print("1.Uczen")
        print("2 Nauczyciel")
        print("3.Wychowawca")
        print("4.Koniec")
        opcja_utworz = input("Wybierz opcje używając numerow 1-8. 8 Konczy program \n")
        opcja_utworz = sprawdz_czy_to_liczba(opcja_utworz)
        if opcja_utworz == 1:
            Uczniowie.dodaj()
        if opcja_utworz == 2:
            Nauczyciele.dodaj(Nauczyciele.lista)
        if opcja_utworz == 3:
            Wychowawcy.dodaj()
        if opcja_utworz == 4:
            break
        if 3 < opcja_utworz < 1:
            print("Zly wobor ")


def zarzadzaj():
    while 1:
        print("1.Uczen")
        print("2 Nauczyciel")
        print("3.Wychowawca")
        print("4.Klasa")
        print("5.Koniec")
        opcja_zarzadzaj = input("Wybierz opcje używając numerow 1-8. 8 Konczy program \n")
        opcja_zarzadzaj = sprawdz_czy_to_liczba(opcja_zarzadzaj)
        if opcja_zarzadzaj == 1:
            Uczniowie.wyswietl_uczniow()
        if opcja_zarzadzaj == 2:
            Nauczyciele.wyswietl_nauczycieli()
        if opcja_zarzadzaj == 3:
            Wychowawcy.wyswietl_wychowawce()
        if opcja_zarzadzaj == 4:
            wyswietl_klasy()
        if opcja_zarzadzaj == 5:
            break
        if 4 < opcja_zarzadzaj < 1:
            print("Zly wobor ")


while 1:
    print("1.Utworz")
    print("2.Zarzadzaj")
    print("3.Koniec")

    opcjaGlowna = input("Wybierz opcje używając numerow 1-8. 8 Konczy program \n")
    opcjaGlowna = sprawdz_czy_to_liczba(opcjaGlowna)
    if opcjaGlowna == 1:
        utworz()
    if opcjaGlowna == 2:
        zarzadzaj()
    if opcjaGlowna == 3:
        break

    if 3 < opcjaGlowna < 1:
        print("Zly wobor ")
