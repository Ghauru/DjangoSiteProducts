from bs4 import BeautifulSoup
import sqlite3
import re


db = 'db.sqlite3'
sqlite_connect = sqlite3.connect(db)
with sqlite_connect.cursor() as cursor:
    qry = 'SELECT * FROM {}'
    print(list(cursor.execute(qry)))