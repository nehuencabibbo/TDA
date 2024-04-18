import networkx as nx

ORIGEN = 0
DESTINO = 1

def crear_conjuntos(aristas):
    """
    Recibe una lista de aristas, crea un conjunto por cada una y agrega los vértices 
    como elementos del conjunto
    """
    conjuntos = []
    for arista in aristas:
        conjuntos.append(set(arista))
    return conjuntos

def transformar_entrada(grafo:nx.Graph):
    """
    A partir de un grafo, transforma la entrada requerida para resolver el problema de Vertex Cover,
    en una entrada válida para el problema de Hitting-Set
    """
    elementos = list(grafo.nodes)
    aristas = grafo.edges
    conjuntos = crear_conjuntos(aristas)
    return elementos, conjuntos    

def es_vertex_cover(elementos, grafo:nx.Graph):
    """
    Recibe un conjunto de elementos y un grafo, valida que el conjunto sea un Vertex Cover
    """
    aristas = grafo.edges
    for e in elementos:
        aristas = [a for a in aristas if e != a[ORIGEN] and e != a[DESTINO]]
    return not aristas

def certificador_eficiente_vc(vertex_cover, k, grafo):
    """
    Recibe una solución para el problema de Vertex Cover, un grafo y un entero positivo k,
    verifica que la solución sea válida, es decir que tenga un número de elementos menor o igual a k
    y que cubra todas las aristas del grafo
    """ 
    return len(vertex_cover) <= k and es_vertex_cover(vertex_cover, grafo)

def es_hitting_set(hitting_set, subconjuntos):
    """
    Recibe un conjunto de elementos y una lista de conjuntos y valida que sea un Hitting-Set
    """ 
    for sc in subconjuntos:
        if sc.isdisjoint(hitting_set):
            return False        
    return True

def certificador_eficiente_hs(hitting_set, k, subconjuntos):
    """
    Recibe una solución para el problema de Hitting-Set, un grafo y un entero positivo k,
    verifica que la solución sea válida, es decir que tenga un número de elementos menor o igual a k
    y que cubra todas las aristas del grafo
    """
    return len(hitting_set) <= k and es_hitting_set(hitting_set, subconjuntos)

def cumple_cota_aproximacion(aproximado, optimo, cota):
    """
    Recibe una solución óptima y una aproximada al problema y una cota y verifica
    que la relación entre ambas soluciones sea a lo sumo la cota definida
    """
    return len(aproximado)/len(optimo) <= cota
