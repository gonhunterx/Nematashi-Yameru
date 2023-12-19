# ネマタ師 ー 辞める


# Classes
class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.inventory = {}

    def display_stats(self):
        print(self.name)
        for item in self.inventory:
            print(f"- {item.value()}")


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"{self.name}, {self.value}"


def shop(player):
    # shop inventory
    shop_items = {}
    sword = Item("剣", 45)
    hammer = Item("短刀）たんとう", 30)
    axe = Item("斧（おんお）", 40)

    print("店に入る...")
    print()


def main():
    print("ネマタ師 ー 辞めるへようこそ")
    while input != "q":
        player_name = input("お名前は何ですか：")
        player = Player(player_name)
        print("どこに行きますか？")
        print("1. 店に")
        print("2. 公園に")
        print("3. オープンバックアップ")
        print("'q' プログラムーを止める")
        choice = input("Input: ")
        if choice == "1":
            shop(player)
        else:
            print("いいえ．．．また")


# tests
obj = Item("Sword", 200)

print(obj.__str__())

if __name__ == "__main__":
    main()
