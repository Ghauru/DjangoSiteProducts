import sqlite3
from .wb_parser_functions import parse_product

wb_search = 'https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search='\
            + '+'.join(str(input()).lower().split())

def product_to_database(product):
    sql_insert_query = f'INSERT INTO comp_product(name, link, price, exist, specifies, seller,' \
                       f' additional_information, image_link, reviews) VALUES("{product.name}",' \
                       f' "{product.link}", "{product.price}", "{product.exist}", "{product.specifies}",' \
                       f' "{product.seller}", "{product.additional_information}", "{product.image_link}", "{product.reviews}")'
    db_path = 'C:\\Users\\rules\\PycharmProjects\\DjangoSiteProducts\\mysite\\db.sqlite3'
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        cursor.execute(sql_insert_query)

item = parse_product(wb_search)
product_to_database(item)