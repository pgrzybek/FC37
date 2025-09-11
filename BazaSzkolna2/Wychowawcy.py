from Szkolny import Szkolny
from Uczniowie import Uczniowie


class Wychowawcy(Szkolny):
    def __init__(self, imie_i_nazwisko, klasa):
        super().__init__(imie_i_nazwisko, klasa)

    @staticmethod
    def wyswietl_wychowawce():
        imie_wychowawcy = input("Podaj imie i nazwisko wychowawcy ze spacja w srodku \n")
        print("Uczniowie tego wychowawcy to")
        # znaleziony=wychowawcy.imie_i_nazwisko=imie_wychowawcy.rfind(imie_wychowawcy)
        for wychowawca in Wychowawcy.lista:
            if wychowawca.imie_i_nazwisko == imie_wychowawcy:
                for i in range(len(Uczniowie.lista)):
                    if wychowawca.klasa == Uczniowie.lista[i].klasa:
                        print(Uczniowie.lista[i].imie_i_nazwisko)
                break
            else:
                print("Nie znaleziono wychowawcy")
