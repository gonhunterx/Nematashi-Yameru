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
