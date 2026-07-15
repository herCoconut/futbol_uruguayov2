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

# Muestra informacion sobre los partidos que se tiene de la temporada 2023.
# print(f"Cabezal del dataframe{partidos.head(15)}")
# print(f"Info del dataframe{partidos.info()}")
# print(f"Columnas del dataframe{partidos.columns}")

partidos_filter = partidos[['idEvent', 'intRound', 'dateEvent', 'strTime', 'strHomeTeam', 'strAwayTeam', 'intHomeScore', 'intAwayScore']]

# Muestra informacion filtra (informacion relevante) sobre los partidos que se tiene de la temporada 2023.
print(f"\033[105m Cabezal del dataframe filtrado:\033[0m\n{partidos_filter.head(15)}")
print(f"\033[104m Tipo de Dato de equipos:\033[0m {type(partidos_filter)}")


# Se crea una copia de partidos_filter
partidos_filter = partidos_filter.copy()

# Se crea una nueva columna 'puntos_local', donde el valor esta asignado dependiendo del resultado del partido.
partidos_filter['puntos_local'] = np.select(
    [
        partidos_filter['intHomeScore'] > partidos_filter['intAwayScore'],
        partidos_filter['intHomeScore'] < partidos_filter['intAwayScore'],
    ],
    [3, 0],
    default=1,
)

# Se crea una nueva columna 'puntos_local', donde el valor esta asignado dependiendo del resultado del partido.
partidos_filter['puntos_visitante'] = np.select(
    [
        partidos_filter['intHomeScore'] < partidos_filter['intAwayScore'],
        partidos_filter['intHomeScore'] > partidos_filter['intAwayScore'],
    ],
    [3, 0],
    default=1,
)

# Se concatenan los resultados, se agrupan segun equipos y se suman los puntos
tabla_posiciones = (
    pd.concat(
        [
            partidos_filter[['strHomeTeam', 'puntos_local']].rename(columns={'strHomeTeam': 'Equipo', 'puntos_local': 'Puntos'}),
            partidos_filter[['strAwayTeam', 'puntos_visitante']].rename(columns={'strAwayTeam': 'Equipo', 'puntos_visitante': 'Puntos'}),
        ]
    )
    .groupby('Equipo', as_index=False)['Puntos']
    .sum()
    .sort_values('Puntos', ascending=False)
)

print(f"\033[105m Tabla de posiciones:\033[0m\n{tabla_posiciones}")
print(f"\033[104m Tipo de Dato de tabla_posiciones:\033[0m {type(tabla_posiciones)}")