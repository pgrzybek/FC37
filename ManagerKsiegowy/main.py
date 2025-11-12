from Manager import Manager


m = Manager()

def saldo():
    print("Saldo")
    print("Co chcesz zrobic?")
    print("1.Wplac")
    print("2.Wyplac")
    opcja = input()
    if opcja == "1":
        wartosc = input("Podaj ile chcesz wplacic ")
        opcja="w"
        m.assign("k", "",wartosc,"",opcja)
    elif opcja == "2":
        opcja="y"
        wartosc = input("Podaj ile chcesz wyplacic ")
        m.assign("k", "", wartosc, "", opcja)

    else:
        print("Zla komenda")
    return m.wartoscKonta


def sprzedarz():
    print("Sprzedarz")
    nazwa = input("Podaj nazwe  produktu: ")
    print(f"W magazynie jest {m.skladMagazynu[nazwa].ilosc} sztuk ile chcesz sprzedac")
    ilosc = input("Podaj ilosc  produktu: ")
    m.sprawdz_czy_to_liczba(ilosc)
    m.assign("s", nazwa, ilosc, "","")

    input("Nacisnij dowolny klawisz")


def zakup():
    print("Zakup")
    nazwa = input("Podaj nazwe zakupionego produktu: ")
    ilosc = input("Podaj ilosc zakupionego produktu: ")
    cena = input("Podaj cena produktu: ")
    m.assign("z", nazwa, ilosc, cena,"")

    input("Nacisnij dowolny klawisz")


def konto():
    print("Konto")
    print(m.wartoscKonta)
    input("Nacisnij dowolny klawisz")


def lista():
    print("Lista")
    print("nazwa", "ilosc", "cena")
    m.execute("lista", "","","")
    input("Nacisnij dowolny klawisz")


def magazyn():
    print("Magazyn")
    przedmiot = input("Podaj nazwe przedmiotu do znalezienia ")
    m.execute("p",przedmiot,"","")

    input("Nacisnij dowolny klawisz")


def przeglad():
    print("Przeglad")
    zakres_start = input(f"Podaj zakres poczatek zakresu od 0")

    zakres_koniec = input(f"Podaj koniec zakresu do {len(m.operacje)}")
    m.execute("p","", zakres_start, zakres_koniec)

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
    opcjaGlowna = m.sprawdz_czy_to_liczba(opcjaGlowna)
    if opcjaGlowna == 1:
        saldo()
    if opcjaGlowna == 2:
        sprzedarz()
    if opcjaGlowna == 3:
        zakup()
    if opcjaGlowna == 4:
        konto()
    if opcjaGlowna == 5:
        lista()
    if opcjaGlowna == 6:
        magazyn()
    if opcjaGlowna == 7:
        przeglad()
    if opcjaGlowna == 8:
        print(m.skladMagazynu, m.wartoscKonta, m.operacje)
        m.assign("e", "", "", "","")
        break
    if 8 < opcjaGlowna < 1:
        print("Zly wobor ")
