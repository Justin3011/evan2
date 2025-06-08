#Evaluacion 2 DRY7122 JUSTIN
Programacion y redes virtualizadas (SDN-NFV)


**Nombre del estudiante:** Justin Hernandez 
**Fecha:** 7 de junio 2025

Este script utiliza la API publica de [OpenRouteService](https://openrouteservice.org) para cumplir los siguientes requerimientos:

- Solicita ingresar al usuario la ciudad de origen y la ciudad de destino (santiago/ovalle)
- Realiza una consulta a la API de rutas ('/directions/driving-car/geojson')
- Calcula: 
	- distancia total de kilometros(con dos decimales)
	- duracion del viaje (en minutos)
	- estimacion de combustible requerido (en litros)
- Imprime las instrucciones del viaje (la narrativa), en español
- Permite salir del programa escribiendo '"q"'

#Estos son los requisitos

- python3
- modulo 'requests' (apt install)

#Ejecucion

'''bash
python3 evan2.py
