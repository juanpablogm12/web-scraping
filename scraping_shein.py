import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import time

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get("https://us.shein.com/")
driver.add_cookie({"name":"sessionID_shein","value":"s%3A9YbPM0_8AO5r-hGW8TW-5u5nu89OUQWk.hjEGt7sJYdeFMDOy%2F1ytFtt%2FCkPMkYIDZdQOc30qwdw"})

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
    
src_images = soup.find_all('div', class_="crop-image-container")
    # print("esta es la caja de las imagenes:", src_images)
    
    # for element in src_images:
    #      if element['src'].endswith(".png"):
    #          print("estas son las imagenes:", element)

for i, imagen in enumerate(src_images):    
    if imagen['data-before-crop-src'].endswith('.jpg'):
        print("la imagen", imagen['data-before-crop-src'])
        r = requests.get(f"https:{imagen['data-before-crop-src']}")
        
        with open(f'imagen_1{i}.jpg', 'wb') as f:
           f.write(r.content)





