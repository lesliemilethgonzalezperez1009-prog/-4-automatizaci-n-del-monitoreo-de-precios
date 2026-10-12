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
# print(df.head()) # vista previa de los primeros 5 registros
# print(df.dtypes) # muestra los tipos de datos de cada columna
df["price"] =  df["price"].str.replace('£', '').astype(float)
ruta_final = os.path.join(processed, f"precios{hoy}.csv")



# print(carpeta_script)
# print(sorted(os.listdir(processed)))
# print(len(os.listdir(processed)))
# listar la carpeta
# leer csv anterior asi no se confunde por que ya los datos anteriores estan
# para luego guardar el actual

lista = os.listdir(processed)
if not lista:
    viejo = None
    anterior = None
else:
    reciente = sorted(lista)[-1]
    anterior  = os.path.join(processed, reciente)
    viejo = pd.read_csv(anterior)
    if viejo is not None:
        df = merge(df, viejo, on="titulo")
        print(df)
# df.to_csv(ruta_final, index=False) # guarda el DataFrame en un archivo CSV
print(reciente, len(viejo), len(df))
