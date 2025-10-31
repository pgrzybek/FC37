from Manager import Manager
from OperacjeNaPliku import odczytajKonto, zapiszPrzyKoncu, kontoPLik, odczytajMagazyn,zachowajStanMagazynu,zachowajOperacje,odczytajOperacje
from Przedmioty import Przedmioty
from Operacje import Operacje

from SprawdzCzyToLiczba import sprawdz_czy_to_liczba

#wartoscKonta=1000
#skladMagazynu={}
#operacje={}



def operacje_wykonane(slownik, wartosc):
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

def sprzedarz(zkonto,zmagazyn):
    print("Sprzedarz")
    nazwa = input("Podaj nazwe  produktu: ")
    if  nazwa in zmagazyn:
        print(f"W magazynie jest {zmagazyn[nazwa].ilosc} sztuk ile chcesz sprzedac")
        ilosc = input("Podaj ilosc  produktu: ")
        ilosc=sprawdz_czy_to_liczba(ilosc)
        if ilosc<zmagazyn[nazwa].ilosc:
            zmagazyn[nazwa].ilosc =zmagazyn[nazwa].ilosc-ilosc
            zkonto = zkonto+zmagazyn[nazwa].ilosc*zmagazyn[nazwa].cena
            sprzedany_przedmiot=Operacje("sprzedarz",zmagazyn[nazwa])
            operacje_wykonane(m.operacje, sprzedany_przedmiot)

        elif ilosc==zmagazyn[nazwa].ilosc:
            zkonto = zkonto + zmagazyn[nazwa].ilosc * zmagazyn[nazwa].cena
            sprzedany_przedmiot = Operacje("sprzedarz", zmagazyn[nazwa])
            m.operacje.append(sprzedany_przedmiot)
            #operacje_wykonane(operacje, sprzedany_przedmiot)
            del zmagazyn[nazwa]
        else:
            print("Niewlasciwa ilosc")

    input("Nacisnij dowolny klawisz")
    return zkonto,zmagazyn
def zakup(zkonto, zmagazyn):
    print("Zakup")
    nazwa=input("Podaj nazwe zakupionego produktu: ")
    ilosc=input("Podaj ilosc zakupionego produktu: ")
    cena=input("Podaj cena produktu: ")
    cena=sprawdz_czy_to_liczba(cena)
    ilosc=sprawdz_czy_to_liczba(ilosc)
    koszt =int(cena)*int(ilosc)
    zakupiono = zkonto - koszt
    if zakupiono >= 0:
        produkt = Przedmioty(nazwa, cena, ilosc)
        #productDict=produkt.__dict__
        if not nazwa in zmagazyn:
            zmagazyn[nazwa]=produkt
        else:
            zmagazyn[nazwa].ilosc=zmagazyn[nazwa].ilosc+ilosc
        zkonto=zakupiono
        produkt = Przedmioty(nazwa, cena, ilosc)
        zakupiony_przedmiot = Operacje("zakup", produkt)
        m.operacje.append(zakupiony_przedmiot)
        #operacje_wykonane(operacje, zakupiony_przedmiot)
    else:
        print(f"Za malo pieniedzy na koncie brakuje {abs(zakupiono)} ")

    input("Nacisnij dowolny klawisz")
    return zkonto,zmagazyn
def konto():
    print("Konto")
    print(wartoscKonta)
    input("Nacisnij dowolny klawisz")
def lista():
    print("Lista")
    print("nazwa", "ilosc", "cena")
    for jednostka in skladMagazynu:
        #print(skladMagazynu[jednostka],skladMagazynu[jednostka]["ilosc"],skladMagazynu[jednostka]["cena"])
        skladMagazynu[jednostka].wypisz()
    input("Nacisnij dowolny klawisz")
def magazyn():
    print("Magazyn")
    przedmiot=input("Podaj nazwe przedmiotu do znalezienia ")
    if przedmiot in skladMagazynu:
        skladMagazynu[przedmiot].wypisz()
    else:
        print("Brak przedmiotu")
    input("Nacisnij dowolny klawisz")
def przeglad():
    print("Przeglad")
    zakres_start=input(f"Podaj zakres poczatek zakresu od 0")

    zakres_koniec = input(f"Podaj koniec zakresu do {len(m.operacje)}")

    if zakres_start=="" or zakres_koniec=="":
        for i in range(len(m.operacje)):
            m.operacje[str(i)].wypisz()
    else:
        zakres_start = sprawdz_czy_to_liczba(zakres_start)
        zakres_koniec = sprawdz_czy_to_liczba(zakres_koniec)
        if zakres_start>0 and zakres_koniec<len(m.operacje):
            for i in range(zakres_start,zakres_koniec):
               m.operacje[i].wypisz()
        else:
            print("zly zakres")

    input("Nacisnij dowolny klawisz")


m=Manager()
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
        wartoscKonta=saldo(m.wartoscKonta)
    if opcjaGlowna == 2:
        wartoscKonta,skladMagazynu =sprzedarz(m.wartoscKonta,m.skladMagazynu)
    if opcjaGlowna == 3:
        wartoscKonta,skladMagazynu=zakup(m.wartoscKonta,m.skladMagazynu)
    if opcjaGlowna == 4:
        konto()
    if opcjaGlowna == 5:
        lista()
    if opcjaGlowna == 6:
        magazyn()
    if opcjaGlowna == 7:
        przeglad()
    if opcjaGlowna == 8:
        print(m.skladMagazynu,m.wartoscKonta,m.operacje)
        zapiszPrzyKoncu(m.wartoscKonta,m.skladMagazynu,m.operacje)
        zachowajStanMagazynu(m.skladMagazynu)
        zachowajOperacje(m.operacje)

        break
    if 8< opcjaGlowna < 1:
        print("Zly wobor ")

