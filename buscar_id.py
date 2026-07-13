from api import buscar_liga_uruguaya

data = buscar_liga_uruguaya()

for liga in data['leagues']:
    print(liga["idLeague"], "-", liga["strLeague"], "-", liga["strCountry"])