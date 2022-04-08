import sys
import subprocess
import os
import time
import urllib.request
from urllib.request import urlopen
import json

print("Running Setup...")
print("Installing Required Packages...")
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pynput'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pywin32'])

print("\nChecking for default word list...")
datajson_url = "https://raw.githubusercontent.com/CJ-5/AutoWorlde/main/data.json"
if not os.path.isfile("data.json"):
    print(f"Error: No Default Data.json word list found. You can find this file here. {datajson_url}")
    answer = None
    while answer != "yes" and answer != "no":
        answer = input("Would you like to download this file automatically? (yes / no): ").lower().replace(' ', '')
        if answer == "yes":
            try:
                with open("data.json", "w") as outfile:
                    response = urlopen(datajson_url)
                    json.dump(json.loads(response.read()), outfile)

                if os.path.isfile("data.json"):
                    print("File Fetched Successfully")
                else:
                    raise Exception("An Error Occurred, File was not created")
            except:
                if os.path.isfile("data.json"):
                    os.remove("data.json")
                raise Exception("An Error occurred while fetching the wordlist file")

        elif answer == "no":
            print("Exiting...")
            time.sleep(1.3)
            quit(-1)
        else:
            print("Invalid answer...")
            time.sleep(1.3)
            os.system("cls")
