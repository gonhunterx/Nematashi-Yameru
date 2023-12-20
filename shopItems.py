class Item:
    def __init__(self, name, value, damage):
        self.name = name
        self.value = value
        self.damage = damage

    def __str__(self) -> str:
        return f"{self.name}, {self.value}, {self.damage}"

    def lower(self):
        return self.name.lower()


shop_items2 = {
    "Weapons": {
        Item("Dagger", 240, 10),
        Item("Battle Axe", 400, 20),
        Item("Fire Sword", 850, 44),
    }
}
