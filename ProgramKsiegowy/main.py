wartoscKonta=0
skladMagazynu={}
def sprawdz_czy_to_liczba(wartosc):
    while 1:
        try:
            wartosc = int(wartosc)
            break
            # this will raise a ValueError
        except ValueError:
            print("To nie jest liczba")
            wartosc = input("Podaj liczbe \n")
    return wartosc

class Przedmioty:
    def __init__(self,nazwa,cena,ilosc):
        self.nazwa=nazwa
        self.cena=cena
        self.ilosc=ilosc

def dodaj_do_magazynu(slownik, wartosc):
    if slownik:  # jeśli słownik nie jest pusty
        nowy_klucz = max(slownik.keys()) + 1
    else:  # jeśli pusty, zaczynamy od 0
        nowy_klucz = 0
    slownik[nowy_klucz] = wartosc
    return slownik

def saldo(kwota_pieniedzy):
    print("Saldo")
    print("Co chcesz zrobic?")
    print("1.Wplac")
    print("2.Wyplac")
    opcja=input()
    if opcja=="1":
        wartosc=input("Podaj ile chcesz wplacic ")
        wartosc=sprawdz_czy_to_liczba(wartosc)
        kwota_pieniedzy=kwota_pieniedzy+wartosc
    elif opcja=="2":
        wartosc=input("Podaj ile chcesz wyplacic ")
        wartosc=sprawdz_czy_to_liczba(wartosc)
        kwota_pieniedzy=kwota_pieniedzy-wartosc
    else:
        print("Zla komenda")
    return kwota_pieniedzy
def sprzedarz():
    print("Sprzedarz")
    input("Nacisnij dowolny klawisz")
def zakup(zkonto, zmagazyn):
    print("Zakup")
    nazwa=input("Podaj nazwe zakupionego produktu: ")
    ilosc=input("Podaj ilosc zakupionego produktu: ")
    cena=input("Podaj cena produktu: ")
    cena=sprawdz_czy_to_liczba(cena)
    ilosc=sprawdz_czy_to_liczba(ilosc)
    koszt =int(cena)*int(ilosc)
    zakupiono = zkonto - koszt
    if zakupiono > 0:
        produkt=Przedmioty(nazwa,cena,ilosc)
        zmagazyn=(skladMagazynu, produkt)
        zkonto=zakupiono
    else:
        print(f"Za malo pieniedzy na koncie brakuje {abs(zakupiono)} ")

    input("Nacisnij dowolny klawisz")
    return zkonto,zmagazyn
def konto():
    print("Konto")
    input("Nacisnij dowolny klawisz")
def lista():
    print("Lista")
    input("Nacisnij dowolny klawisz")
def magazyn():
    print("Magazyn")
    input("Nacisnij dowolny klawisz")
def przeglad():
    print("Przeglad")
    input("Nacisnij dowolny klawisz")

while 1:
    print("1.Saldo")
    print("2.Sprzedarz")
    print("3.Zakup")
    print("4.Konto")
    print("5.Lista")
    print("6.Magazyn")
    print("7.Przeglad")
    print("8.Koniec")
    opcjaGlowna = input("Wybierz opcje używając numerow 1-8. 8 Konczy program \n")
    opcjaGlowna= sprawdz_czy_to_liczba(opcjaGlowna)
    if opcjaGlowna == 1:
        wartoscKonta=saldo(wartoscKonta)
    if opcjaGlowna == 2:
        sprzedarz()
    if opcjaGlowna == 3:
        wartoscKonta,skladMagazynu=(wartoscKonta,skladMagazynu)
    if opcjaGlowna == 4:
        konto()
    if opcjaGlowna == 5:
        lista()
    if opcjaGlowna == 6:
        magazyn()
    if opcjaGlowna == 7:
        przeglad()
    if opcjaGlowna == 8:
        break
    if 8< opcjaGlowna < 1:
        print("Zly wobor ")

