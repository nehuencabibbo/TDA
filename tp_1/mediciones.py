import time
from analisis_rival import analizar_rivales

"""
Funciones para medir el tiempo de ejecución
"""

def medir_tiempo_ejecucion(rivales):
	"""
	Recibe los datos de los videos de rivales y mide el tiempo de ejecución 
	de la función analizar_rivales
	"""
	inicio = time.time()
	analizar_rivales(rivales)
	fin = time.time()
	return (fin-inicio)*1000

def promediar_tiempos_ejecucion(rivales, iteraciones):
	"""
	Recibe los datos de los videos de rivales y un número de iteraciones 
	y ejecuta la función analizar_rivales para medir y promediar
	su tiempo de ejecución.
	"""
	tiempos = 0
	for _ in range(iteraciones):
		tiempos += medir_tiempo_ejecucion(rivales)
	return tiempos / iteraciones
