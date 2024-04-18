"""
Funciones para analizar los videos de rivales
"""

def calcular_tiempo_total_de_analisis(videos_rivales):
	"""
	Recibe una lista con los datos de los rivales ordenados
	y calcula su tiempo total de análisis
	"""
	fin_scaloni = 0
	fin_analisis = 0
	for video in videos_rivales:
		fin_scaloni += video["S_i"]
		fin_ayudante = fin_scaloni + video["A_i"]
		if fin_analisis < fin_ayudante:
			fin_analisis = fin_ayudante
	return fin_analisis

def ordenar_rivales(videos_rivales):
	"""
	Recibe una lista con los datos de los rivales y los ordena de mayor a menor 
	por los valores de a_i
	"""
	videos_ordenados = sorted(videos_rivales, key=lambda t:t["A_i"], reverse=True)
	return videos_ordenados

def analizar_rivales(videos_rivales):
	"""
	Recibe una lista con los datos de los rivales, los ordena y calcula 
	el tiempo óptimo de análisis
	"""
	videos_ordenados = ordenar_rivales(videos_rivales)
	tiempo_analisis = calcular_tiempo_total_de_analisis(videos_ordenados)
	return tiempo_analisis, videos_ordenados
