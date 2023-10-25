import requests
from bs4 import BeautifulSoup

URL_BASE = 'https://scrapepark.org/courses/spanish'
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text

# print(html_obtenido)

soup = BeautifulSoup(html_obtenido, 'html.parser')
h2_todos = soup.find_all('h2')
# print(primer_h2)

# for seccion in h2_todos:
#     print (seccion.get_text(strip=True))

srcs = soup.find_all('img', src=True)
for elemento in srcs: 
    if elemento['src'].endswith(".jpg"):
      print(elemento)

# url_imagenes = []

# for i, imagen in enumerate(srcs):
    
#     if imagen['src'].endswith('.png'):
        
#         print(imagen)
#         r = requests.get(f"{URL_BASE}/{imagen['src']}")
        
#         with open(f'imagen_{i}.png', 'wb') as f:
#             f.write(r.content)