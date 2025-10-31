from SprawdzCzyToLiczba import sprawdz_czy_to_liczba
from OperacjeNaPliku import odczytajKonto
from OperacjeNaPliku import odczytajMagazyn
from OperacjeNaPliku import odczytajOperacje

class Manager:
    wartoscKonta = None

    def __init__(self):
        self.wartoscKonta = odczytajKonto()
        self.skladMagazynu = odczytajMagazyn()
        self.operacje = odczytajOperacje()

    def execute(self):
        pass

    def assign(self):
        pass


