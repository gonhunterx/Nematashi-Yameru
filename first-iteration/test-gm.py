class Item:
    def __init__(self, id, name, value, damage):
        self.id = id
        self.name = name
        self.value = value
        self.damage = damage

    def __str__(self) -> str:
        return f"{self.id}: {self.name}, {self.value}, {self.damage}"


golden_axe = Item(1, "golden axe", 300, 25)

print(golden_axe.__str__())

weapons = list()

weapons.append(golden_axe)

print(f"DAMAGE: {golden_axe.damage}")

for item in weapons:
    print(f"- {item.__str__()}")
