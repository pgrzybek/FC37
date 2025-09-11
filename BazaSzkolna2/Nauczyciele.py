from Szkolny import Szkolny


class Nauczyciele(Szkolny):
    nauczyciele = []
    def __init__(self, imie_i_nazwisko, klasa, przedmiot):
        self.przedmiot = przedmiot
        super().__init__(imie_i_nazwisko, klasa)


    @staticmethod
    def wyswietl_nauczycieli():
        wybrany = input("podaj imiei nazwisko nauczyciela ze spacja w srodku \n")
        print("Ten nauczyciel prowadzi te klasy")
        for nauczyciel in Nauczyciele.lista:
            if nauczyciel.imie_i_nazwisko == wybrany:
                for i in range(len(nauczyciel.klasa)):
                    print(nauczyciel.klasa[i])
            break
        else:
            print("Nie znaleziono nauczyciela")


    def dodaj(cls):
        #print("Dodaj nauczyciela")
        imie_i_nazwisko = input("Podaj imie i nazwisko ze spacja w srodku \n")
        przedmiot = input("Podaj przedmiot \n")
        i = 0
        klasy = []
        while 1:
            klasa = input("Podaj klase w ktorej naucza pusta wartosc konczy wprowadzanie ")
            klasy.append(klasa)
            if klasa == "":
                break
        Nauczyciele.lista.append(Nauczyciele(imie_i_nazwisko, klasy, przedmiot))

    @staticmethod
    def dodaj_nauczyciela():
        print("Dodaj nauczyciela")
        imie_i_nazwisko = input("Podaj imie i nazwisko ze spacja w srodku \n")
        przedmiot = input("Podaj przedmiot \n")
        i = 0
        klasy = []
        while 1:
            klasa = input("Podaj klase w ktorej naucza pusta wartosc konczy wprowadzanie ")
            klasy.append(klasa)
            if klasa == "":
                break
        Nauczyciele.lista.append(Nauczyciele(imie_i_nazwisko, klasy, przedmiot))