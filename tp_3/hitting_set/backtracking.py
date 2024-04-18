def _hitting_set(conjuntos, solucion_parcial, mejor_solucion, indice):
    """
    Resuelve de forma óptima el problema de 
    encontrar un Hitting-Set mínimo usando backtracking
    """ 
    if len(solucion_parcial) > len(conjuntos):
        return mejor_solucion
    
    if mejor_solucion and (len(solucion_parcial) >= len(mejor_solucion)):
        return mejor_solucion 

    if indice >= len(conjuntos):
        if not mejor_solucion or len(solucion_parcial) < len(mejor_solucion):
            return solucion_parcial.copy()
        return mejor_solucion
    
    conjunto_actual = conjuntos[indice]    
    if solucion_parcial.intersection(conjunto_actual):
        return _hitting_set(conjuntos, solucion_parcial, mejor_solucion, indice+1)

    for jugador in conjunto_actual:
        if jugador in solucion_parcial:
            continue
        solucion_parcial.add(jugador)
        mejor_solucion = _hitting_set(conjuntos, solucion_parcial, mejor_solucion, indice+1)
        solucion_parcial.remove(jugador)    
    return mejor_solucion

def hitting_set(conjuntos):
    """
    Recibe una lista de conjuntos y resuelve de forma óptima el problema de 
    encontrar un Hitting-Set mínimo usando backtracking
    """
    return _hitting_set(conjuntos, set(), set(), 0)
