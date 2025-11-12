from ConvertToFile import ConvertToFile
from Przedmioty import Przedmioty

class Operacje(ConvertToFile):
    # def __repr__(self):
    #     return {self.operacja,self.przedmiot.to_dict()}

    def __init__(self,operacja,przedmiot):
        self.operacja = operacja
        self.przedmiot=przedmiot
    def __str__(self):
        return self.operacja, self.przedmiot.nazwa, self.przedmiot.cena, self.przedmiot.ilosc
    def wypisz(self):
        print(self.operacja,self.przedmiot.nazwa,self.przedmiot.cena,self.przedmiot.ilosc)
        return self.operacja,self.przedmiot.nazwa,self.przedmiot.cena,self.przedmiot.ilosc
    def to_dict(self):
        return {"operacja":self.operacja,"przedmiot":self.przedmiot.to_dict()}

    @staticmethod
    def from_dict(data):
        operacja=data["operacja"]
        przedmiot=Przedmioty.from_dict(data["przedmiot"])
        return Operacje(operacja,przedmiot)


