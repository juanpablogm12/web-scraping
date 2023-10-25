import requests
from bs4 import BeautifulSoup

URL_BASE = 'https://es.shein.com/Women-Dresses-c-1727.html?adp=10065537&src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_1%60ps%3D4_1%60jc%3Dreal_1727&src_tab_page_id=page_home1698194561650&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D10776958_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-1_ABT%3D0'
get_order = requests.get(URL_BASE)
html_contents = get_order.text

# print(html_contents)

soup = BeautifulSoup(html_contents, 'html.parser')
products = soup.find('h3')

print(products)