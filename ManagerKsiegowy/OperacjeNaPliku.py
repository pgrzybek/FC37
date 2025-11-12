from Operacje import Operacje
from Przedmioty import Przedmioty
import json


kontoPLik="konto.json"
magazynPlik="magazyn.json"
operacjePlik="operacje.json"

def sprawdz_czy_to_liczba(wartosc):
    while 1:
        try:
            wartosc = int(wartosc)
            break
            # this will raise a ValueError
        except ValueError:
            print("To nie jest liczba")
            wartosc = input("Podaj liczbe \n")
    return wartosc

def zapiszPrzyKoncu(KontoDoZapisu,magazyn,operacja):

    with open(kontoPLik,'w') as f:

        json.dump(KontoDoZapisu,f)


def odczytajKonto():
    with open(kontoPLik,'r') as f:
        kontoOdczytane=f.read()

        kontoOdczytane=sprawdz_czy_to_liczba(kontoOdczytane)

    return kontoOdczytane

def zachowajStanMagazynu(magazyn):
    with open(magazynPlik, 'w') as f:
        magazyn={k: v.to_dict() for k, v in magazyn.items()}
        json.dump(magazyn, f)

def zachowajOperacje(operacja):
    with open(operacjePlik, 'w') as f:
        operacja = {k: v.to_dict() for k, v in operacja.items()}

        json.dump(operacja, f)

def odczytajMagazyn():
    with open(magazynPlik, newline="") as f:
        magazynOdczytane=json.loads(f.read())
        for key, value in magazynOdczytane.items():
            magazynOdczytane[key]=Przedmioty.from_dict(magazynOdczytane[key])
    return magazynOdczytane

def odczytajOperacje():
    with open(operacjePlik, newline="") as f:
        operacja={}
        d=json.loads(f.read())
        for key, value in d.items():
           operacja[key] = Operacje.from_dict(value)

            #first_key = next(iter(d))
            #first_value = d[first_key]
        #print(value)
        #operacjeOdczytane[second_key]=from_dict(Przedmioty)
        #operacjeOdczytane=from_dict(operacjeOdczytane,Operacje)
    print(operacja)
    return operacja

# def from_dict(data, cls):
#     converted = {}
#     for k, v in data.items():
#         if isinstance(v, dict):
#             converted[k] = cls(**v)  # jeśli dict → tworz obiekt
#         else:
#             converted[k] = v         # jeśli nie dict → zostaw wartość
#     return cls(**converted)
# def from_dict(data, cls):
#     return {k: cls(**v) for k, v in data.items()}
