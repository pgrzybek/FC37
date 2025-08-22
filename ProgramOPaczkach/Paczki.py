iloscPrzedmiotow=input("Podaj ilosc przedmiotow \n")
wagaPrzedmiotu=[]

for i in range(0,int(iloscPrzedmiotow)):
    waga=int(input("Podaj waga przedmiotu {} ".format(i)))
    if waga<=10 or waga>=1 :
        wagaPrzedmiotu.append(waga)
    else:
        print("zla waga")
        break

wagaPaczki=0
i=0
j=0
paczka=[]
licznikPaczek=0
wszytkiePaczki=[]
iloscDoSpakowania=len(wagaPrzedmiotu)
najwiecejkg=0
pusteMiejsce=0
sumaPustych=0
sumaKg=0
paczkaNajciezsza=0
while iloscDoSpakowania>0 :  #Tu sprawdzamy ile zostało do spakowania
    pusteMiejsce = 20  # maksymalna waga paczki
    wagaPaczki=0
    while pusteMiejsce > wagaPrzedmiotu[i]: #Tu robimy paczke
        wagaPaczki=wagaPrzedmiotu[i]+wagaPaczki
        iloscDoSpakowania=iloscDoSpakowania-1
        paczka.append(wagaPrzedmiotu[i])
        pusteMiejsce = pusteMiejsce - wagaPrzedmiotu[i]
        i = i + 1
        if iloscDoSpakowania == 0:
            break

    licznikPaczek = licznikPaczek +1
    wszytkiePaczki.append(paczka)
    paczka=[]# nowa paczka
    sumaPustych=sumaPustych+pusteMiejsce
    sumaKg=sumaKg+wagaPaczki
    if wagaPaczki>najwiecejkg:
        najwiecejkg=wagaPaczki
        paczkaNajciezsza=licznikPaczek


print(f"licznikPaczek {licznikPaczek}")
print(f"Wysłano {wszytkiePaczki}")
print(f"puste miejsce {sumaPustych} kg")
print(f"wysłano {sumaKg} kg")
print(f"najwiecej miala paczka {paczkaNajciezsza}  {najwiecejkg} kg")



