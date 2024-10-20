import requests
import os
print("Welcome to the Update Wizard 🧙. This will update your current LB version.")
name = input("What is the name of your LigmaBalls file? (DO NOT INCLUDE .PY) ")
os.remove(name + ".py")
url = 'https://github.com/Freakybob-Team/lb/blob/main/lb.py?raw=true'
response = requests.get(url)
file_Path = "lb.py"
response = requests.get(url)
if response.status_code == 200:
    with open(file_Path, 'wb') as file:
        file.write(response.content)
        print('File downloaded successfully')
print("Done! Your LigmaBalls version has been updated.")
wantremove = input("Do you want to delete update.py? (Yes/No)")
if (wantremove == "Yes"):
    os.remove("update.py")
else:
    print("Okay! We have not deleted update.py.")
exec(open('lb.py').read())
