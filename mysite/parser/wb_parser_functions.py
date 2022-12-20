from selenium.webdriver.common.by import By
from comp.models import Product
from selenium import webdriver
import time


def parse_product(query, best_price):
    link = 'https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search=' \
                + '+'.join(query.split())
    product_link = ''
    goods_name = ''
    exist = True
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument('--headless')

    driver = webdriver.Chrome(executable_path='C:\\Users\\rules\\PycharmProjects\\DjangoSiteProducts\\parser'
                                              '\\chromedriver\\chromedriver.exe', options=options)
    try:
        driver.get(url=link)
        driver.implicitly_wait(5)
        elements = driver.find_elements(By.CLASS_NAME, "j-card-item")
        for product in elements:
            for elem in product.text.split('\n'):
                if '₽' in elem:
                    if ' ' in elem[:elem.find('₽')]:
                        price = int(''.join(elem[:elem.find('₽')].split()))
                    else:
                        price = int(elem[:elem.find('₽')])
                    if best_price > price or best_price==0:
                        best_price = price
                        goods_name = product.find_element(By.CLASS_NAME, "goods-name").text
                        if query not in goods_name:
                            return parse_product(query, best_price+1)
                        product_link = product.find_element(By.CLASS_NAME, "product-card__main").get_property('href')
        driver.implicitly_wait(5)
    except Exception as ex:
        print(ex)
    finally:
        time.sleep(5)
        driver.close()
        driver.quit()
    product = Product()
    product.name = goods_name
    product.exist = exist
    product.link = product_link
    product.price = best_price
    product.additional_information = 'Hello'
    product.image_link = 'image link'
    product.specifies = 'specifies'
    product.seller = 'seller'
    product.reviews = 'reviews'
    return product