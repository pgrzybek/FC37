#print("zadanie 1")
#print("Podaj imie")
#imie = input()
#print("podaj wiek")
#wiek = input()
#print("Cześć mam na imię {} i mam {} lat".format(imie, wiek ))
#print("********************************")
# print("zadanie 2")
# print("Podaj 1 liczbe")
# a=int(input())
# print("Podaj 2 liczbe")
# b=int(input())
# print("Suma to {}".format(a+b))
#ctl+/ komentowanie wielu lini
# dwa razy ctrl i strzalka w dol gore rozmazanie kursowa pisanie wielu lini
print("zadanie3")
print("Podaj 1 liczbe")
a=int(input())
print("Podaj 2 liczbe")
b=int(input())
pole= a*b
obwod=2*a+2*b
print("Pole prostokata to {} a obwod to {} " .format(pole,obwod) )
print(" ")
print("zadanie 4")
reszta= a%b
print("Liczba a dzielona przez b reszta to {} " .format(reszta))
print(" ")
print("zadanie 5")
reszta= a%2

if reszta==0:
    napisz="parzysta"
else:
    napisz="nieparzysta"

print("Liczba {}".format(napisz))

print("Czy liczba {} jest parzysta {}".format(a, a%2 == 0))
print("zadanie 6")
if a>=b: napisz="wieksza"
else: napisz="mniejsza"
if a==b: napisz="rowna"
print(" a jest {} b ".format(napisz))
print("zadanie 7")
print("podaj haslo")
haslo=input()
if haslo=="sekret123":napisz="Uznano dostęp"
else:napisz="blędne haslo"
print("{} ".format(napisz))
print("podaj haslo")
print("")
print("zadanie 8")
# print("Napisz zdanie ")
zdanie = input("Napisz zdanie")
dlugosc=len(zdanie)
duze= zdanie.upper()

print(" zdanie ma {} znakow  ".format(dlugosc))
print("Python" in zdanie)
print("podaj haslo")
if a>1 and a<10:napisz= "jest w przedziale"

