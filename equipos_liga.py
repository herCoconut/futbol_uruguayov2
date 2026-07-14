from api import get_equipos_liga

data = get_equipos_liga()

# data es un diccionario que tiene una unica clave que es 'countries'.
# data['countries'] devuelve Invalid name passed. INDAGAR MAS AL RESPECTO EN LA DOC DE LA API.

print(f"Tipo de dato de data['countries']: {type(data['countries'])}")
print(f"Cantidad de elementos en data['countries']: {len(data['countries'])}")
print(f"Elementos de data['countries']: {data['countries']}")