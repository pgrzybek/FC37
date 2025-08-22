liczbaStartowa = input("Podaj liczbe od 1 do 100 \n")
while 1:
    try:
        liczbaStartowa = int(liczbaStartowa)
        break
        # this will raise a ValueError
    except ValueError:
        print("To nie jest liczba")
        liczbaStartowa = input("Podaj liczbe od 1 do 100 \n")

while 1:
    if liczbaStartowa < 1 or  liczbaStartowa > 100:
        liczbaStartowa = input("To nie jest liczba od 1 do 100 podaj nowa \n")
        while 1:
            try:
                liczbaStartowa = int(liczbaStartowa)
                break
            except ValueError:
                liczbaStartowa = input("To nie jest liczba podaj nowa \n")
    else:
        print("ok")
        break
#koniec kontroli bledow
