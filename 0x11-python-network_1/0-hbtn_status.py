#!/usr/bin/python3
from urllib.request import urlopen

url = "https://alx-intranet.hbtn.io/status"

with urlopen(url) as response:
    body = response.read()

print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode('utf-8'))
