#from Operacje import Operacje
#from itertools import product

from OperacjeNaPliku import  odczytajMagazyn, odczytajOperacje
from KontoEncja import KontoEncja
#from Przedmioty import Przedmioty
from dbInit import db
from Produkt import Produkt
from OperacjeEncja import Operacje


class Magazyn:
    def __init__(self):
        self.saldo = self.odczytajKonto().saldo
        self.skladMagazynu = odczytajMagazyn()
        self.operacje = odczytajOperacje()

    @staticmethod
    def odczytajKonto():
        konto = db.session.get(KontoEncja, 1)

        if konto is None:
            konto = KontoEncja(saldo=1000)
            db.session.add(konto)

        # trzeba zapisać, żeby dostał id

        return konto


    def lista(self):
        #for jednostka in self.skladMagazynu:
            # print(skladMagazynu[jednostka],skladMagazynu[jednostka]["ilosc"],skladMagazynu[jednostka]["cena"])
        return db.session.query(Produkt).all()
        #return "Brak w magazynie"

    def zmienSaldo(self, opcja, iloscPieniedzy):
        """

        :param opcja: w , wplata, y, wyplata
        :param iloscPieniedzy: wartosc do zmiany
        :return:
        """
        konto = self.odczytajKonto()
        saldo = konto.saldo
         # lub konto.saldo += 100
          # zapis do bazy

        if opcja == "w" or opcja == "wplata":
            wartosc = self.sprawdz_czy_to_liczba(iloscPieniedzy)
            saldo = saldo + wartosc
        elif opcja == "y" or opcja == "wyplata":

            wartosc = self.sprawdz_czy_to_liczba(iloscPieniedzy)
            saldo = saldo - wartosc
        else:
            print("Zla komenda")
        konto.saldo = saldo
        db.session.commit()
        #zapiszKonto(konto)
        return konto

    def przeglad(self, zakres_start, zakres_koniec):

        if zakres_start == "" or zakres_koniec == "":
            operacje = db.session.query(Operacje).all()
            return operacje
        else:
            zakres_start = self.sprawdz_czy_to_liczba(zakres_start)
            zakres_koniec = self.sprawdz_czy_to_liczba(zakres_koniec)
            operacje = Operacje.query.filter(
                Operacje.id.between(zakres_start, zakres_koniec)
            ).all()

            return operacje

        #     for i in range(len(self.operacje)):
        #         self.operacje[str(i)].wypisz()
        #     return None
        # else:
        #     zakres_start = self.sprawdz_czy_to_liczba(zakres_start)
        #     zakres_koniec = self.sprawdz_czy_to_liczba(zakres_koniec)
        #     operacje = {}
        #     if zakres_start >= 0 and zakres_koniec <= len(self.operacje)-1:
        #         for i in range(zakres_start, zakres_koniec+1):
        #             i=str(i)
        #             operacje[i]= self.operacje[i]
        #         return operacje
        #     else:
        #         print("zly zakres")
        #
        #return operacje

    def zakup(self,nazwa,ilosc,cena):
        try:
            cena= int(cena)
        except ValueError:
            return "To nie liczba"
        # ilosc = self.sprawdz_czy_to_liczba(ilosc)
        konto = self.odczytajKonto()
        saldo = konto.saldo
        try:
            ilosc=int(ilosc)
        except ValueError:
            return "To nie liczba"
        koszt = int(cena) * int(ilosc)
        zakupiono = saldo - koszt

        produkt = (db.session.query(Produkt)
                   .filter_by(nazwa=nazwa)
                   .first())
        if zakupiono >= 0:
            if not produkt:
                produkt = Produkt(nazwa=nazwa, cena=cena, ilosc=ilosc)
                db.session.add(produkt)
                db.session.commit()
            else:
                produkt.ilosc=produkt.ilosc + ilosc
            przedmiot=produkt
            db.session.add(przedmiot)
            operacja=Operacje(typ="kupno",produkt=produkt)
            db.session.add(operacja)
            db.session.commit()
            return produkt
        else:
            return produkt

    def sprzedarz(self,nazwa,ilosc):
        konto = self.odczytajKonto()
        saldo = konto.saldo
        try:
            ilosc = int(ilosc)
        except ValueError:
            return "To nie liczba"

        produkt = (db.session.query(Produkt)
                   .filter_by(nazwa=nazwa)
                   .first())
        if produkt:
            if ilosc < produkt.ilosc:
                produkt.ilosc = produkt.ilosc -ilosc
                saldo = saldo + produkt.ilosc * produkt.cena
                konto.saldo = saldo
                operacja = Operacje(typ="sprzedarz",produkt=produkt)
                db.session.add(operacja)
                db.session.commit()
            elif ilosc == produkt.ilosc :

                saldo = saldo + produkt.ilosc * produkt.cena
                konto.saldo = saldo

                db.session.delete(produkt)
                db.session.commit()
            return produkt
        else:
            return None



    # def sprzedarz(self, nazwa, ilosc):
    #     konto = self.odczytajKonto()
    #     saldo = konto.saldo
    #     try :
    #         ilosc =int(ilosc)
    #     except ValueError:
    #         return "To nie liczba"
    #     if nazwa in self.skladMagazynu:
    #         if ilosc < self.skladMagazynu[nazwa].ilosc:
    #             self.skladMagazynu[nazwa].ilosc = self.skladMagazynu[nazwa].ilosc - ilosc
    #             saldo = saldo + self.skladMagazynu[nazwa].ilosc * self.skladMagazynu[nazwa].cena
    #             sprzedany_przedmiot = Operacje("sprzedarz", self.skladMagazynu[nazwa])
    #             self.operacje_wykonane(self.operacje, sprzedany_przedmiot)
    #             konto.saldo=saldo
    #             db.session.commit()
    #         elif ilosc == self.skladMagazynu[nazwa].ilosc:
    #             saldo = saldo + self.skladMagazynu[nazwa].ilosc * self.skladMagazynu[nazwa].cena
    #             sprzedany_przedmiot = Operacje("sprzedarz", self.skladMagazynu[nazwa])
    #             self.operacje.append(sprzedany_przedmiot)
    #             # operacje_wykonane(operacje, sprzedany_przedmiot)
    #             del self.skladMagazynu[nazwa]
    #             konto.saldo = saldo
    #             db.session.commit()
    #         else:
    #             print("Niewlasciwa ilosc")
    #             return None
    #     return "success"

    def magazyn_rzeczy(self,wybor):
        return db.session.query(Produkt).filter_by(nazwa=wybor).first()
        # if przedmiot in self.skladMagazynu:
        #     self.skladMagazynu[przedmiot].wypisz()
        # else:
        #     print("Brak przedmiotu")
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


