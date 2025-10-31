from Operacje import Operacje
from Przedmioty import Przedmioty
from SprawdzCzyToLiczba import sprawdz_czy_to_liczba

kontoPLik="konto.json"
magazynPlik="magazyn.json"
operacjePlik="operacje.json"

import json

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

    print(operacja)
    return operacja

