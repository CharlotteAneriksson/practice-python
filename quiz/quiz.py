def show_menu():
    print("1. Ask question")
    print("2. Add question")
    print("3. Exit game")

    option = input("Enter option: ")
    return option


print(show_menu())


def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You selected 'Ask question'")
        elif option == "2":
            print("You selected 'Add question'")
        elif option == "3":
            break
        else:
            print("Invalid option")
        print("")


game_loop()
