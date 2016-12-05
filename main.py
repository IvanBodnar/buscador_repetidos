import csv
from collections import Counter


with open('prueba.csv') as fh:
    """Crea una lista de diccionarios para poder
    re-iterar, porque DictReader es un generador
    y se exhausta la primera vez que se itera."""
    reader = list(csv.DictReader(fh))

"""Crea una lista de tuplas que contienen los campos a comparar"""
lista = [(x['id'], x['sexo'], x['edad']) for x in reader if x['id'].isdigit()]

"""Crea un objeto Counter (subclass de dict).
keys: tuple - con los campos a comparar
values: int - la cantidad de veces que se repite cada tupla"""
counter = Counter(lista)

"""Crea un dict 'filtrado' a partir del counter, solo con los
campos repetidos.
keys: str - las ids de los campos repetidos.
values: int - la cantidad de veces que se repite"""
rep = {x[0][0]: x[1] for x in counter.items() if x[1] > 1}

"""Itera por la lista reader y agrega un campo 'cantidad'.
Lo completa con la cantidad de veces q se repite si la id
está en rep. Deja None si no está."""
for x in reader:
    if x['id'] in rep.keys():
        x['cantidad'] = rep[x['id']]

"""Itera por la lista reader y agrega un campo 'original'.
Lo completa con un 1 cuando encuentra que el campo está en rep
y despues lo borra de rep, de manera que queda marcado
un solo caso por grupo de repetidos."""
for x in reader:
    if x['id'] in rep.keys():
        x['original'] = 1
        del rep[x['id']]



with open('resultado.csv', 'w') as fh:
    fieldnames = ['id', 'sexo', 'edad', 'cantidad', 'original']
    writer = csv.DictWriter(fh, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(reader)


