import json

from ConvertToFile import ConvertToFile


class Przedmioty:
    def __repr__(self):
        return json.dumps(self.__dict__)
    def __init__(self,nazwa,cena,ilosc):
        self.nazwa=nazwa
        self.ilosc = ilosc
        self.cena=cena
    def wypisz(self):
        print(self.nazwa, self.ilosc, self.cena)
        return self.nazwa, self.ilosc, self.cena
    def __str__(self):
        return self.nazwa, self.ilosc, self.cena
    def to_dict(self):
        #return self.__dict__
        return {self.nazwa: self.ilosc, self.cena: self.cena}
    @staticmethod
    #def from_dict(data, cls):
        #return {k: cls(**v) for k, v in data.items()}
    def from_dict(data):
        nazwa=data["nazwa"]
        ilosc=data["ilosc"]
        cena=data["cena"]
        return Przedmioty(nazwa,ilosc,cena)

