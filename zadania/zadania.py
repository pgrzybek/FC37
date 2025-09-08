import random

#zadanie 1
# liczba= int(input("Podaj liczba: "))
# if liczba%2:
#     print("Liczba nieparzysta")
# else:
#     print("Liczba parzysta")
# #zadanie2
# liczba= int(input("Podaj liczbe: "))
# liczba2= int(input("Podaj liczbe2: "))
# liczba3= int(input("Podaj liczbe3: "))
#
# lista=[liczba,liczba2,liczba3]
# print(lista)
# najwieksza=0
# i=0
# for liczba in lista:
#     if liczba >najwieksza:
#         najwieksza=liczba
# print(najwieksza)
#zadanie3

from doctest import master

# liczba= int(input("Podaj liczbe: "))
# if liczba<13:
#     print("jestes dzieckiem ")
# if 13 <= liczba < 20:
#     print("jestes nastolatkiem  ")
# if liczba>20:
#     print("jestes dorosly ")
# #zadanie 4
# start=0
# nastepna=0
# while nastepna<liczba:
#     nastepna=nastepna+1
#     start=start+nastepna
# print(start)
# #zadanie 5
# nastepna=0
# while nastepna<10:
#     nastepna=nastepna+1
#     print(f"{liczba}*{nastepna}={liczba*nastepna} ")
#
# #zadanie 6
# print(random.randint(1,10))
# doZgadniecia=random.randint(1,10)
# while 1:
#     liczba=int(input("zgadnij lizbe od 0 do 10"))
#     if liczba==doZgadniecia:
#         break
# #zadanie 9
# slowo="cos"
# print("" .join(reversed(slowo)))

#zadanie lista1
lista = ["chleb", "mleko", "masło", "jajka"]
lista.append("ser")
lista.remove("masło")
print(lista)
#zadanie lista2
lista = ["chleb", "mleko", "masło", "jajka" ,"mleko"]
lista=set(lista)
print(lista)
#zadanie 3
tupel=(52.2297, 21.0122)

print(f" latitude {tupel[0]} longitude {tupel[1]}")