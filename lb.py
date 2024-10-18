import os
def code():
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
    print("Welcome to LB, also known as LigmaBalls.")
    print("For help, type help below.")
    command = input("lb > ")
    if (command == "fs"):
        isstop = "no"
        print("Welcome to freakysay, also known as FS.")
        print("To exit, say stop.")
        while (isstop == "no"):
            echo = input("freakysay < ")
            if (echo == "stop"):
                isstop = "yes"
        print(echo)
    if (command == "help"):
        print("Welcome to LigmaBalls!")
        print("Here are some commands you can use:")
        print("fs")
        print("Using fs will launch freakysay, so you can echo your words!")
        print("credits")
        print("Using credits will show the people who helped make this!")
        print("clear")
        print("Clear clears the terminal!")
        code()
    if (command == "credits"):
        print("Wish made the intial 1.0 version! He also made freakysay and the first version of help.")
        print("Names helped Wish decide on the name!")
        print("Made with love by the Freakybob Team <3")
        code()
    if (command == "clear"):
        cls()
        code()
code()