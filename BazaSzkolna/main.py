uczniowie = []
nauczyciele = []
wychowawcy = []


class Szkolny:
    def __init__(self, imie_i_nazwisko, klasa):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.klasa = klasa


class Uczen(Szkolny):
    def __init__(self, imie_i_nazwisko, klasa):
        super().__init__(imie_i_nazwisko, klasa)


class Wychowawca(Szkolny):
    def __init__(self, imie_i_nazwisko, klasa):
        super().__init__(imie_i_nazwisko, klasa)


class Nauczyciel(Szkolny):
    def __init__(self, imie_i_nazwisko, klasa, przedmiot):
        self.przedmiot = przedmiot
        super().__init__(imie_i_nazwisko, klasa)


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
    uczniowie.append(Uczen(imie_i_nazwisko, klasa))


def dodaj_nauczyciela():
    print("Dodaj nauczyciela")
    imie_i_nazwisko = input("Podaj imie i nazwisko ze spacja w srodku \n")
    przedmiot = input("Podaj przedmiot \n")
    i = 0
    klasy = []
    while 1:
        klasa=input("Podaj klase w ktorej naucza pusta wartosc konczy wprowadzanie ")
        klasy.append(klasa)
        if klasa == "":
            break
        nauczyciele.append(Nauczyciel(imie_i_nazwisko, klasy, przedmiot))


def dodaj_wychowawce():
    print("Dodaj wychowawce")
    imie_i_nazwisko, klasa = dodaj()
    wychowawcy.append(Wychowawca(imie_i_nazwisko, klasa))


def wyswietl_klasy():
    nazwa_klasy=input("Podaj nazwe klasy ")
    print(f"Uczniowie klasy {nazwa_klasy} to")
    for uczen in uczniowie:
        if nazwa_klasy == uczen.klasa:
            #klasa.add(uczen.imie_i_nazwisko)
            print(uczen.imie_i_nazwisko)
    else:
        print("Nie znaleziono uczniow")
    print("Wychowawca to ")
    for wychowawca in wychowawcy:
        if wychowawca.klasa == nazwa_klasy:
            print(wychowawca.imie_i_nazwisko)
            break
    else:
        print("Nie znaleziono wychowawcy")


def wyswietl_nauczycieli():
    wybrany=input("podaj imiei nazwisko nauczyciela ze spacja w srodku \n")
    print("Ten nauczyciel prowadzi te klasy")
    for nauczyciel in nauczyciele:
        if nauczyciel.imie_i_nazwisko == wybrany:
            for i in range(len(nauczyciel.klasa)):
                print(nauczyciel.klasa[i])
        break
    else:
        print("Nie znaleziono nauczyciela")


def wyswietl_wychowawce():
    imie_wychowawcy=input("Podaj imie i nazwisko wychowawcy ze spacja w srodku \n")
    print("Uczniowie tego wychowawcy to")
    #znaleziony=wychowawcy.imie_i_nazwisko=imie_wychowawcy.rfind(imie_wychowawcy)
    for wychowawca in wychowawcy:
        if wychowawca.imie_i_nazwisko==imie_wychowawcy:
            for i in range(len(uczniowie)):
                if wychowawca.klasa == uczniowie[i].klasa:
                    print(uczniowie[i].imie_i_nazwisko)
            break
        else:
            print("Nie znaleziono wychowawcy")



def wyswietl_uczniow():
    imie_ucznia=input("Podaj imie i nazwisko ucznia ze spacja w srodku \n")
    wybrany=""
    for uczen in uczniowie:
        if imie_ucznia == uczen.imie_i_nazwisko:
            wybrany=uczen
            break
    print("Uczen ma te przedmioty i tych nauczycieli")
    if wybrany != "":
        klasa_ucznia=wybrany.klasa
        for nauczyciel in nauczyciele:
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
            dodaj_ucznia()
        if opcja_utworz == 2:
            dodaj_nauczyciela()
        if opcja_utworz == 3:
            dodaj_wychowawce()
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
            wyswietl_nauczycieli()
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
