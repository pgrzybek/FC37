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
wyrazCiagu=[]
i=0
wyrazCiagu.append(liczbaStartowa)
while wyrazCiagu[i] !=1.0:
    parzysta = wyrazCiagu[i]%2
    if parzysta == 0:
        wyrazCiagu.append(wyrazCiagu[i]/2)
    else:
        wyrazCiagu.append(3*wyrazCiagu[i]+1)
    print(wyrazCiagu[i])
    i=i+1
print(wyrazCiagu[i])
