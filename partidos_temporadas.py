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
# print(f"\033[105m Cabezal del dataframe filtrado:\033[0m\n{partidos_filter.head(15)}")
# print(f"\033[104m Tipo de Dato de equipos:\033[0m {type(partidos_filter)}")


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

# Se concatenan los resultados, se agrupan según equipos y se calculan puntos y partidos jugados.
partidos = pd.concat(
    [
        partidos_filter[['strHomeTeam', 'puntos_local']].rename(columns={'strHomeTeam': 'Equipo', 'puntos_local': 'Puntos'}),
        partidos_filter[['strAwayTeam', 'puntos_visitante']].rename(columns={'strAwayTeam': 'Equipo', 'puntos_visitante': 'Puntos'}),
    ],
    ignore_index=True,
)


tabla_posiciones = (
    partidos.groupby('Equipo', as_index=False)
    .agg(
        Puntos=('Puntos', 'sum'),
        PJ=('Puntos', 'size'),
    )
    .sort_values('Puntos', ascending=False)
)

# Se muestra la informacion de la tabla de posiciones
print(f"\033[105m Tabla de posiciones:\033[0m\n{tabla_posiciones}")
print(f"\033[104m Tipo de Dato de tabla_posiciones:\033[0m {type(tabla_posiciones)}")

# Diccionario de colores de los equipos para 
colores_equipos = {
    "Peñarol": "#fdca01",                   #esta
    "Nacional Montevideo": "#f80020",       #esta
    "Defensor Sporting": "#450090",         #esta
    "Boston River": "#1f5428",              #esta
    "Progreso": "#de0204",
    "Cerro Largo FC": "#2b29d2",            #esta
    "Racing Montevideo": "#1c6823",         #esta
    "Liverpool Montevideo": "#003399",      #esta
    "Wanderers": "#1d120e",                 #esta
    "CA Cerro": "#0193de",                  #esta
    "Deportivo Maldonado": "#d00000",       #esta
    "Rampla Juniors": "#009a3e",
    "CA River Plate": "#c01b24",            #esta
    "Danubio": "#171613",                   #esta
    "Fenix": "#6e3178",                     #esta
    "Miramar": "#e5060b",
    "Montevideo City Torque": "#6caedf",    #esta
    "La Luz": "#056136",                    #esta
    "Plaza Colonia": "#00933d"              #esta
}

# Lista de colores a partir de el dict
colores_barras = [colores_equipos[label] for label in tabla_posiciones['Equipo']]

# Grafica
plt.figure(figsize=(18,10))
plt.bar(tabla_posiciones['Equipo'], tabla_posiciones['Puntos'], color=colores_barras)
plt.title("Posiciones Campeonato Uruguayo 2023 en la fecha 2")
plt.xlabel("Equipos")
plt.ylabel("Puntos")
plt.xticks(rotation=45)
for i, v in enumerate(tabla_posiciones["Puntos"]):
    plt.text(i, v + 0.5, str(v), ha='center', va='bottom')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("Imagenes/Posiciones.jpg")