from constantes import *
from persistencia import *
from planificar_entrenamiento import planificar_entrenamiento, reconstruir_plan_entrenamiento
import sys

"""
Función principal del programa
"""

def main():
	if len(sys.argv) < CANTIDAD_ARGUMENTOS:
		print(MENSAJE_ERROR)
		return

	dias, esfuerzo, energia = importar_datos(sys.argv[DATOS])
	ganancia, plan_entrenamiento = planificar_entrenamiento(dias, esfuerzo, energia)	
	plan_reconstruido = reconstruir_plan_entrenamiento(plan_entrenamiento)
	print(f"{MENSAJE_GANANCIA} {ganancia}")
	
	crear_directorio_salida(DIRECTORIO_SALIDA)
	exportar_plan_resultante(dias, ganancia, plan_reconstruido, crear_ruta_salida(DIRECTORIO_SALIDA, NOMBRE_ARCHIVO_SALIDA))
	print(MENSAJE_EXPORTACION)

if __name__ == "__main__":
	main()
