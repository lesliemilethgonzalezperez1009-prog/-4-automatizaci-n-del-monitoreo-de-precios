import requests
from bs4 import BeautifulSoup
import openpyxl
import os
# El texto es "..", que en una ruta significa “la carpeta de arriba”:

Url = "https://books.toscrape.com/"
page = requests.get(Url)
page.raise_for_status()
carpeta_script = os.path.dirname(os.path.abspath(__file__))
raw = os.path.join(carpeta_script, "..", "data", "raw")
# print (raw)```python
page.encoding = "utf-8"

os.makedirs(raw, exist_ok=True)
pagina1= os.path.join(raw, "index.html")

def guardar_html(contenido, ruta_archivo):
    with open(ruta_archivo,  mode = 'w', encoding="utf-8") as archivo:
        archivo.write(contenido)
guardar_html(page.text, pagina1)