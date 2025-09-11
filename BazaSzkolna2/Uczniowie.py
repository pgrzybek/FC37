from Nauczyciele import Nauczyciele
from Szkolny import Szkolny

class Uczniowie(Szkolny):
    def __init__(self, imie_i_nazwisko, klasa):
        super().__init__(imie_i_nazwisko, klasa)
    # def __init__(self, dane):
    #     super().__init__(dane)

    @classmethod
    def wyswietl_uczniow(cls):
        imie_ucznia = input("Podaj imie i nazwisko ucznia ze spacja w srodku \n")
        wybrany = ""
        for uczen in Uczniowie.lista:
            if imie_ucznia == uczen.imie_i_nazwisko:
                wybrany = uczen
                break
        #wybrany=Uczniowie.lista[imie_ucznia]
        print("Uczen ma te przedmioty i tych nauczycieli")
        if wybrany != "":
            klasa_ucznia = wybrany.klasa
            for nauczyciel in Nauczyciele.lista:
                for i in range(len(nauczyciel.klasa)):
                    if nauczyciel.klasa[i] == klasa_ucznia:
                        print(nauczyciel.imie_i_nazwisko)
                        print(nauczyciel.przedmiot)
            else:
                print("nie znaleziono ucznia")