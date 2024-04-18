from constantes import *
from persistencia import *
from interaccion import iniciar_comandos, procesar_comando
import sys

"""
Función principal del programa
"""

def main():
	if len(sys.argv) < CANTIDAD_ARGUMENTOS:
		print(ERROR_CANTIDAD_PARAMETROS)
		return
	
	print(MENSAJE_INICIAL)
	conjuntos = importar_datos(sys.argv[DATOS])
	comandos = iniciar_comandos()
	procesar_comando(comandos, conjuntos)

if __name__ == "__main__":
	main()
