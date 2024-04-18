def bodegon(w, grupos):
    sol_parcial = []
    mejor_sol = []
    _bodegon(w, grupos, sol_parcial, mejor_sol, 0)
    return mejor_sol[0]

def _bodegon(w, grupos, sol_parcial, mejor_sol, indice):
    #Me pase de largo
    if indice > len(grupos):
        return 0 
     
    #Me pase de cantidad de elementos
    if sum(sol_parcial) > w:
        return 0

    #Llegue al final
    if len(grupos) == indice:
        if sum(sol_parcial) > sum(mejor_sol):
            mejor_sol = sol_parcial

            return sum(mejor_sol)
        
    #Considero mi elemento actual
    sol_parcial.append(grupos[indice])

    if _bodegon(w, grupos, sol_parcial, mejor_sol, indice + 1) == w:
        return w
    
    sol_parcial.pop()

    #Se retorna directamente porque el mejor resultado de haber considerado el elemento 
    #ya se tiene en cuenta en la variable "mejor asignacion"
    return _bodegon(w, grupos, sol_parcial, mejor_sol, indice + 1)


def bodegon(W, vector_p, indice, asignacion_actual, mejor_asignacion):
    if sum(asignacion_actual) > W:
        return 0

    if sum(asignacion_actual) == W:
        return sum(asignacion_actual)

    if grupo == len(vector_p) and (mejor_asignacion == [] or sum(asignacion_actual) > sum(mejor_asignacion)):
        mejor_asignacion = list(asignacion_actual)

    if grupo == len(vector_p):
        return 0

    asignacion_actual.append(vector_p[indice])

    incluir = bodegon(W, vector_p, indice + 1, asignacion_actual, mejor_asignacion)
    asignacion_actual.pop()

    excluir = bodegon(W, vector_p, indice + 1, asignacion_actual, mejor_asignacion)

    return max(incluir, excluir)
 
        
    

