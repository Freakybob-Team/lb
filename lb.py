import os
import requests
import subprocess
def code():
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
    print("Welcome to LB, also known as LigmaBalls.")
    print("For help, type help below.")
    command = input("lb < ")
    if (command == "fs"):
        print("This command is broken. Thanks for your patience! <3")
        code()
        # print("Welcome to freakysay, also known as FS.")
        # echo = input("freakysay < ")
        # print(echo)
    if (command == "help"):
        print("Welcome to LigmaBalls!")
        print("Here are some commands you can use:")
        print("fs")
        print("Using fs will launch freakysay, so you can echo your words! (BROKEN)")
        print("credits")
        print("Using credits will show the people who helped make this!")
        print("clear")
        print("Clear clears the terminal!")
        print("freakybob")
        print("WARNING: SPAMS CONSOLE")
        print("This command prints a freakybob ASCII art thingymajig")
        print("update")
        print("Updates LigmaBalls")
        print("greg")
        print("Adds Greg Heffley to your desktop")
        print("packing")
        print("A package manager for LigmaBalls!")
        code()
    if (command == "credits"):
        print("Wish made the intial 1.0 version! He also made freakysay and the first version of help.")
        print("Names helped Wish decide on the name!")
        print("Made with love by the Freakybob Team <3")
        code()
    if (command == "clear"):
        cls()
        code()
    if (command == "freakybob"):
        print("This requires an additional download of 5.42 KB.")
        input("Are you fine with that? Close this if not. ")
        url = 'https://github.com/Freakybob-Team/lb/blob/main/freakybob.txt?raw=true'
        response = requests.get(url)
        file_Path = 'freakybob.txt'
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
        fb = open("freakybob.txt", "r")
        print(fb.read())
        fb.close()
        code()
    if (command == "update"):
        print("This requires an additional download of 569 bytes.")
        input("Are you fine with that? Close this if not. ")
        url = 'https://github.com/Freakybob-Team/lb/blob/main/update.py?raw=true'
        response = requests.get(url)
        file_Path = 'update.py'

        if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
            print('File downloaded successfully')
            exec(open('update.py').read())
        else:
            print('Failed to download file')
            print("Bringing you back...")
            code()
    if (command == "greg"):
        url = 'https://github.com/Freakybob-Team/lb/blob/main/greg.bat?raw=true'
        response = requests.get(url)
        file_Path = 'greg.bat'
        if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
                file.close()
                subprocess.run(['greg.bat'])
        else:
            print('Failed to download file')
            print("Bringing you back...")
            code()
    if (command == "packing"):
        print("Welcome! Packing is a package manager for LigmaBalls.")
        print("This desert is very dry.. Upload something with the link below!")
        print("https://github.com/Freakybob-Team/packign")
        code()
code()