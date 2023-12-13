import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import pprint
import time

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get("https://us.shein.com/")
driver.add_cookie({"name":"sessionID_shein","value":"s%3AAwee4OKP8XpUPE0qtiQf0JPVfzdnwjLk.Fa8nVe%2FFcZnY9HGXo0FFwaw0YYtXqB044keAR8pp99w"})

try:
    wait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-close"))).click()
    wait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "svgicon-arrow-left"))).click()
    print("aparece el descuento")
    pass
except:
    pass
    print("no aparece el descuento")

wish_list = wait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "header-wishlist"))).click()
products = wait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "j-product-list-info")))
products = products.get_attribute('innerHTML')
soup = BeautifulSoup(products, 'html.parser')
    
cards = soup.find_all('section', class_='wish-list__item')

list_products = []

for element in cards:
    name = element.find('a', class_='S-product-item__link').text
    price = element.find('span', class_='normal-price-ctn__sale-price').text
    image = element.find('div', class_='crop-image-container')['data-before-crop-src']

    card_info = {'name': name, 'price': price, 'image': image}
    list_products.append(card_info)

    r = requests.get(f'https:{image}')
    with open(f'{name}.jpg', 'wb') as f:
        f.write(r.content)

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(list_products)    
