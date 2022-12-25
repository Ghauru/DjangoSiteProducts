import sqlite3
from .wb_parser_functions import parse_product


def full_parser(query):
    def product_to_database(product):
        product.name = product.name.replace('\"', '')
        sql_insert_query = f'INSERT INTO comp_product(name, link, price, exist, specifies, seller,' \
                           f' additional_information, image_link, reviews, search_name) VALUES("{product.name}",' \
                           f' "{product.link}", "{product.price}", "{product.exist}", "{product.specifies}",' \
                           f' "{product.seller}", "{product.additional_information}", "{product.image_link}", "{product.reviews}"' \
                           f',"{product.name.lower()}")'
        db_path = 'db.sqlite3'
        print(sql_insert_query)
        with sqlite3.connect(db_path) as db:
            cursor = db.cursor()
            cursor.execute(sql_insert_query)

    item = parse_product(query, 0)
    product_to_database(item)