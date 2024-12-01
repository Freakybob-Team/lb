import requests
import os
print("Welcome to the Update Wizard. This will update your current Largs version.")
url = 'https://github.com/Freakybob-Team/lb/blob/main/Largs.py?raw=true'
response = requests.get(url)
file_Path = "Largs.py"
response = requests.get(url)
if response.status_code == 200:
    with open(file_Path, 'wb') as file:
        file.write(response.content)
        print('File downloaded successfully')
else:
    print("Oops! There was an error and we couldn't download Largs.")
    print("We're trying a different source...")
    alturl = 'https://codeberg.org/Freakybob/lb/raw/branch/main/Largs.py'
    response = requests.get(alturl)
    file_Path = "Largs.py"
    with open(file_Path, 'wb') as file:
        file.write(response.content)
        print('File downloaded successfully')
print("Done! Largs has been updated.")
wantremove = input("Do you want to delete update.py? (Yes/No) (Case-sensitive) ")
if (wantremove == "Yes"):
    os.remove("Largsupdate.py")
else:
    print("Okay! We have not deleted update.py.")
exec(open('Largs.py').read())
