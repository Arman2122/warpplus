import requests
import json
import datetime
import random
import string
import time

print ("[?] Q; How to find a WARP+ ID?")
print ("[-] A; Go this route and copy the WARP+ ID => Setting/Advanced/Diagnostics/ID")
print ("---------------------------------------")
print ("   This script is coded By Arman_HC") 
print ("---------------------------------------")
referrer = input("Enter the WARP+ ID: ")
def genString(stringLength):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))
def digitString(stringLength):
    digit = string.digits
    return ''.join((random.choice(digit) for i in range(stringLength)))    
url = 'http://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
    install_id = genString(11)
    body = {"key": "{}=".format(genString(42)),
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
            "referrer": referrer,
            "warp_enabled": False,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
            "type": "Android",
            "locale": "zh-CN"}
    bodyString = json.dumps(body)
    headers = {'Content-Type': 'application/json; charset=UTF-8',
               'Host': 'api.cloudflareclient.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.12.1'
               }
    r = requests.post(url, data=bodyString, headers=headers)
    return r
c = 1
while True:
    result = run()
    if result.status_code == 200:
        print(f"\n{c - 1} GB has been successfully added to your account.")
        c = c + 1
        time.sleep(2)
    else:
        print("Error when connecting to server.")

