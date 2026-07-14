import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from api import get_equipos_liga

data = get_equipos_liga()

# data es un diccionario que tiene una unica clave que es 'countries'.
# data['countries'] es 

print(f"Tipo de dato de data['countries']: {type(data['countries'])}")
print(f"Cantidad de elementos en data['countries']: {len(data['countries'])}")
print(f"Elementos de data['countries']: {data['countries']}")