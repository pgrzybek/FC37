from datetime import date
#rok= date.year()
rok = 2025
print("Kartka z zyczeniami ")
print("Podaj proszę imie odbiorcy")
odbiorca=input()
print("Podaj jego wiek")
jegoWiek=input()
print("Napisz swoje zyczenie")
wiadomosc=input()
print("Podaj swoje imie")
imie=input()
wiek=rok- int(jegoWiek)
print("Wszystkiego najlepszego {imie} z okazji {wiek}  urodzin /n {wiadomosc} /n {nadawca}")
