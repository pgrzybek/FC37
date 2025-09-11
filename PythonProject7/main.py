#Sposoby wyliczania ceny:
#1. Liczby sztuk (cena sztuki x liczba zamówionych sztuk)
#2. Liczby paczek (cena paczki * (liczba zamówionych sztuk / liczba sztuk w paczce zaokrąglona w górę) )
#3. Wycena na podstawie ilości + ustalony dodatkowy % straty na ścinki, ucięte rogi itp.)
from math import floor, ceil

products={
    "products_floor_tiles_white":{"price":120,"size":15},
    "products_floor_tiles_black":{"price":140,"size":20},
    "paint_can":{"price":60},
    "paint_brush":{"price":60},
    "planks":{"price":80,"loss":0.1,"unit":"metry"},
    "concrete":{"price":60,"loss":0.05,"unit":"kilogramy"},
}
products_pieces={"pain_can,","paint_brush"}
products_packs={"products_floor_tiles_white","products_floor_tiles_black"}
products_amount={"planks","concrete"}

def pieces_or_packs_ask():
    print("Podaj liczbe sztuk")
    return int(input())

def amount_ask(unit_name):
    print(f"Podaj ilosc {unit_name} ")
    return floor(int(input()))

def price_piece(price,quantity):
    return price*quantity

def price_packs(price,quantity,size):
    return price*ceil(quantity/size)

def price_amount(price,quantity,loss):
    return price*quantity*(1+loss)

def piece_print(quantity):
    print(f"Zamowiono {quantity}")

def packs_print(quantity,size):
    packs= int(ceil(quantity / size))
    print(f"Zamowiono {packs}")

def amount_print(quantity,loss):
    print(f"Zamowiono {quantity} o dodaktowej stracie {loss}")


total_price=0

while True:
    print("Podaj nazwe producktu")
    current_product = int(input())
    if not current_product:
        break
    if current_product not in current_product:
        continue
    if current_product in products_pieces or current_product in products_packs:
        quantity = pieces_or_packs_ask()
    if current_product in products_amount:
        quantity = amount_ask(current_product)
    
