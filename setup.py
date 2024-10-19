import requests
import os
print("We're installing LigmaBalls. Please wait!")
url = 'https://github.com/Freakybob-Team/lb/blob/main/lb.py?raw=true'
response = requests.get(url)
file_Path = "lb.py"
response = requests.get(url)
print("URL fetched...")
if response.status_code == 200:
    print("Fetch successful")
    with open(file_Path, 'wb') as file:
        file.write(response.content)
        print('File downloaded successfully')
os.remove("setup.py")
exec(open('lb.py').read())