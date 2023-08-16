import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://habr.com/ru/articles/670980/"
r = requests.get(URL_TEMPLATE)
soup = bs(r.text, "html.parser")
vacancies_names = soup.find_all('h2', class_='tm-comments-wrapper__title')
for name in vacancies_names:
    print(name.a['title'])
print(r.status_code)

print(bs.text)