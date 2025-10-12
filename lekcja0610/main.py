from itertools import count

counter=0
counter2=0
def dodaj(a,b):
  global counter
  counter+=1
  return a+b
def odejmij(a,b):
    global counter
    counter += 1
    return a-b
def pomnoz(a,b):
    global counter2
    counter2 += 1
    return a*b
def podziel(a,b):
    global counter2
    counter2 += 1
    try:
        return a/b
    except ZeroDivisionError:
        print("nie dziel przez 0")

a=2
b=3
print(counter)
print(f"counter2 {counter2}")
dodaj(a,b)
odejmij(a,b)
pomnoz(a,b)
podziel(a,b)
print(counter)
print(f"counter2 {counter2}")

class Calculator:
    def __init__(self, brand, price, serial_number):
        self.brand = brand
        self.price = price
        self.serial_number = serial_number
        self.counter = 0
        self.battery=100


    def sum(self, a, b):
        self.topUpCounter()
        self.drainBattery()
        if self.battery > 0:
            return a + b
        else:
            return 0

    def divide(self, a, b):
        self.topUpCounter()
        self.drainBattery()
        if self.battery > 0:
            try:
                return a / b
            except ZeroDivisionError:
                print("nie dziel przez 0")
        else:
            return 0
    def multiply(self, a, b):
        self.topUpCounter()
        self.drainBattery()
        if self.battery > 0:
            return a * b
        else:
            return 0
    def substract(self, a, b):
        self.topUpCounter()
        self.drainBattery()
        if self.battery > 0:
            return a - b
        else:
            return 0

    def calculate(self, a, b, operation_type):

        operation_type= operation_type.lower().strip()
        operations = {"sum": lambda a, b: a + b,
                      "divide": lambda a, b: a / b if b != 0 else None,
                      "multiply": lambda a, b: a * b,
                      "substract": lambda a, b: a - b}
        function = operations.get(operation_type)
        if function:
            return function(a, b)
        else:
            print("Niema tej operacji")
            return None
        # if operation_type =="sum":
        #     return self.sum(a, b)
        # elif operation_type == "divide":
        #     return self.divide(a, b)
        # elif operation_type == "multiply":
        #     return self.multiply(a, b)
        # elif operation_type == "substract":
        #     return self.substract(a, b)
        # else:
        #      return print("zly wybor")
    def topUpCounter(self):
        self.counter += 1
    def drainBattery(self):
        self.battery -= 1

nowy=Calculator("jakis",567,56789)

print(nowy.counter)
print(nowy.battery)
print(nowy.calculate(10,20,"jsdnasjdnk"))

# nowy.sum(10, 20)
# nowy.divide(10,20)
# nowy.multiply(10,20)
# nowy.substract(10,20)
print(nowy.counter)
print(nowy.battery)
#do aktualnej implementacji klasy Calculator dodaj atrybut battery który na początku jest różny 100 a każda operacja artyemtnyczna wywołana na kalkulatorze zmniejsza poziom baterii o 1



