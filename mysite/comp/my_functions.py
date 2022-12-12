from selenium.webdriver.common.by import By
from .models import Product
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--headless')

driver = webdriver.Chrome(executable_path='C:\\Users\\rules\\PycharmProjects\\DjangoSiteProducts\\comp'
                                          '\\chromedriver\\chromedriver.exe', options=options)
def parse_product(link):
    best_price = 0
    product_link = ''
    goods_name = ''
    exist = True
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
                        product_link = product.find_element(By.CLASS_NAME, "product-card__main").get_property('href')
        driver.implicitly_wait(5)
    except Exception as ex:
        print(ex)
    finally:
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