import sys
import os
import requests
import subprocess
import time
import socket
print("Welcome to Largs, LigmaBalls with args.")
# print("Here are some commands you can use:")
# print("fs")
# print("Using fs will launch freakysay, so you can echo your words!")
# print("clear")
# print("Clear clears the terminal!")
# print("freakybob")
# print("WARNING: FLOODS CONSOLE")
# print("This command prints a freakybob ASCII art thingymajig")
# print("update")
# print("Updates LigmaBalls")
# print("greg")
# print("Adds Greg Heffley to your desktop")
# print("ping")
# print("Pings google.com and provides the ping time in ms.")
# print("buttcalc")
# print("literally just a calculator")
if (sys.argv[1] == "fs"):
    isstop = "no"
    print("Welcome to freakysay, also known as FS.")
    while (isstop == "no"):
        echo = input("freakysay < ")
        print(echo)
if (sys.argv[1] == "clear"):
    os.system('cls' if os.name=='nt' else 'clear')
if (sys.argv[1] == "freakybob"):
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
if (sys.argv[1] == "update"):
    url = 'https://github.com/Freakybob-Team/lb/blob/main/Largsupdate.py?raw=true'
    response = requests.get(url)
    file_Path = 'update.py'
    if response.status_code == 200:
        with open(file_Path, 'wb') as file:
            file.write(response.content)
        print('File downloaded successfully')
        exec(open('update.py').read())
    else:
        print('Failed to download file')
        print("Trying another source...")
        alturl = 'https://codeberg.org/Freakybob/lb/raw/branch/main/Largsupdate.py'
        response = requests.get(alturl)
        file_Path = 'update.py'
        with open(file_Path, 'wb') as file:
            file.write(response.content)
            print('File downloaded successfully')
            exec(open('update.py').read())
if (sys.argv[1] == "greg"):
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
if (sys.argv[1] == "ping"):
    server = "google.com"
    try:
        start_time = time.time()
        sock = socket.create_connection((server, 80), timeout=2)
        end_time = time.time()
        sock.close()
        delay = (end_time - start_time) * 1000  
        print(f"Pong! {delay:.2f} ms")
    except Exception as e:
        print(f"Error connecting to {server}: {e}")
if (sys.argv[1] == "thiscommanddoesnotexist"):
    print("Yes it does.")
if (sys.argv[1] == "buttcalc"):
    num1 = input("First number: ")
    num2 = input("Second number: ")
    sign = input("Enter the operation thingy (ex: Addition) ")
    if (sign == "Addition"):
        sum = int(num1) + int(num2)
        print(sum)
    if (sign == "Multiplication"):
        product = int(num1) * int(num2)
        print(product)
    if (sign == "Subtraction"):
        difference = int(num1) - int(num2)
        print(difference)
    if (sign == "Division"):
        quotient = int(num1) / int(num2)
        print(quotient)
if (sys.argv[1] == "dungeon"):
    print("help freakybob has me in his dungeon send help NOW please")
if (sys.argv[1] == "quarky"):
    print("YOU DUMMY PYTHON 3.8??? THE NEWEST VERSION IS 3.13")
    print("AND A PIP VERSION FROM 2021?????")