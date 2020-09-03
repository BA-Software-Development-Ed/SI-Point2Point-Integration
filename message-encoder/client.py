import requests
import sys

try:
    payload = sys.argv[1]
except:
    payload = 'default payload'

response = requests.post('http://127.0.0.1:6666/', data=payload)
print(response.text)
