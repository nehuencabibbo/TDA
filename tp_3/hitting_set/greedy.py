def calcular_frecuencias(conjuntos):
    """
    Calcula la cantidad de apariciones de cada jugador entre todos los conjuntos
    """
    frecuencias = {}
    for conjunto in conjuntos:
        for jugador in conjunto:
            frecuencias[jugador] = frecuencias.get(jugador, 0) + 1
    return frecuencias

def buscar_jugador_mas_pedido(conjuntos):
    """
    Selecciona el jugador que más veces aparece entre todos los conjuntos recibidos por parámetro.
    """
    frecuencias = calcular_frecuencias(conjuntos)
    return max(frecuencias, key=frecuencias.get)

def conjuntos_cubiertos(jugador, conjuntos):
    """
    Recibe el ombre d eun jugador y la lista de conjuntos y devuelve una lista con todos los
    conjuntos a los que pertence el jugador 
    """
    cubiertos = []
    for conjunto in conjuntos:
        if jugador not in conjunto: 
            continue
        cubiertos.append(conjunto)
    return cubiertos

def hitting_set(conjuntos):
    """
    Recibe una lista de conjuntos y busca un Hitting-Set aproximado usando la técnica Greedy
    """
    conjuntos_restantes = set(frozenset(c) for c in conjuntos)
    hitting_set = set()
    while conjuntos_restantes:
        jugador = buscar_jugador_mas_pedido(conjuntos_restantes)
        hitting_set.add(jugador)
        cubiertos = conjuntos_cubiertos(jugador, conjuntos_restantes)
        conjuntos_restantes.difference_update(cubiertos)
    return hitting_set
