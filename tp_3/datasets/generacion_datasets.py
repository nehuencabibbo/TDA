import random

"""
Módulo de funciones para generar set de datos con valores aleatorios
"""

def generar_dataset(n, jugadores, min=1, max=10, max_var=50):
    """
    Crea un set de datos aleatorios con n subconjuntos.
    Recibe por parámetro la cantidad de subconjuntos que se generan (n), una lista de jugadores
    y opcionalmente valores mínimo y máximo para definir la cantidad de elementos de cada subconjunto
    """
    conjuntos = []
    for _ in range(n):
        subconjunto = set(jugadores[random.randint(0, max_var)] for _ in range(random.randint(min, max)))
        conjuntos.append(subconjunto)
    return conjuntos
    