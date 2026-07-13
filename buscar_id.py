from api import buscar_liga_uruguaya

data = buscar_liga_uruguaya()

for liga in data["countries"]:
    print(liga["idLeague"], "-", liga["strLeague"], "-", liga["strCountry"])