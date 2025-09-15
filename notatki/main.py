a = [1, 2, 3]
#b = [x for x in a]
f = a[:]
print(id(a))
print(id(f))

import copy

a = [[1, 2], [3, 4]]

# 1. Tylko referencja (ta sama lista)
b = a

# 2. Płytka kopia
c = a.copy()

# 3. Głęboka kopia
d = copy.deepcopy(a)

print("id(a):", id(a))
print("id(b):", id(b))
print("id(c):", id(c))
print("id(d):", id(d))

print("\nPorównania:")
print("a is b:", a is b)   # True – ta sama lista
print("a is c:", a is c)   # False – nowa lista, ale elementy te same
print("a is d:", a is d)   # False – zupełnie nowa lista

print("a == b:", a == b)   # True – zawartość taka sama
print("a == c:", a == c)   # True – zawartość taka sama
print("a == d:", a == d)   # True – zawartość taka sama

# Test zmian
b[0][0] = 99
print("\nPo zmianie b[0][0] = 99:")
print("a:", a)  # zmienia się, bo b = a
print("c:", c)  # zmienia się też, bo to płytka kopia (dzielą te same podlisty)
print("d:", d)  # nie zmienia się, bo deepcopy
#@dataclass(frozen=True) nie mutowalna klas