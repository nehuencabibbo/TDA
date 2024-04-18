import random

"""
Módulo de funciones para generar set de datos con valores aleatorios
"""

def generar_valores_aleatorios(min_si=1, max_si=100, min_ai=1, max_ai=100):
    """
    Genera valores aleatorios para S_i y A_i en los rango definidos por los 
    parámetros opcionales min y max.
    """
    s_i = random.randint(min_si, max_si)
    a_i = random.randint(min_ai, max_ai)
    return {"S_i": s_i, "A_i": a_i}

def generar_dataset(n, min_si=1, max_si=100, min_ai=1, max_ai=100):
    """
    Crea un set de datos aleatorios con n elementos.
    Recibe por parámetro la cantidad de elementos que se generan (n) y opcionalmente
    valores mínimo y máximo para definir el rango de los valores generados para A_i y S_i
    """
    return [generar_valores_aleatorios(min_si, max_si, min_ai, max_ai) for _ in range(n)]