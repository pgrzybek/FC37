"shift +f6 refaktoring zmiennej"
firstName=[1,2,3,4,5,6,6,6,7]
print(firstName[-1])#daje koncowa wartosc
print(firstName[-2])#daje przedostatni element

#tuple krotki nie modyfikowalne elementy
sampleTuple= 1,2,3,4,5
print(sampleTuple)
sampleTuple=(1,"Ewa",3,4,True)
list=[1,2,3,4,5,6,6,6,("Ania")]
#szybsza kolekcja
#id sprawdza miejsce w pamieci
#przypisywanie to podwiazanie w pamieci wskazuje na to samo miejsce
#metoda clear czysci pamiec czyli obydwie zmienne
#sety nie pilnuja kolejnosci
#set nie ma duplikatów
#lista jest najwolniejsza
#roznica nawiasow