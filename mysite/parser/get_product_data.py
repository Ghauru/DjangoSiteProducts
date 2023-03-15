import sqlite3
import json
import glob
import re
from comp.models import Product

def full_parser():
    def parse_product():
        products = get_products()
        price = 99999999
        for product in products:
            try:
                product_json = get_json(product)
                result = parse_data(product_json)
                if result.price < price:
                    price = result.price
                    final_result = result
            except Exception as e:
                print(e)
        return final_result

    def product_to_database(product):
        product.name = product.name.replace('\"', '')
        text = 'specifies'
        product.specifies = text
        sql_insert_query = f'INSERT INTO comp_product(name, link, price, exist, specifies, seller,' \
                           f' additional_information, image_link, reviews, search_name, delivery, market_place' \
                           f') VALUES("{product.name}",' \
                           f' "{product.link}", "{product.price}", {product.exist}, "{product.specifies}",' \
                           f' "{product.seller}", "{product.additional_information}", "{product.image_link}", "{product.reviews}"' \
                           f',"{product.name.lower()}","{product.delivery}","{product.market_place}")'
        db_path = 'db.sqlite3'
        with sqlite3.connect(db_path) as db:
            cursor = db.cursor()
            cursor.execute(sql_insert_query)

    def get_products() -> list:
        return glob.glob('products/*.html')

    def get_json(filename: str) -> dict:
        with open(filename, 'r', encoding='utf-8') as f:
            data = f.read()
            return json.loads(data)

    def parse_data(data: dict) -> dict:
        widgets = data.get('widgetStates')
        for key, value in widgets.items():
            if 'webGallery' in key:
                image_link = json.loads(value).get('coverImage')
            if 'webProductHeading' in key:
                title = json.loads(value).get('title')
            if 'webSale' in key:
                prices = json.loads(value).get('offers')[0]
                if prices.get('price'):
                    price = re.search(r'[0-9]+', prices.get('price').replace(u'\u2009', ''))[0]
                else:
                    price = 0
            if 'webCharacteristics' in key:
                specifies = json.loads(value).get("characteristics")
        layout = json.loads(data.get('layoutTrackingInfo'))
        seller = layout.get('brandName')
        url = layout.get('currentPageUrl')
        reviews = url + 'reviews'
        product = Product()
        product.name = title
        product.exist = True
        product.link = url
        product.price = int(price)
        product.additional_information = 'no additional info'
        product.image_link = image_link
        product.specifies = specifies
        product.seller = seller
        product.reviews = reviews
        product.delivery = 'later'
        product.market_place = 'Ozon'
        return product

    product_to_database(parse_product())