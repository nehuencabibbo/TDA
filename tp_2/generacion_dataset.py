import random

"""
Módulo de funciones para generar set de datos con valores aleatorios
"""

def generar_valores_aleatorios(min_ei=1, max_ei=100, min_si=1, max_si=100):
    """
    Genera valores aleatorios para S_i y A_i en los rango definidos por los 
    parámetros opcionales min y max.
    """
    e_i = random.randint(min_ei, max_ei)
    s_i = random.randint(min_si, max_si)
    return e_i, s_i

def generar_dataset(n, min_ei=1, max_ei=100, min_si=1, max_si=100):
    """
    Crea un set de datos aleatorios con n elementos.
    Recibe por parámetro la cantidad de elementos que se generan (n) y opcionalmente
    valores mínimo y máximo para definir el rango de los valores generados para e_i y s_i
    """
    esfuerzo = []
    energia = []
    for _ in range(n):
        e_i, s_i = generar_valores_aleatorios(min_ei, max_ei, min_si, max_si)
        esfuerzo.append(e_i)
        energia.append(s_i)
    energia = sorted(energia, reverse=True)
    return esfuerzo, energia
    