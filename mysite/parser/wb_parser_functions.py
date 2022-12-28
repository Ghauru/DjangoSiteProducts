from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from comp.models import Product
from selenium import webdriver
import time


def parse_product(query, best_price):
    link = 'https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search=' \
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
        elements = driver.find_elements(By.CLASS_NAME, "j-card-item")
        for product in elements:
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
                                words_list.append(q.lower())
                        if compare_count > max_count:
                            specifies_list = ''
                            delivery = product.find_element(By.CLASS_NAME, 'product-card__delivery-date').text
                            max_words = words_list
                            max_count = compare_count
                            best_price = price
                            goods_name = product.find_element(By.CLASS_NAME, "goods-name").text
                            product_link = product.find_element(By.CLASS_NAME, "product-card__main").get_property('href')
                            image = product.find_element(By.CLASS_NAME, "j-thumbnail")
                            image_link = image.get_attribute('src')
                            try:
                                driver.execute_script(f'window.open("{product_link}");')
                                driver.switch_to.window(driver.window_handles[1])
                                specifies = driver.find_elements(By.CLASS_NAME, 'product-params__cell')
                                for i in specifies:
                                    specifies_list += str(i.text) + ' '
                                specifies_list = ' '.join(specifies_list.split())
                                seller = driver.find_element(By.CLASS_NAME, 'seller-info__name').text
                                additional_info = driver.find_elements(By.CLASS_NAME, 'collapsable__text')[0].text
                            except Exception as e:
                                print(e)
                            finally:
                                time.sleep(5)
                                driver.close()
                                driver.switch_to.window(driver.window_handles[0])
                        compare_count = 0
                        words_list = []
        driver.implicitly_wait(5)
    except Exception as ex:
        print(ex)
    finally:
        time.sleep(5)
        driver.close()
        driver.quit()
    product = Product()
    product.name = goods_name
    product.exist = True
    product.link = product_link
    product.price = best_price
    product.additional_information = additional_info
    product.image_link = image_link
    product.specifies = specifies_list
    product.seller = seller
    product.reviews = product_link+'/feedbacks'
    product.delivery = delivery
    product.market_place = 'Wildberries'
    return product, max_words