# Mercadona products web scrapper (Based on soysuper.com data)
# This program may have errors, it was created to learn python

import requests
from bs4 import BeautifulSoup

file = open("datos.txt", "w", encoding="utf8")

pagcont = 1
prod_buscados = int(input("How many products do you want to collect?: "))
num_producto = 1  # Variable usada para asignar a los productos un numero

while num_producto < prod_buscados:

    url = 'https://soysuper.com/marca/mercadona?page='  # URL de la pagina
    url = url + str(pagcont)  # Le concatenamos el numero de pagina

    file.write("\nPagina {}".format(pagcont))
    file.write("\n----------------------")
    file.write("\n")

    r = requests.get(url)  # Definimos la peticion a la pagina

    # Tambien podemos parsear con html.parse
    soup = BeautifulSoup(r.content, 'lxml')
    articulos = soup.find_all('span', {"class": "productname"})
    precios = soup.find_all('span', {"class": "price"})

    pagcont += 1  # Utilizado para contar las paginas

    # Utilizado para iterar exactamente 24 veces (ya que cada pagina tiene 24 productos)
    contador = 1

    for a, p in zip(articulos, precios):
        if num_producto == prod_buscados + 1:  # Paramos la ejecucion si ya hemos devuelto los articulos que buscabamos
            exit()
        if contador < 25:

            file.write("\nNumero producto: {}".format(num_producto))
            file.write("\nProducto: {}".format(a.getText()))
            file.write("\nPrecio: {}".format(p.getText()))
            file.write("\n")

            contador += 1
            num_producto += 1

        else:
            break

file.close()
