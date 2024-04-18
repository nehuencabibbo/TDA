import time

"""
Funciones para medir el tiempo de ejecución
"""

def medir_tiempo_ejecucion(conjuntos, funcion_hitting_set):
    """
    Recibe los datos de los conjuntos y la función para contruir el hitting set 
    y mide el tiempo de ejecución de la función seleccionada
    """
    inicio = time.time()
    funcion_hitting_set(conjuntos)
    fin = time.time()
    return (fin-inicio)*1000

def promediar_tiempos_ejecucion(conjuntos, funcion_hitting_set, iteraciones):
    """
    Recibe los datos de los conjuntos, la función para construir el hitting set y 
    un número de iteraciones y ejecuta la función elegida para medir y promediar
    su tiempo de ejecución.
    """
    tiempos = 0
    for _ in range(iteraciones):
        tiempos += medir_tiempo_ejecucion(conjuntos, funcion_hitting_set)
    return tiempos / iteraciones
