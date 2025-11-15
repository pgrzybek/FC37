from Operacje import Operacje
from OperacjeNaPliku import odczytajKonto, odczytajMagazyn, odczytajOperacje, zapiszKonto

from Przedmioty import Przedmioty

class Magazyn:
    def __init__(self):
        self.wartoscKonta = odczytajKonto()
        self.skladMagazynu = odczytajMagazyn()
        self.operacje = odczytajOperacje()

    def lista(self):
        #for jednostka in self.skladMagazynu:
            # print(skladMagazynu[jednostka],skladMagazynu[jednostka]["ilosc"],skladMagazynu[jednostka]["cena"])
        return self.skladMagazynu
        #return "Brak w magazynie"

    def saldo(self, opcja, iloscPieniedzy):
        """

        :param opcja: w , wplata, y, wyplata
        :param iloscPieniedzy: wartosc do zmiany
        :return:
        """
        if opcja == "w" or opcja == "wplata":
            wartosc = self.sprawdz_czy_to_liczba(iloscPieniedzy)
            self.wartoscKonta = self.wartoscKonta + wartosc
        elif opcja == "y" or opcja == "wyplata":

            wartosc = self.sprawdz_czy_to_liczba(iloscPieniedzy)
            self.wartoscKonta = self.wartoscKonta - wartosc
        else:
            print("Zla komenda")
        zapiszKonto(self.wartoscKonta)
        return self.wartoscKonta

    def przeglad(self, zakres_start, zakres_koniec):
        if zakres_start == "" or zakres_koniec == "":
            for i in range(len(self.operacje)):
                self.operacje[str(i)].wypisz()
            return None
        else:
            zakres_start = self.sprawdz_czy_to_liczba(zakres_start)
            zakres_koniec = self.sprawdz_czy_to_liczba(zakres_koniec)
            operacje = {}
            if zakres_start >= 0 and zakres_koniec <= len(self.operacje)-1:
                for i in range(zakres_start, zakres_koniec+1):
                    i=str(i)
                    operacje[i]= self.operacje[i]
                return operacje
            else:
                print("zly zakres")

                return operacje

    def zakup(self, nazwa, ilosc, cena):
        #cena = self.sprawdz_czy_to_liczba(cena)
        try:
            cena= int(cena)
        except ValueError:
            return "To nie liczba"
        # ilosc = self.sprawdz_czy_to_liczba(ilosc)
        try:
            ilosc=int(ilosc)
        except ValueError:
            return "To nie liczba"
        koszt = int(cena) * int(ilosc)
        zakupiono = self.wartoscKonta - koszt
        if zakupiono >= 0:
            produkt = Przedmioty(nazwa, cena, ilosc)
            # productDict=produkt.__dict__
            if not nazwa in self.skladMagazynu:
                self.skladMagazynu[nazwa] = produkt
            else:
                self.skladMagazynu[nazwa].ilosc = self.skladMagazynu[nazwa].ilosc + ilosc
            self.wartoscKonta = zakupiono
            produkt = Przedmioty(nazwa, cena, ilosc)
            zakupiony_przedmiot = Operacje("zakup", produkt)
            self.operacje.append(zakupiony_przedmiot)
            return "Success"
            # operacje_wykonane(operacje, zakupiony_przedmiot)
        else:
            print(f"Za malo pieniedzy na koncie brakuje {abs(zakupiono)} ")
            return f"Za malo pieniedzy na koncie brakuje {abs(zakupiono)} "

    def sprzedarz(self, nazwa, ilosc):
        try :
            ilosc =int(ilosc)
        except ValueError:
            return "To nie liczba"
        if nazwa in self.skladMagazynu:
            if ilosc < self.skladMagazynu[nazwa].ilosc:
                self.skladMagazynu[nazwa].ilosc = self.skladMagazynu[nazwa].ilosc - ilosc
                self.wartoscKonta = self.wartoscKonta + self.skladMagazynu[nazwa].ilosc * self.skladMagazynu[nazwa].cena
                sprzedany_przedmiot = Operacje("sprzedarz", self.skladMagazynu[nazwa])
                self.operacje_wykonane(self.operacje, sprzedany_przedmiot)

            elif ilosc == self.skladMagazynu[nazwa].ilosc:
                self.wartoscKonta = self.wartoscKonta + self.skladMagazynu[nazwa].ilosc * self.skladMagazynu[nazwa].cena
                sprzedany_przedmiot = Operacje("sprzedarz", self.skladMagazynu[nazwa])
                self.operacje.append(sprzedany_przedmiot)
                # operacje_wykonane(operacje, sprzedany_przedmiot)
                del self.skladMagazynu[nazwa]
            else:
                print("Niewlasciwa ilosc")
                return "Niewlasciwa ilosc"
        return "success"

    def magazyn_rzeczy(self,przedmiot):
        if przedmiot in self.skladMagazynu:
            self.skladMagazynu[przedmiot].wypisz()
        else:
            print("Brak przedmiotu")
    @staticmethod
    def operacje_wykonane(slownik, wartosc):
        if slownik:  # jeśli słownik nie jest pusty
            keys_as_ints = [int(k) for k in slownik.keys()]
            nowy_klucz = max(keys_as_ints) + 1
        else:  # jeśli pusty, zaczynamy od 0
            nowy_klucz = "0"
        slownik[nowy_klucz] = wartosc
        return slownik

    @staticmethod
    def sprawdz_czy_to_liczba(wartosc):
        try:
            wartosc = int(wartosc)
            return wartosc
            # this will raise a ValueError
        except ValueError:
            print("To nie jest liczba")
            return 0


