from Nauczyciele import Nauczyciele
from Uczniowie import Uczniowie
from Wychowawcy import Wychowawcy


def operacje_wykonane(slownik, wartosc):
    if slownik:  # jeśli słownik nie jest pusty
        nowy_klucz = max(slownik.keys()) + 1
    else:  # jeśli pusty, zaczynamy od 0
        nowy_klucz = 0
    slownik[nowy_klucz] = wartosc
    return slownik


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


def dodaj():
    imie_i_nazwisko = input("Podaj imie i nazwisko ze spacja w srodku \n")
    klasa = input("Podaj klase \n")
    return imie_i_nazwisko, klasa


def dodaj_ucznia():
    print("Dodaj ucznia")
    imie_i_nazwisko, klasa = dodaj()
    Uczniowie.lista.append(Uczniowie(imie_i_nazwisko, klasa))


def dodaj_wychowawce():
    print("Dodaj wychowawce")
    imie_i_nazwisko, klasa = dodaj()
    Wychowawcy.lista.append(Wychowawcy(imie_i_nazwisko, klasa))


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




def wyswietl_wychowawce():
    imie_wychowawcy=input("Podaj imie i nazwisko wychowawcy ze spacja w srodku \n")
    print("Uczniowie tego wychowawcy to")
    #znaleziony=wychowawcy.imie_i_nazwisko=imie_wychowawcy.rfind(imie_wychowawcy)
    for wychowawca in Wychowawcy.lista:
        if wychowawca.imie_i_nazwisko==imie_wychowawcy:
            for i in range(len(Uczniowie.lista)):
                if wychowawca.klasa == Uczniowie.lista[i].klasa:
                    print(Uczniowie.lista[i].imie_i_nazwisko)
            break
        else:
            print("Nie znaleziono wychowawcy")



def wyswietl_uczniow():
    imie_ucznia=input("Podaj imie i nazwisko ucznia ze spacja w srodku \n")
    wybrany=""
    for uczen in Uczniowie.lista:
        if imie_ucznia == uczen.imie_i_nazwisko:
            wybrany=uczen
            break
    print("Uczen ma te przedmioty i tych nauczycieli")
    if wybrany != "":
        klasa_ucznia=wybrany.klasa
        for nauczyciel in Nauczyciele.lista:
            for i in range(len(nauczyciel.klasa)):
                if nauczyciel.klasa[i] == klasa_ucznia:
                    print(nauczyciel.imie_i_nazwisko)
                    print(nauczyciel.przedmiot)
        else:
            print("nie znaleziono ucznia")


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
            Nauczyciele.dodaj_nauczyciela()
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
            wyswietl_uczniow()
        if opcja_zarzadzaj == 2:
            Nauczyciele.wyswietl_nauczycieli()
        if opcja_zarzadzaj == 3:
            wyswietl_wychowawce()
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
