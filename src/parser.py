import os 
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# carpeta script es la ruta del script actual, y ".." significa “la carpeta de arriba”:

carpeta_script = os.path.dirname(os.path.abspath(__file__))
ruta_HTML= os.path.join(carpeta_script, "..", "data", "raw", "index.html")
hoy = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
processed = os.path.join(carpeta_script, "..", "data", "processed")
os.makedirs(processed, exist_ok=True)
libros = []
with open(ruta_HTML,  mode = 'r' , encoding="utf-8") as archivo:
    contenido = archivo.read()
    soup = BeautifulSoup(contenido, 'html.parser')
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        libros.append({"title": title, "price": price})

df = pd.DataFrame(libros)
print(df.head()) # vista previa de los primeros 5 registros
print(df.dtypes) # muestra los tipos de datos de cada columna
df["price"] =  df["price"].str.replace('£', '').astype(float)
ruta_final = os.path.join(processed, f"precios{hoy}.csv")
df.to_csv(ruta_final, index=False) # guarda el DataFrame en un archivo CSV


print(carpeta_script)

