def planificar_entrenamiento(n, esfuerzo, energia):
    """
    Recibe la cantidad de días del plan de entrenamiento, una lista con los valores de
    los esfuerzos disponibles y otra lista con los valores de la energía disponible y 
    calcula la ganancia máxima para el plan de entrenamiento
	"""
    memoria = [[0 for _ in range(n)] for _ in range(n)]
    memoria[0] = [min(esfuerzo[n-1], energia[d]) for d in range(n)]

    for i in range(1,n):
        for d in range(n-i):
            memoria[i][d] = max(memoria[i-1][d+1] + min(esfuerzo[n-1-i], energia[d]), memoria[i-1][0])

    return memoria[n-1][0], memoria

def reconstruir_plan_entrenamiento(plan_entrenamiento):
    """
    Recibe la matriz del plan de entrenamiento con las ganancias 
    previamente calculadas y devuelve la secuencia reconstruída de entrenamientos y 
    descansos correspondiente.
	"""
    reconstruccion = []
    dias = len(plan_entrenamiento)
    d = 0
    for i in range(dias-1,-1,-1):
        if plan_entrenamiento[i][d] != plan_entrenamiento[i-1][0]:
            reconstruccion.append("Entreno")
            d+=1
            continue
        reconstruccion.append("Descanso")
        d=0

    return reconstruccion
