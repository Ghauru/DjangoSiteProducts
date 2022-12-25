from selenium.webdriver.common.by import By
from comp.models import Product
from selenium import webdriver
import time


def parse_product(query, best_price):
    link = 'https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search=' \
                + '+'.join(query.split())
    query_list = query.split()
    compare_count = 0
    product_name = ''
    image_link = ''
    product_link = ''
    goods_name = ''
    exist = True
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('--headless')

    driver = webdriver.Chrome(executable_path='C:\\Users\\rules\\PycharmProjects\\DjangoSiteProducts\\parser'
                                              '\\chromedriver\\chromedriver.exe', options=options)
    try:
        driver.get(url=link)
        driver.implicitly_wait(5)
        elements = driver.find_elements(By.CLASS_NAME, "j-card-item")
        for product in elements:
            print(product.text)
            print('-----------')
            for elem in product.text.split('\n'):
                if '₽' in elem:
                    if ' ' in elem[:elem.find('₽')]:
                        try:
                            price = int(''.join(elem[:elem.find('₽')].split()))
                        except:
                            price = int(''.join(elem[2:elem.find('₽')].split()))
                    else:
                        try:
                            price = int(elem[:elem.find('₽')])
                        except:
                            price = int(elem[2:elem.find('₽')])
                    if best_price > price or best_price==0: #and query.lower() in goods_name.lower() or goods_name=='':
                        product_name = product.find_element(By.CLASS_NAME, "goods-name").text
                        for q in query_list:
                            if q.lower() in product_name.lower():
                                compare_count += 1
                        if compare_count == len(query_list):
                            best_price = price
                            goods_name = product.find_element(By.CLASS_NAME, "goods-name").text
                            product_link = product.find_element(By.CLASS_NAME, "product-card__main").get_property('href')
                            image = product.find_element(By.CLASS_NAME, "j-thumbnail")
                            image_link = image.get_attribute('src')
                        compare_count = 0
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
    product.image_link = image_link
    product.specifies = 'specifies'
    product.seller = 'seller'
    product.reviews = 'reviews'
    return product