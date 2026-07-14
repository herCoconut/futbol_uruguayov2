from api import get_temporadas

data = get_temporadas()

print(f"Tipo de dato de data: {type(data['seasons'])}")
print(f"Cantidad de elementos en data: {len(data['seasons'])}")
print(f"Elementos de data: {data['seasons'][0]}")