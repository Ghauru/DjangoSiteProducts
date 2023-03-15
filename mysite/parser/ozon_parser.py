from parser.selenium_pages import UseSelenium
from parser.link_collector import parse_links
from parser.get_product_data import full_parser
from parser.get_product_json import parse_json

url = "https://www.ozon.ru/search/?from_global=true&text=xiaom+redmi+note+10"
filename = 'page.html'


UseSelenium(url, filename).save_page()
parse_links()
parse_json()
full_parser()
