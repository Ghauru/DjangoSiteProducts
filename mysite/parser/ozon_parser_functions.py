from selenium.webdriver.common.by import By
#from comp.models import Product
from selenium import webdriver


def parse_product(query, best_price):
    link = 'https://www.ozon.ru/search/?from_global=true&text=' \
                + '+'.join(query.split())
    query_list = query.split()
    compare_count = 0
    max_count = 0
    max_words = []
    words_list = []
    image_link = ''
    product_link = ''
    goods_name = ''
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #options.add_argument('--headless')

    driver = webdriver.Chrome(executable_path='C:\\Users\\rules\\PycharmProjects\\DjangoSiteProducts\\parser'
                                              '\\chromedriver\\chromedriver.exe', options=options)
    try:
        driver.get(url=link)
        driver.implicitly_wait(5)
        elements = driver.find_elements(By.CLASS_NAME, "ex1")
        elements = elements[0].find_elements(By.CLASS_NAME, '16o')
        elements = elements[0].find_elements(By.CLASS_NAME, 'o16')
        elements = elements[0].find_elements(By.CLASS_NAME, 'lm6 l6m')
        for product in elements:
            print(product.text)
            print('-------')

    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()

parse_product(input(), 0)