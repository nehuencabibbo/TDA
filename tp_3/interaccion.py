import sys
import hitting_set.backtracking as backtracking
import hitting_set.programacion_lineal_entera as pl_entera
import hitting_set.programacion_lineal as pl_aproximado
import hitting_set.greedy as greedy
from persistencia import *
from constantes import ERROR_ENTRADA_INVALIDA, NOMBRE_COMANDO, MENSAJE_RESULTADO, MENSAJE_EXPORTACION, DIRECTORIO_SALIDA, NOMBRE_ARCHIVO_SALIDA

"""
Módulo de funciones que procesan y manejan la entrada y salida del programa
"""

def iniciar_comandos():
    """
    Crea el diccionario con los comandos que se pueden ejecutar en el programa.
    Guarda como clave el nombre del comando y como valor la función que lo ejecuta.
    """
    return {
        "backtracking": backtracking.hitting_set,
        "pl_entera": pl_entera.hitting_set,
        "pl_aproximado": pl_aproximado.hitting_set,
        "greedy": greedy.hitting_set,
    }

def procesar_comando(comandos, datos):
    """
    Espera hasta recibir el nombre de un comando por entrada estándar hasta que finalice. 
    Procesa la entrada, verifica que el comando sea válido y lo ejecuta.
    """
    for entrada in sys.stdin:
        if not entrada.rstrip():
            print(ERROR_ENTRADA_INVALIDA)
            continue
        cmd = procesar_entrada_usuario(entrada)
        if cmd == "listar_algoritmos":
            listar_algoritmos(comandos)
            continue
        if cmd not in comandos:
            print(ERROR_ENTRADA_INVALIDA)
            continue
        ejecutar_comando(comandos[cmd], datos)

def listar_algoritmos(comandos):
    """
    Imprime los comandos disponibles para ejecutar en el programa
    """
    print("Los algoritmos diponibles para obtener el Hitting Set son:")
    for cmd in comandos:
        print(cmd)

def procesar_entrada_usuario(entrada):
    """
    Procesa la entrada del usuario para obtener el nombre del comando.
    """
    argumentos = entrada.split()
    cmd = argumentos.pop(NOMBRE_COMANDO).lower()
    return cmd

def ejecutar_comando(cmd, datos):
    """
    Ejecuta el comando elegiudo por el usuario con los datos previamente cargados
    y exporta el resultado a un archivo de texto
    """
    hitting_set = cmd(datos)
    cantidad_hs = len(hitting_set)
    print(f"{MENSAJE_RESULTADO} {cantidad_hs}")
    exportar_hitting_set(cantidad_hs, hitting_set)    

def exportar_hitting_set(cantidad_hs, hitting_set):
    """
    Exporta el resultado obtenido a un archivo de texto
    """
    crear_directorio_salida(DIRECTORIO_SALIDA)
    exportar_resultado(cantidad_hs, hitting_set, crear_ruta_salida(DIRECTORIO_SALIDA, NOMBRE_ARCHIVO_SALIDA))
    print(MENSAJE_EXPORTACION)
