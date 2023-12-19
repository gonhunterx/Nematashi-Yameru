class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"{self.name}, {self.value}"


# Create instances of the Item class
item1 = Item("item1", 10)
item2 = Item("item2", 20)
item3 = Item("item3", 30)

# Create a dictionary and add objects with unique keys
item_dict = {}
item_dict["key1"] = item1
item_dict["key2"] = item2
item_dict["key3"] = item3


# Access objects in the dictionary
def main():
    print(item_dict["key1"])
    print(item_dict["key2"])
    print(item_dict["key3"])


main()
