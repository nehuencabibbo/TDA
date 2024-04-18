import unittest
import networkx as nx
import hitting_set.programacion_lineal_entera as pl_entera
from hitting_set.validacion import transformar_entrada, certificador_eficiente_hs, certificador_eficiente_vc

class TestHittingReduccion(unittest.TestCase):

    def test_cinco_elementos(self):
        ruta = "./datasets/02_tests/5.txt"
        grafo = nx.read_adjlist(ruta)
        _, conjuntos = transformar_entrada(grafo)
        min_cantidad = 2
        hitting_set = pl_entera.hitting_set(conjuntos)

        self.assertTrue(certificador_eficiente_hs(hitting_set, min_cantidad, conjuntos))
        self.assertTrue(certificador_eficiente_vc(hitting_set, min_cantidad, grafo))

    def test_siete_elementos(self):
        ruta = "./datasets/02_tests/7.txt"
        grafo = nx.read_adjlist(ruta)
        _, conjuntos = transformar_entrada(grafo)
        min_cantidad = 3
        hitting_set = pl_entera.hitting_set(conjuntos)

        self.assertTrue(certificador_eficiente_hs(hitting_set, min_cantidad, conjuntos))
        self.assertTrue(certificador_eficiente_vc(hitting_set, min_cantidad, grafo))
    
    def test_diez_elementos(self):
        ruta = "./datasets/02_tests/10.txt"
        grafo = nx.read_adjlist(ruta)
        _, conjuntos = transformar_entrada(grafo)
        min_cantidad = 4
        hitting_set = pl_entera.hitting_set(conjuntos)

        self.assertTrue(certificador_eficiente_hs(hitting_set, min_cantidad, conjuntos))
        self.assertTrue(certificador_eficiente_vc(hitting_set, min_cantidad, grafo))
    
    def test_quince_elementos(self):
        ruta = "./datasets/02_tests/15.txt"
        grafo = nx.read_adjlist(ruta)
        _, conjuntos = transformar_entrada(grafo)
        min_cantidad = 7
        hitting_set = pl_entera.hitting_set(conjuntos)

        self.assertTrue(certificador_eficiente_hs(hitting_set, min_cantidad, conjuntos))
        self.assertTrue(certificador_eficiente_vc(hitting_set, min_cantidad, grafo))
    
    if __name__ == '__main__':
        unittest.main()    
