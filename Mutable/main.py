from dataclasses import dataclass

# === Mutowalny obiekt ===

class PlayerMutable:
    def __init__(self, name, score):
        self.name = name
        self.score = score

# === Niemutowalny obiekt ===
@dataclass(frozen=True)
class PlayerImmutable:
    name: str
    score: int

# Lista mutowalnych obiektów
mutable_players = [PlayerMutable("Ala", 10), PlayerMutable("Ola", 20)]
# Lista niemutowalnych obiektów
immutable_players = [PlayerImmutable("Ala", 10), PlayerImmutable("Ola", 20)]

# Kopie
mutable_copy = mutable_players.copy()
immutable_copy = immutable_players.copy()

# === Eksperyment ===
print("=== Przed zmianą ===")
print([p.score for p in mutable_players])    # [10, 20]
print([p.score for p in mutable_copy])       # [10, 20]

# Modyfikacja mutowalnego obiektu w kopii
mutable_copy[0].score += 5

print("\n=== Po zmianie mutowalnej kopii ===")
print([p.score for p in mutable_players])    # [15, 20] – zmiana widoczna w oryginale!
print([p.score for p in mutable_copy])       # [15, 20]

# Modyfikacja niemutowalnej kopii (spróbujmy)
try:
    immutable_copy[0].score += 5
except Exception as e:
    print("\nPróba zmiany niemutowalnego obiektu:")
    print(e)
