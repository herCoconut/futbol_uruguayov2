import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from api import get_partidos_temporada

# Datos de la temporada 2023, que es la mas reciente en la cual hay datos.
data = get_partidos_temporada(temporada="2023")

# Se imprime informacion sobre data, es un diccionario de largo 1 con key 'events'.
# print(f"Tipo de dato de data: {type(data)}")
# print(f"Cantidad de elementos en data: {len(data)}")
# print(f"Elementos de data: {data.keys()}")

# Se imprime informacion sobre data['events'], que es una lista de largo 15
# print(f"Tipo de dato de data['events']: {type(data['events'])}")
# print(f"Cantidad de elementos en data['events']: {len(data['events'])}")

# Se imprimen informacion sobre el primer elemento de data['events'], que es un
# diccionario de largo 30 que contine un partido de la temporada 2023.
# print(f"\033[105m Primer elemento de data['events']:\033[0m {data['events'][0]}")
# print(f"Largo de data['events'][0]: {len(data['events'][0])}")
# print(f"Keys de data['events'][0]: {data['events'][0].keys()}")

# Se crea el dataframe a partir de data
partidos = pd.json_normalize(data['events'])

print(f"Cabezal del dataframe{partidos.head(10)}")
print(f"Info del dataframe{partidos.info()}")
print(f"Columnas del dataframe{partidos.columns}")