import unittest
from persistencia import importar_datos
from hitting_set.backtracking import hitting_set
from hitting_set.validacion import certificador_eficiente_hs

class TestHittingSetOptimoBacktracking(unittest.TestCase):

    def test_cinco_conjuntos(self):
        ruta = "./datasets/00_datasets_curso/5.txt"
        cantidad_minima = 2
        conjuntos = importar_datos(ruta)
        min_hitting_set = hitting_set(conjuntos)        

        self.assertTrue(certificador_eficiente_hs(min_hitting_set, cantidad_minima, conjuntos))

    def test_siete_conjuntos(self):
        ruta = "./datasets/00_datasets_curso/7.txt"
        cantidad_minima = 2
        conjuntos = importar_datos(ruta)
        min_hitting_set = hitting_set(conjuntos)        

        self.assertTrue(certificador_eficiente_hs(min_hitting_set, cantidad_minima, conjuntos))
    
    def test_diez_conjuntos_pocos(self):
        ruta = "./datasets/00_datasets_curso/10_pocos.txt"
        cantidad_minima = 3
        conjuntos = importar_datos(ruta)
        min_hitting_set = hitting_set(conjuntos)        

        self.assertTrue(certificador_eficiente_hs(min_hitting_set, cantidad_minima, conjuntos))
    
    def test_diez_conjuntos_todos(self):
        ruta = "./datasets/00_datasets_curso/10_todos.txt"
        cantidad_minima = 10
        conjuntos = importar_datos(ruta)
        min_hitting_set = hitting_set(conjuntos)        

        self.assertTrue(certificador_eficiente_hs(min_hitting_set, cantidad_minima, conjuntos))
    
    def test_diez_conjuntos_varios(self):
        ruta = "./datasets/00_datasets_curso/10_varios.txt"
        cantidad_minima = 6
        conjuntos = importar_datos(ruta)
        min_hitting_set = hitting_set(conjuntos)        

        self.assertTrue(certificador_eficiente_hs(min_hitting_set, cantidad_minima, conjuntos))
    
    def test_quince_conjuntos(self):
        ruta = "./datasets/00_datasets_curso/15.txt"
        cantidad_minima = 4
        conjuntos = importar_datos(ruta)
        min_hitting_set = hitting_set(conjuntos)        

        self.assertTrue(certificador_eficiente_hs(min_hitting_set, cantidad_minima, conjuntos))
    
    def test_veinte_conjuntos(self):
        ruta = "./datasets/00_datasets_curso/20.txt"
        cantidad_minima = 5
        conjuntos = importar_datos(ruta)
        min_hitting_set = hitting_set(conjuntos)        

        self.assertTrue(certificador_eficiente_hs(min_hitting_set, cantidad_minima, conjuntos))
    
    def test_cincuenta_conjuntos(self):
        ruta = "./datasets/00_datasets_curso/50.txt"
        cantidad_minima = 6
        conjuntos = importar_datos(ruta)
        min_hitting_set = hitting_set(conjuntos)        

        self.assertTrue(certificador_eficiente_hs(min_hitting_set, cantidad_minima, conjuntos))
    
    def test_setenta_y_cinco_conjuntos(self):
        ruta = "./datasets/00_datasets_curso/75.txt"
        cantidad_minima = 8
        conjuntos = importar_datos(ruta)
        min_hitting_set = hitting_set(conjuntos)        

        self.assertTrue(certificador_eficiente_hs(min_hitting_set, cantidad_minima, conjuntos))
    
    def test_cien_conjuntos(self):
        ruta = "./datasets/00_datasets_curso/100.txt"
        cantidad_minima = 9
        conjuntos = importar_datos(ruta)
        min_hitting_set = hitting_set(conjuntos)        

        self.assertTrue(certificador_eficiente_hs(min_hitting_set, cantidad_minima, conjuntos))
    
    def test_doscientos_conjuntos(self):
        ruta = "./datasets/00_datasets_curso/200.txt"
        cantidad_minima = 9
        conjuntos = importar_datos(ruta)
        min_hitting_set = hitting_set(conjuntos)        

        self.assertTrue(certificador_eficiente_hs(min_hitting_set, cantidad_minima, conjuntos))
    
    if __name__ == '__main__':
        unittest.main()    
