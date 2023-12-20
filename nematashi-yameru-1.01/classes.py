class Item:
    def __init__(self, name, value, damage):
        self.name = name
        self.value = value
        self.damage = damage

    def __str__(self):
        return f"{self.name}, {self.value}, {self.damage}"


class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 400
        self.inventory = []

    def display_stats(self):
        print(f"{self.name}")
        for item in self.inventory:
            print(
                f"""
            ====================
            name: {item.name},
            damage: {item.damage}
                  """
            )
        print(f"{self.gold}")

    def buy_item(self, item_name):
        if self.gold >= item_name.value:
            pass
