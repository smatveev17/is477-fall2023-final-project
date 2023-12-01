import requests
import hashlib
import os

wine_url = 'https://archive.ics.uci.edu/static/public/109/wine.zip'
response = requests.get(wine_url)

if not os.path.exists('data'):
    os.makedirs('data')

with open ('data\\wine\\wine.zip', mode='wb') as f:
    f.write(response.content)

filename = 'data\\wine\\wine.zip'
with open (filename, mode='rb') as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()

wine_hash = "2bae62c4481220623579d4c4fb36b55652b6b75e06e49fa1981b8198362dfdab"

if wine_hash != sha256hash:
    print('Computed hash (wine) does not match expected hash')
else:
    print('Computed hash (wine) matches expected hash')


