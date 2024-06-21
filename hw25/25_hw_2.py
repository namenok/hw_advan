import requests
import json

URL_2 = 'https://hacker-news.firebaseio.com/v0/topstories.json'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(URL_2, headers=headers)
article_list_url_2 = response.json()

for ident in article_list_url_2:

    st = 'https://hacker-news.firebaseio.com/v0/item/'
    id_from_li = str(ident)
    f = '.json'
    re = st + id_from_li + f
    URL = re

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(URL, headers=headers)
    article_dict = response.json()

    print(f'Title : {article_dict["title"]}')
    print(f'URL : {article_dict["url"]}')
    print(f'By : {article_dict["by"]}\nID : {article_dict["id"]}\nType:  {article_dict["type"]}')

