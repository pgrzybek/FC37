class Szkolny:
    lista=[]
    def __init__(self, imie_i_nazwisko, klasa):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.klasa = klasa

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # tworzymy niezależną kopię value dla klasy potomnej
        cls.lista = cls.lista

    @classmethod
    def dodaj(cls):
        print(f"{cls.__name__}")
        imie_i_nazwisko = input("Podaj imie i nazwisko ze spacja w srodku \n")
        klasa = input("Podaj klase \n")
        cls.lista.append(cls(imie_i_nazwisko, klasa))
