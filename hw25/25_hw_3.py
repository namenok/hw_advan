import requests

URL = 'https://meowfacts.herokuapp.com/'

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(URL, headers=headers)
print(response.status_code)
answ_dict = response.json()
print(answ_dict)