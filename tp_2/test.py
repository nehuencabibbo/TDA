import unittest
from planificar_entrenamiento import *
from persistencia import importar_datos

class TestGanaciaOptima(unittest.TestCase):

    def test_plan_tres_dias(self):
        ruta = "./datasets/00_datasets_curso/3.txt"
        optimo = 7
        dias, esfuerzo, energia = importar_datos(ruta)
        ganancia, plan = planificar_entrenamiento(dias, esfuerzo, energia)

        self.assertEqual(ganancia, optimo)
    
    def test_plan_diez_dias(self):
        ruta = "./datasets/00_datasets_curso/10.txt"
        optimo = 380
        dias, esfuerzo, energia = importar_datos(ruta)
        ganancia, plan = planificar_entrenamiento(dias, esfuerzo, energia)

        self.assertEqual(ganancia, optimo)
    
    def test_plan_diez_dias_bis(self):
        ruta = "./datasets/00_datasets_curso/10_bis.txt"
        optimo = 523
        dias, esfuerzo, energia = importar_datos(ruta)
        ganancia, plan = planificar_entrenamiento(dias, esfuerzo, energia)

        self.assertEqual(ganancia, optimo)
    
    def test_plan_diez_dias_entreno(self):
        ruta = "./datasets/00_datasets_curso/10_todo_entreno.txt"
        optimo = 860
        dias, esfuerzo, energia = importar_datos(ruta)
        ganancia, plan = planificar_entrenamiento(dias, esfuerzo, energia)

        self.assertEqual(ganancia, optimo)
    
    def test_plan_cincuenta_dias(self):
        ruta = "./datasets/00_datasets_curso/50.txt"
        optimo = 1870
        dias, esfuerzo, energia = importar_datos(ruta)
        ganancia, plan = planificar_entrenamiento(dias, esfuerzo, energia)

        self.assertEqual(ganancia, optimo)
    
    def test_plan_cincuenta_dias_bis(self):
        ruta = "./datasets/00_datasets_curso/50_bis.txt"
        optimo = 2136
        dias, esfuerzo, energia = importar_datos(ruta)
        ganancia, plan = planificar_entrenamiento(dias, esfuerzo, energia)

        self.assertEqual(ganancia, optimo)
    
    def test_plan_cien_dias(self):
        ruta = "./datasets/00_datasets_curso/100.txt"
        optimo = 5325
        dias, esfuerzo, energia = importar_datos(ruta)
        ganancia, plan = planificar_entrenamiento(dias, esfuerzo, energia)

        self.assertEqual(ganancia, optimo)
    
    def test_plan_quinientos_dias(self):
        ruta = "./datasets/00_datasets_curso/500.txt"
        optimo = 27158
        dias, esfuerzo, energia = importar_datos(ruta)
        ganancia, plan = planificar_entrenamiento(dias, esfuerzo, energia)

        self.assertEqual(ganancia, optimo)
    
    def test_plan_mil_dias(self):
        ruta = "./datasets/00_datasets_curso/1000.txt"
        optimo = 54021
        dias, esfuerzo, energia = importar_datos(ruta)
        ganancia, plan = planificar_entrenamiento(dias, esfuerzo, energia)

        self.assertEqual(ganancia, optimo)
    
    def test_plan_cinco_mil_dias(self):
        ruta = "./datasets/00_datasets_curso/5000.txt"
        optimo = 279175
        dias, esfuerzo, energia = importar_datos(ruta)
        ganancia, plan = planificar_entrenamiento(dias, esfuerzo, energia)

        self.assertEqual(ganancia, optimo)
    
    def test_mas_esfuerzo_que_energia(self):
        dias = 3
        esfuerzo = [200, 50, 100]
        energia = [100, 10, 1]
        optimo = 200
        ganancia, plan = planificar_entrenamiento(dias, esfuerzo, energia)

        self.assertEqual(ganancia, optimo)
    
    def test_mas_energia_que_esfuerzo(self):
        dias = 3
        esfuerzo = [100, 10, 1]
        energia = [200, 50, 10]
        optimo = 111
        ganancia, plan = planificar_entrenamiento(dias, esfuerzo, energia)

        self.assertEqual(ganancia, optimo)
    
    def test_mismo_esfuerzo_que_energia(self):
        dias = 3
        esfuerzo = [10, 5, 1]
        energia = [10, 5, 1]
        optimo = 16
        ganancia, plan = planificar_entrenamiento(dias, esfuerzo, energia)

        self.assertEqual(ganancia, optimo)
    
    def test_los_jugadores_no_se_cansan(self):
        dias = 5
        esfuerzo = [10, 100, 100, 500, 20]
        energia = [100, 100, 100, 100, 100]
        optimo = 330
        ganancia, plan = planificar_entrenamiento(dias, esfuerzo, energia)

        self.assertEqual(ganancia, optimo)
    
    def test_los_jugadores_se_agotan(self):
        dias = 5
        esfuerzo = [10, 10, 5, 25, 1]
        energia = [100, 0, 0, 0, 0]
        optimo = 35
        ganancia, plan = planificar_entrenamiento(dias, esfuerzo, energia)

        self.assertEqual(ganancia, optimo)
    
    def test_mismo_esfuerzo_todos_los_dias(self):
        dias = 5
        esfuerzo = [100, 100, 100, 100, 100]
        energia = [50, 40, 30, 20, 10]
        optimo = 180
        ganancia, plan = planificar_entrenamiento(dias, esfuerzo, energia)

        self.assertEqual(ganancia, optimo)


if __name__ == '__main__':
    unittest.main()
