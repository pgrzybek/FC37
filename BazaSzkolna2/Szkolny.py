class Szkolny:
    lista=[]
    def __init__(self,*args):
        if len(args) == 1:
            self.dane = args[0]
        elif len(args) == 2:
            self.imie_i_nazwisko = args[0]
            self.klasa = args[1]
        else:
            raise ValueError("Nieprawidłowa liczba argumentów")


    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # tworzymy niezależną kopię value dla klasy potomnej
        cls.lista = cls.lista

    @classmethod
    def dodaj(cls,*args):
        print(f"{cls.__name__}")
        imie_i_nazwisko = input("Podaj imie i nazwisko ze spacja w srodku \n")
        klasa = input("Podaj klase \n")
        if len(args) == 2:
            cls.lista.append(cls(imie_i_nazwisko, klasa))
        elif len(args) == 1:
            dane= {imie_i_nazwisko: klasa}
            cls.lista.append(cls(dane))
        #cls.lista.append(cls(imie_i_nazwisko, klasa))
        #cls.__przypisz(imie_i_nazwisko, klasa)



