from analisis_rival import analizar_rivales
from persistencia import *
from constantes import *
import sys

"""
Función principal del programa
"""

def main():
	if len(sys.argv) < CANTIDAD_ARGUMENTOS:
		print(MENSAJE_ERROR)
		return

	datos = importar_dataset(sys.argv[DATOS])
	tiempo, orden_rivales = analizar_rivales(datos)	
	print(f"{MENSAJE_TIEMPO} {tiempo}")

	crear_directorio_salida(DIRECTORIO_SALIDA)
	exportar_dataset(orden_rivales, crear_ruta_salida(DIRECTORIO_SALIDA, NOMBRE_ARCHIVO_SALIDA))
	print(MENSAJE_EXPORTACION)

if __name__ == "__main__":
	main()
