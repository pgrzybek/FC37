import json
class ConvertToFile:
    def to_dict(self):
        #data = {"nazwa": self.nazwa, "ilosc": self.ilosc, "cena": self.cena, }
        return self.__dict__
        #return data

    def to_json(self):
        #data = {"nazwa": self.nazwa, "ilosc": self.ilosc, "cena": self.cena}
        return json.dumps(self.to_dict())
        #return json.dumps(data)