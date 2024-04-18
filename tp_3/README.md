# Trabajo Práctico 3: Problemas NP-Completos

En este directorio se encuentra el código fuente del Trabajo Práctico 3 de la materia 75.29 Teoría de Algoritmos, curso Buchwald-Genender

- Los detalles del enunciado, consigna y especificaciones están disponibles [en este link](https://github.com/algoritmos-rw/tda_bg/blob/master/tps/2023_2/tp3.md).

- Puede accederse al informe desde [este link](Informe.pdf)

---

## Instrucciones de ejecución

### Programa principal

El programa está escrito en Python y puede ejecutarse desde la terminal con el siguiente comando:

```
$ python3 main.py <ruta_archivo_entrada>
```

Recibe como parámetro la ruta a un archivo de texto con el set de datos que se quiera utilizar. El archivo de entrada debe adecuarse a los ejemplos provistos por el curso. El formato debe ser acorde al siguiente ejemplo:

```
Barcon't,Cuti Romero,Colidio,Casco
Colo Barco,Wachoffisde Abila,Messi,Casco,Armani,Chiquito Romero
Barcon't,Wachoffisde Abila,Colidio,Casco
Messi,Cuti Romero,Casco,Pezzella
Colo Barco,Messi,Cuti Romero
``` 

Donde cada línea tiene un conjunto, con sus elementos separados por coma.

El programa se quedará esperando instrucciones por entrada del usuario. Los comandos disponibles son:

- `backtracking`
- `pl_entera`
- `pl_aproximado`
- `greedy`
- `listar_algoritmos`

Cada comando ejecuta el algoritmo correspondiente y `listar_algoritmos` muestra por terminal el listado de algoritmos disponibles.

Al finalizar la ejecución del algoritmo, se imprime en la terminal el valor del *Hitting-Set* calculado y la solución se exporta al directorio `./salida`

El programa finaliza con `Ctrl+D`

---

### Dependencias:

- Los algoritmos de Programación Lineal requieren de la librería [Pulp](https://coin-or.github.io/pulp/)
- Los tests de reducción requieren de la librería [Networkx](https://networkx.org/)

---

### Tests

Se incluye un conjunto de pruebas con los ejemplos provistos por el curso y algunos casos adicionales, que pueden ejecutarse desde el directorio `tp_3` con el siguiente comando:

```
$ python3 -m unittest -v test_<nombre_del_test>.py
```

---
