
import pyfiglet
  
result = pyfiglet.figlet_format("SPY-BREACHER",font = 'doh',width = 500)
print(result)
banner = pyfiglet.figlet_format("Developed by SPIDY", font="slant", justify="left")

print(banner)

import os
import time
import requests

import json
#pip install json2html
from json2html import *

PATH = 'api_file.txt'
def check():
    
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        print("API FOUND !!!!!")
        
    else:
        
        print("API Not Found !!!!")
        ap = input("ENTER YOUR BREACH DIRECTORY API -: ")
        with open('api_file.txt', 'w') as j:
            j.write(ap)
        j.close()
        check()
        
check()
k = open('api_file.txt')
q = k.read()
print(q)
us = input('Enter Email (example123@gmail.com)-: ')

url = "https://breachdirectory.p.rapidapi.com/"

querystring = {"func":"auto","term":us}

headers = {

    "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com",

    "X-RapidAPI-Key": q

}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

with open('data.json', 'w') as f:
    f.write(response.text)
    f.close()
    print("\nResponse Data has been written to data.json file !!!!!\n\n")

choice_out = int(input("Press 0 to EXIT \n\nPress 1 to write the response to HTML TABLE format \n\nEnter Choice -: "))

if choice_out == 0:
    print("\nThanks for using this program !!!")
    time.sleep(3)
    exit()

if choice_out == 1:
    a = f'"""{response.text}"""'
    json_object = a
    #print(json_object)
    #json_k= json.loads('data.json')
    with open('data.json', 'r') as j:
        contents = json.loads(j.read())
        haha = json2html.convert(json=contents)
        x = open('web.html', 'w')
        x.write(haha)
        x.close()
    print("Response Data has been written to web.html file !!!!!")
    print("\nThanks for using this program !!!")
    time.sleep(3)
    exit()
else:
    print("\nThanks for using this program !!!")
    time.sleep(3)
    exit()
