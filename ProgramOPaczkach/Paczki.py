iloscPrzedmiotow=input("Podaj ilosc przedmiotow")
wagaPrzedmiotu=[]

for i in iloscPrzedmiotow:
    waga=int(input("Podaj waga przedmiotu {} ") .format(i))
    if waga<=10 or waga>=1 :
        wagaPrzedmiotu.append(waga)
    else:
        print("zla waga")
        break
wagaPaczki=[]
waga=0
while waga <20:
    if waga.bit_length()>0:
        print()


