import pulp as pl

def hitting_set(conjuntos):
    """
    Recibe una lista de conjuntos y resuelve de forma óptima el problema de encontrar 
    un Hitting-Set mínimo usando Programación Lineal Entera
    """
    jugadores = set.union(*conjuntos)
    problema = pl.LpProblem("hitting_set", pl.LpMinimize)     
    hs = {jugador:pl.LpVariable(f"{jugador}", cat="Binary") for jugador in jugadores}           
    for conjunto in conjuntos:
        variables = []
        for jugador in conjunto:
            variables.append(hs[jugador])
        problema += pl.lpSum(variables) >= 1
    problema += pl.lpSum(hs.values())
    problema.solve(pl.PULP_CBC_CMD(msg=False))
    return [j for j in hs.keys() if pl.value(hs[j]) > 0]
