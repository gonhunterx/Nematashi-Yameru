# ネマタ師 ー 辞める
from shopItems import shop_items2


# Classes
class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 900
        self.inventory = {}

    def display_stats(self):
        print("=======Player Stats=======")
        print(self.name)
        for item_name, (item, cost) in self.inventory.items():
            print(f"- {item_name} ({item.value} gold))")
        print(f"Gold: {self.gold}")

    def buy_item(self, item):
        total_cost = item.value
        if self.gold >= total_cost:
            self.gold -= total_cost
            self.inventory[item.name] = (item, total_cost)
            print(f"You have bought {item.name}")
            print(f"Adjusted gold value: {self.gold}")
            return True
        else:
            print("You do not have enough gold...")
            return False


def shop(player):
    # shop inventory
    global shop_items2
    print("You enter the shop...")
    print("=======Shop Inventory=======")

    # copy of shop_items2
    weapons_copy = list(shop_items2["Weapons"])

    for weapon in weapons_copy:
        print(f"- {weapon}")

    print("What would you like to buy?: ")
    item_to_buy = input("Input: ")

    for weapon in shop_items2["Weapons"]:
        if weapon.name.lower() == item_to_buy.lower():
            purchase_successful = player.buy_item(weapon)
            if purchase_successful:
                shop_items2["Weapons"].remove(weapon)
                print(f"{weapon.name} added to your inventory for {weapon.value} gold")
                break
    else:
        print("That item is not in the shop...")

    return player


def battle(player):
    print("You go into battle...")
    print("You have encountered a monster!")
    print("You attack first...")
    print("Choose your weapon: ")
    weapon_selection = input("Input: ")
    if weapon_selection in player.inventory:
        print("You attack the monster...")


def garden(player):
    print("You go to the garden...")
    print("Sift through the garden (y/n)?")
    choice = input("Input: ")
    if choice == "y":
        battle = battle(player)
    else:
        print("You leave the garden...")
        return player


def main():
    print("ネマタ師 ー 辞めるへようこそ")
    choice = ""
    player_name = input("What is your name?：")
    player = Player(player_name)
    while choice != "q":
        print("=======Main Menu=======")
        print("Where do you want to go?")
        print("1. To the shop")
        print("2. To the garden")
        print("3. Open backpack")
        print("'q' Exit Program")
        choice = input("Input: ")
        if choice == "1":
            shop(player)
        elif choice == "q":
            break
        elif choice == "2":
            print("You go to the garden...")
        elif choice == "3":
            player.display_stats()
        else:
            print("いいえ．．．また")


# tests
# obj = Item("Sword", 200)

# print(obj.__str__())

if __name__ == "__main__":
    main()
# class Item:
#     def __init__(self, name, value, quantity):
#         self.name = name
#         self.value = value
#         self.quantity = quantity

#     def __str__(self) -> str:
#         return f"{self.name}, {self.value}"
