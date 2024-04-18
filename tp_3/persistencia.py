from datetime import datetime
from constantes import FORMATO_FECHA, SEPARADOR
import csv
import os

"""
Módulo de funciones para menjar archivos
"""

def importar_datos(ruta):
    """
    Recibe la ruta a un archivos de texto con el set de datos, lo lee y crea los conjuntos 
    con los elementos correspondientes.
    """
    conjuntos = []
    with open(ruta, encoding="utf8",newline='') as reader:
        for linea in reader:
            c = set(linea.rstrip().split(","))
            conjuntos.append(c)
    return conjuntos

def exportar_datos(conjuntos, ruta):
    """
    Recibe un set de datos y una ruta de salida y escribe los datos en un archivo de texto
    """
    with open(ruta, "w", encoding="utf8", newline='') as writer:
        for conjunto in conjuntos:
            writer.write(f"{','.join(conjunto)}\n")

def exportar_resultado(cantidad, hitting_set, ruta):
    """
    Recibe un set de datos y una ruta de salida y escribe los datos en un archivo de texto
    """
    with open(ruta, "w", encoding="utf8", newline='') as writer:
        writer.write(f"Cantidad mínima: {cantidad} ({SEPARADOR.join(hitting_set)})")

def exportar_tiempos_ejecucion(resultados, ruta, encabezado):
    """
    Recibe un set de datos y una ruta de salida y escribe los datos en un archivo de texto
    """
    with open(ruta, "w", encoding="utf8", newline='') as datos:
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
