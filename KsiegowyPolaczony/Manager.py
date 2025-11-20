from Magazyn import Magazyn
from OperacjeNaPliku import  zapiszKonto, zachowajStanMagazynu, zachowajOperacje
from dbInit import db


class Manager(Magazyn):

    def assign(self, typ, nazwa, ilosc, cena,wplataLubWyplata):
        """
        Przypisywanie wyoluje saldo zakup lub sprzedarz
        :param wplataLubWyplata:
        :param cena: cena przedmiotu do zakupu lub sprzedarzy sluzy tez do wplaty lub wyplaty
        :param ilosc: ilosc przedmiotu do zakupu lub sprzedarzy
        :param nazwa:

        :param typ: Typ operacji parametry to s z k .s,e to sprzedarz ,z to zakup ,k to konto.Działa na pełnych nazwach lub literach , e to end czyli koniec
        :return:
        """
        if typ == "e" or typ == "koniec":
            zapiszKonto(self.saldo)
            zachowajStanMagazynu(self.skladMagazynu)
            zachowajOperacje(self.operacje)
        if typ == 'konto' or typ == 'k':
            self.zmienSaldo(wplataLubWyplata, ilosc)
        if typ == "zakup" or typ == "z":
            self.zakup(nazwa, ilosc, cena)
        if typ == "sprzedarz" or typ == "s":
            self.sprzedarz(nazwa, ilosc)

    def execute(self,typ,wybor,zakres_start,zakres_end):
        """

        :param typ: "k" lub konto,"m lub magazyn, "p" lub przeglad
        :param wybor: parametr do magazyn
        :param zakres_start: parametr do przeglad
        :param zakres_end: parametr do przeglad
        :return:
        """
        if typ == "k" or typ=="konto":
            return self.odczytajKonto()
        if typ=="m" or typ=="magazyn":
            return self.magazyn_rzeczy(wybor)

        if typ == "l" or typ=="lista":
             return self.lista()
        if typ == "p" or typ=="przeglad":
              return self.przeglad(zakres_start,zakres_end)
        return None


