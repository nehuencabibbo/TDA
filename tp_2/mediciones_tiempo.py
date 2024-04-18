import time
from planificar_entrenamiento import planificar_entrenamiento

"""
Funciones para medir el tiempo de ejecución
"""

def medir_tiempo_ejecucion(dias, esfuerzo, energia):
    """
    Recibe los datos para la planificacion del entrenamiento y mide el tiempo de ejecución 
    de la función planificar entrenamiento
    """
    inicio = time.time()
    planificar_entrenamiento(dias, esfuerzo, energia)
    fin = time.time()
    return (fin-inicio)*1000

def promediar_tiempos_ejecucion(dias, esfuerzo, energia, iteraciones):
    """
    Recibe los datos para la planificacion del entrenamiento y un número de iteraciones 
    y ejecuta la función planificar entrenamiento para medir y promediar
    su tiempo de ejecución.
    """
    tiempos = 0
    for _ in range(iteraciones):
        tiempos += medir_tiempo_ejecucion(dias, esfuerzo, energia)
    return tiempos / iteraciones
