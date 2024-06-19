import requests
import json

URL = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(URL, headers=headers)
# print(response.status_code)
article_dict = response.json()

print(str(article_dict))

