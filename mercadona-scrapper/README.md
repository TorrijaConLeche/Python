# Mercadona products web scrapper
### This program may have errors, it was made to learn Python.
---
Data collected from soysuper.com


## Use
Execute .py file and input how many products you want to collect.

    ```python
    soup = BeautifulSoup(r.content, 'lxml')
    articulos = soup.find_all('span', {"class": "productname"})
    precios = soup.find_all('span', {"class": "price"})
    ```
    
    ::We can change variable content to collect other data::


