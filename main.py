import json
import time
import webbrowser

import colorama
import pyautogui
import requests


# This is the part with the API of Classeviva, but it doesn't work (the API)
# Here's the link to the API page --> https://classevivapi.docs.apiary.io/#reference

# import urllib.request

# values = {"username": "daniele.beltrami13@gmail.com", "password": "Daniele30112003!"}

# headers = {
#   'Content-Type': 'application/json'
# }
# request = urllib.request.Request("https://api.morrillo.it/classeviva/v1/login", data=values, headers=headers)
# response_body = urllib.request.urlopen(request).read()
# print (response_body)


# send the messsage to every number in ther dictionary
def send(names_list, message):
    for name in names_list:
        # open the precompiled message on the browser and send it to every
        # number in the dictionary
        webbrowser.open(f"https://wa.me/{numbers[name]}?text={message}")
        print(
            colorama.Fore.GREEN
            + "[V] "
            + colorama.Fore.WHITE
            + f"message sent to {name}"
        )
        # wait 7 seconds
        time.sleep(7)
        # press the enter key to send the message
        pyautogui.press("enter")


# load the file json with the numbers
numbers_file = open("contacts.json", "r").read()
numbers = json.loads(numbers_file)

# names in the dictionary
names_list = numbers.keys()

# take the neko image
url_neko_pic = requests.get("https://nekos.life/api/v2/img/neko").json()["url"]

# write here the message that will be sent
message = f"Hi!%20Here's a neko for you <3%20{url_neko_pic}"

# call the function
send(names_list, message)
