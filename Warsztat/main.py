from Exceptions import Wyjatek


def checkAdult(age):
    if age >= 18:
        raise Wyjatek("Uzytkownik maz za malo lat")
    else:
        print("ok")



try:
    checkAdult(20)
except Wyjatek as e:
    print(e)


try:
    checkAdult(15)
except Wyjatek as e:
    print(e)
