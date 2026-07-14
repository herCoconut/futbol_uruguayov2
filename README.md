# futbol_uruguayov2
Analisis del futbol uruguayo con la API de TheSportsDB.

## Archvios creados
- ```api.py```: Archivo en el cual se accede a la api. 
- ```buscar_id.py```: Es utilizado para identificar la liga.
- ```equipos_liga.py```: Devuelve Invalid name passed.
- ```temporadas.py```: Dice cuantas temporadas hay en la base de datos.


### Archivo ```api.py```
Al ser una api publica y sin registro la API_KEY es conocida por todos (123), por este motivo no es necesario ocultarla. En caso de contar con la subscripcion paga de la api, si es necesario crear e; ```.env```.
La identificacion que la api le da a la primera division de Uruguay es 4432.

### Archivo ```temporadas.py```
Contiene unicamente las tempordas que tienen datos, por lo que la informacion que tree es un dict con las temporadas 2019, 2020, 2021, 2022 y 2023. 