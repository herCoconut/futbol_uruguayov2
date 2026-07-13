import requests
import os

# API de la aplicacion
API_KEY = '123' # key gratuita publica, sin registro
BASE_URL = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}"

# Identificacion de la liga uruguaya
ID_LIGA_URUGUAYA = 4432

def _get(endpoint, params=None):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def buscar_liga_uruguaya():
    return _get("search_all_leagues.php", {"c": "Uruguay", "s": "Soccer"})

def get_equipos_liga(nombre_liga="Uruguay Primera Division"):
    return _get("search_all_leagues.php", {"1": nombre_liga})

def get_temporadas(id_liga=ID_LIGA_URUGUAYA):
    return _get("search_all_season.php", {"id": id_liga})

def get_partidos_temporada(id_liga=ID_LIGA_URUGUAYA, temporada="2025-2026"):
    return _get("eventsseason.php", {"id": id_liga, "s": temporada})

def get_tabla(id_liga=ID_LIGA_URUGUAYA, temporada="2025-2026"):
    return _get("lookuptable.php", {"l": id_liga, "s": temporada})

def get_jugadores_equipo(id_equipo):
    return _get("lookup_all_players.php", {"id": id_equipo})

def get_proximos_partidos_liga(id_liga=ID_LIGA_URUGUAYA):
    return _get("eventsnextleague.php", {"id": id_liga})

def get_ultimos_partidos_liga(id_liga=ID_LIGA_URUGUAYA):
    return _get("eventspastleagur.php", {"id": id_liga})