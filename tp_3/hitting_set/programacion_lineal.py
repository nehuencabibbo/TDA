import pulp as pl

COTA_INFERIOR = 0
COTA_SUPERIOR = 1

def hitting_set(conjuntos):
    """
    Recibe una lista de conjuntos y resuelve de forma aproximada el problema de 
    encontrar un Hitting-Set mínimo usando Programación Lineal y redondeo
    """
    jugadores = set.union(*conjuntos)
    problema = pl.LpProblem("hitting_set", pl.LpMinimize)     
    hs = {jugador: pl.LpVariable(f"{jugador}", COTA_INFERIOR, COTA_SUPERIOR) for jugador in jugadores}     
    for conjunto in conjuntos:
        variables = []
        for jugador in conjunto:
            variables.append(hs[jugador])
        problema += pl.lpSum(variables) >= 1
    problema += pl.lpSum(hs.values())
    problema.solve(pl.PULP_CBC_CMD(msg=False))   
    b = len(max(conjuntos, key=len))
    return [j for j in hs.keys() if pl.value(hs[j]) >= 1/b]
