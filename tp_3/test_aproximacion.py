import unittest
from persistencia import importar_datos
import hitting_set.programacion_lineal_entera as pl_entera
import hitting_set.programacion_lineal as pl
from hitting_set.validacion import es_hitting_set, cumple_cota_aproximacion

class TestHittingSetPLAproximado(unittest.TestCase):

    def test_cinco_conjuntos(self):
        ruta = "./datasets/00_datasets_curso/5.txt"
        conjuntos = importar_datos(ruta)
        b = len(max(conjuntos, key=len))
        optimo = pl_entera.hitting_set(conjuntos)        
        aproximado = pl.hitting_set(conjuntos)

        self.assertTrue(es_hitting_set(aproximado, conjuntos))
        self.assertTrue(cumple_cota_aproximacion(aproximado, optimo, b))

    def test_siete_conjuntos(self):
        ruta = "./datasets/00_datasets_curso/7.txt"
        conjuntos = importar_datos(ruta)
        b = len(max(conjuntos, key=len))
        optimo = pl_entera.hitting_set(conjuntos)        
        aproximado = pl.hitting_set(conjuntos)

        self.assertTrue(es_hitting_set(aproximado, conjuntos))
        self.assertTrue(cumple_cota_aproximacion(aproximado, optimo, b))
    
    def test_diez_conjuntos_pocos(self):
        ruta = "./datasets/00_datasets_curso/10_pocos.txt"
        conjuntos = importar_datos(ruta)
        b = len(max(conjuntos, key=len))
        optimo = pl_entera.hitting_set(conjuntos)        
        aproximado = pl.hitting_set(conjuntos)

        self.assertTrue(es_hitting_set(aproximado, conjuntos))
        self.assertTrue(cumple_cota_aproximacion(aproximado, optimo, b))
    
    def test_diez_conjuntos_todos(self):
        ruta = "./datasets/00_datasets_curso/10_todos.txt"
        conjuntos = importar_datos(ruta)
        b = len(max(conjuntos, key=len))
        optimo = pl_entera.hitting_set(conjuntos)        
        aproximado = pl.hitting_set(conjuntos)

        self.assertTrue(es_hitting_set(aproximado, conjuntos))
        self.assertTrue(cumple_cota_aproximacion(aproximado, optimo, b))
    
    def test_diez_conjuntos_varios(self):
        ruta = "./datasets/00_datasets_curso/10_varios.txt"
        conjuntos = importar_datos(ruta)
        b = len(max(conjuntos, key=len))
        optimo = pl_entera.hitting_set(conjuntos)        
        aproximado = pl.hitting_set(conjuntos)

        self.assertTrue(es_hitting_set(aproximado, conjuntos))
        self.assertTrue(cumple_cota_aproximacion(aproximado, optimo, b))
    
    def test_quince_conjuntos(self):
        ruta = "./datasets/00_datasets_curso/15.txt"
        conjuntos = importar_datos(ruta)
        b = len(max(conjuntos, key=len))
        optimo = pl_entera.hitting_set(conjuntos)        
        aproximado = pl.hitting_set(conjuntos)

        self.assertTrue(es_hitting_set(aproximado, conjuntos))
        self.assertTrue(cumple_cota_aproximacion(aproximado, optimo, b))
    
    def test_veinte_conjuntos(self):
        ruta = "./datasets/00_datasets_curso/20.txt"
        conjuntos = importar_datos(ruta)
        b = len(max(conjuntos, key=len))
        optimo = pl_entera.hitting_set(conjuntos)        
        aproximado = pl.hitting_set(conjuntos)

        self.assertTrue(es_hitting_set(aproximado, conjuntos))
        self.assertTrue(cumple_cota_aproximacion(aproximado, optimo, b))
    
    def test_cincuenta_conjuntos(self):
        ruta = "./datasets/00_datasets_curso/50.txt"
        conjuntos = importar_datos(ruta)
        b = len(max(conjuntos, key=len))
        optimo = pl_entera.hitting_set(conjuntos)        
        aproximado = pl.hitting_set(conjuntos)

        self.assertTrue(es_hitting_set(aproximado, conjuntos))
        self.assertTrue(cumple_cota_aproximacion(aproximado, optimo, b))
    
    def test_setenta_y_cinco_conjuntos(self):
        ruta = "./datasets/00_datasets_curso/75.txt"
        conjuntos = importar_datos(ruta)
        b = len(max(conjuntos, key=len))
        optimo = pl_entera.hitting_set(conjuntos)        
        aproximado = pl.hitting_set(conjuntos)

        self.assertTrue(es_hitting_set(aproximado, conjuntos))
        self.assertTrue(cumple_cota_aproximacion(aproximado, optimo, b))
    
    def test_cien_conjuntos(self):
        ruta = "./datasets/00_datasets_curso/100.txt"
        conjuntos = importar_datos(ruta)
        b = len(max(conjuntos, key=len))
        optimo = pl_entera.hitting_set(conjuntos)        
        aproximado = pl.hitting_set(conjuntos)

        self.assertTrue(es_hitting_set(aproximado, conjuntos))
        self.assertTrue(cumple_cota_aproximacion(aproximado, optimo, b))
    
    def test_doscientos_conjuntos(self):
        ruta = "./datasets/00_datasets_curso/200.txt"
        conjuntos = importar_datos(ruta)
        b = len(max(conjuntos, key=len))
        optimo = pl_entera.hitting_set(conjuntos)        
        aproximado = pl.hitting_set(conjuntos)

        self.assertTrue(es_hitting_set(aproximado, conjuntos))
        self.assertTrue(cumple_cota_aproximacion(aproximado, optimo, b))
    
    def test_trecientos_conjuntos(self):
        ruta = "./datasets/02_tests/300_conjuntos.txt"
        conjuntos = importar_datos(ruta)
        b = len(max(conjuntos, key=len))
        optimo = pl_entera.hitting_set(conjuntos)        
        aproximado = pl.hitting_set(conjuntos)

        self.assertTrue(es_hitting_set(aproximado, conjuntos))
        self.assertTrue(cumple_cota_aproximacion(aproximado, optimo, b))

    def test_quinientos_conjuntos(self):
        ruta = "./datasets/02_tests/500_conjuntos.txt"
        conjuntos = importar_datos(ruta)
        b = len(max(conjuntos, key=len))
        optimo = pl_entera.hitting_set(conjuntos)        
        aproximado = pl.hitting_set(conjuntos)

        self.assertTrue(es_hitting_set(aproximado, conjuntos))
        self.assertTrue(cumple_cota_aproximacion(aproximado, optimo, b))

    def test_mil_conjuntos(self):
        ruta = "./datasets/02_tests/1000_conjuntos.txt"
        conjuntos = importar_datos(ruta)
        b = len(max(conjuntos, key=len))
        optimo = pl_entera.hitting_set(conjuntos)        
        aproximado = pl.hitting_set(conjuntos)

        self.assertTrue(es_hitting_set(aproximado, conjuntos))
        self.assertTrue(cumple_cota_aproximacion(aproximado, optimo, b))
    
    if __name__ == '__main__':
        unittest.main()    
