def show_menu():
    print("1. Ask question")
    print("2. Add question")
    print("3. Exit game")

    option = input("Enter option: ")
    return option


def add_question():
    print("")
    question = input("Enter a question:\n ")

    print("")
    print("Ok then, tell me the answere")
    answer = input("{0}\n ".format(question))

    file = open('question.txt', 'a')
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()


print(show_menu())


def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You selected 'Ask question'")
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else:
            print("Invalid option")
        print("")


game_loop()
