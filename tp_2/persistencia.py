from datetime import datetime
import csv
import os

FORMATO_FECHA = "%Y-%m-%d_%H%M%S"
DIAS = 0
ESFUERZO = 1
SEPARADOR = ", "

def importar_datos(ruta):
    """
    Recibe una ruta a un archivo de texto, lo lee y crear los set de datos
    a partir del archivo
    """
    datos = []
    with open(ruta, newline='') as reader:
        for linea in reader:
            datos.append(int(linea.rstrip()))

    dias = datos[DIAS]
    esfuerzo = datos[ESFUERZO:dias+1]
    energia = datos[dias+1:]

    return dias, esfuerzo, energia

def exportar_datos(dias, esfuerzo, energia, ruta):
    """
    Recibe un set de datos y una ruta de salida y escribe los datos en un archivo de texto
    """
    with open(ruta, "w", newline='') as writer:
        writer.write(f"{dias}\n")
        for e_i in esfuerzo:
            writer.write(f"{e_i}\n")
        for s_i in energia:
            writer.write(f"{s_i}\n")

def exportar_plan_resultante(dias, ganancia, plan_entrenamiento, ruta):
    """
    Recibe un set de datos y una ruta de salida y escribe los datos en un archivo de texto
    """
    with open(ruta, "w", newline='') as writer:
        writer.write(f"Dias de entrenamiento: {dias}\n")
        writer.write(f"Ganancia maxima: {ganancia}\n")
        writer.write(f"Plan de entrenamiento: {SEPARADOR.join(plan_entrenamiento)}\n")

def exportar_tiempos_ejecucion(resultados, ruta, encabezado):
    """
    Recibe un set de datos y una ruta de salida y escribe los datos en un archivo de texto
    """
    with open(ruta, "w", newline='') as datos:
        writer = csv.DictWriter(datos, delimiter=',', fieldnames=encabezado)
        writer.writeheader()
        for elemento in resultados:
            writer.writerow(elemento)

def crear_directorio_salida(dir_salida):
    """
    Recibe una ruta a un directorio, evalúa su existencia y si no existe, lo crea
    """
    if not os.path.exists(dir_salida):
        os.makedirs(dir_salida)

def crear_ruta_salida(dir_salida, nombre_archivo):
    """
    Recibe la ruta a un directorio y el nombre del archivo y crea la ruta 
    completa con el timestamp en el que fue creado
    """
    fecha = datetime.now().strftime(FORMATO_FECHA)
    return f"./{dir_salida}/{fecha}_{nombre_archivo}"
