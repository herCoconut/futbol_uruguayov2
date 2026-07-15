# futbol_uruguayov2
Analisis del futbol uruguayo con la API de TheSportsDB.

## Archvios creados
- ```api.py```: Archivo en el cual se accede a la api. 
- ```buscar_id.py```: Es utilizado para identificar la liga.
- ```equipos_liga.py```: Devuelve Invalid name passed.
- ```temporadas.py```: Dice cuantas temporadas hay en la base de datos.
- ```partidos_temporadas.py```: Muestra los partidos de la temporada 2023. NO ESTAN TODOS LOS PARTIDOS.

### Archivo ```api.py```
Al ser una api publica y sin registro la API_KEY es conocida por todos (123), por este motivo no es necesario ocultarla. En caso de contar con la subscripcion paga de la api, si es necesario crear e; ```.env```.
La identificacion que la api le da a la primera division de Uruguay es 4432.

### Archivo ```temporadas.py```
Contiene unicamente las tempordas que tienen datos, por lo que la informacion que tree es un dict con las temporadas 2019, 2020, 2021, 2022 y 2023. 

### Archivo ```partidos_temporadas.py```
Con varios parametros sobre los partidos disputados, desde quien era local y visitante hasta los goles de los locales y visitantes. Como <span style="color: red">negativo</span> esta el hecho de que es informacion incompleta, tienen informacion de las 2 primeras fechas.
Se hace una grafica de barra para visualizar las posiciones de los equipos en la fecha 2, las imagenes se guardan en la carpeta Imagenes.


## Carpetas creadas
- Se crea la carpeta Imagenes para poner en ella, todas las graficas que vayan surgiendo del procesamiento de datos.