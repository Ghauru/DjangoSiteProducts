from bs4 import BeautifulSoup
import sqlite3
import re
import urllib.request


sqlite_connect = sqlite3.connect('test.db')
sqlite_create_table = 'CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT not null,' \
                        ' link TEXT UNIQUE not null, price REAL, exist BOOL)'
cursor = sqlite_connect.cursor()
cursor.execute(sqlite_create_table)
cursor.close()

ozon_search = 'https://www.ozon.ru/search/?from_global=true&text=' + '+'.join(str(input()).lower().split())

def url_decode(url):
    hdr = {'User-Agent': 'Chrome/108.0.5359.98',
        'Accept-Language': 'ru-RU,ru;q=0.8',
        'Connection': 'keep-alive'}

    request = urllib.request(url,None, headers=hdr)
    return request.urlopen(url).read().decode('utf-8')


#def product_to_database():

url = url_decode(ozon_search)

main_soup = BeautifulSoup(url, 'html.parser')
