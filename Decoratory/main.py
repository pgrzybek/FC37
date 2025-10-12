# type numeric = int | float
# def sum2(a: numeric, b: numeric) -> numeric:
#     return a + b
# print(sum2(2, 3))
from datetime import datetime
print(datetime.now().hour)
def not_during_night(func):

    def wrapper():
        if 6<datetime.now().hour < 16:
            func()
        else:
            print("wszyscy spia")
    return wrapper
@not_during_night
def funkcja1():
    print("Hello World")
@not_during_night
def funkcja2():
    print("Jestem")

funkcja1()
funkcja2()