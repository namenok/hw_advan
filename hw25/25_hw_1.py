from bs4 import BeautifulSoup
import requests

response = requests.get(
    'https://bank.gov.ua/'
)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    my_block = soup.find('div', class_='collection macro-indicators')
    my_block_detail = my_block.find_all('div', class_='collection-item indicator with-dir')

    my_euro = my_block_detail[2].find('div', class_='col-xs-4')
    strip_my_euro = my_euro.text.strip()
    print(f'курс євро до гривні : {strip_my_euro}')

    my_dollar = my_block_detail[3].find('div', class_='value index-page')
    strip_my_dol = my_dollar.text.strip()
    print(f'курс долару до гривні : {strip_my_dol}')










