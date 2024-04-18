from constantes import FORMATO_FECHA
from datetime import datetime
import csv
import os

"""
Módulo de funciones para importar y exportar set de datos en archivos de texto
"""

def importar_dataset(ruta):
	"""
	Recibe una ruta a un archivo de texto, lo lee y crear los set de datos
	a partir del archivo
	"""
	resultado = []
	with open(ruta, newline='') as datos:
		reader = csv.DictReader(datos, delimiter=',')
		for linea in reader:
			resultado.append({"S_i": int(linea["S_i"]), "A_i": int(linea["A_i"])})
	return resultado

def exportar_dataset(dataset, ruta, encabezado=["S_i", "A_i"]):
	"""
	Recibe un set de datos y una ruta de salida y escribe los datos en un archivo de texto
	"""
	with open(ruta, "w", newline='') as datos:
		writer = csv.DictWriter(datos, delimiter=',', fieldnames=encabezado)
		writer.writeheader()
		for elemento in dataset:
			writer.writerow(elemento)

def crear_directorio_salida(dir_salida):
	"""
	Recibe una ruta a un directorio, evalúa su existencia y si no existe, lo crea
	"""
	if not os.path.exists(dir_salida):
		os.makedirs(dir_salida)

def crear_ruta_salida(dir_salida, nombre_archivo):
	"""
	Recibe la ruta a un directorio y el nombre del archivo y crea la ruta 
	completa con el timestamp en el que fue creado
	"""
	fecha = datetime.now().strftime(FORMATO_FECHA)
	return f"./{dir_salida}/{fecha}_{nombre_archivo}"
