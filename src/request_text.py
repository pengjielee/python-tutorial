import requests

url = 'https://cnodejs.org/'

r = requests.get(url)

print(r.text)