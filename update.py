import requests
import os
print("Welcome to the Update Wizard. This will update your current LB version.")
url = 'https://github.com/Freakybob-Team/lb/blob/main/lb.py?raw=true'
response = requests.get(url)
file_Path = "lb.py"
response = requests.get(url)
if response.status_code == 200:
    with open(file_Path, 'wb') as file:
        file.write(response.content)
        print('File downloaded successfully')
else:
    print("Oops! There was an error and we couldn't download LigmaBalls.")
    print("We're trying a different source...")
    alturl = 'https://codeberg.org/Freakybob/lb/raw/branch/main/lb.py'
    response = requests.get(alturl)
    file_Path = "lb.py"
    with open(file_Path, 'wb') as file:
        file.write(response.content)
        print('File downloaded successfully')
print("Done! Your LigmaBalls version has been updated.")
wantremove = input("Do you want to delete update.py? (Yes/No) ")
if (wantremove == "Yes"):
    os.remove("update.py")
else:
    print("Okay! We have not deleted update.py.")
exec(open('lb.py').read())
