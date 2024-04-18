# Trabajo Práctico 2: Programación Dinámica

En este directorio se encuentra el código fuente del Trabajo Práctico 2 de la materia 75.29 Teoría de Algoritmos, curso Buchwald-Genender

- Los detalles del enunciado, consigna y especificaciones están disponibles [en este link](https://github.com/algoritmos-rw/tda_bg/blob/master/tps/2023_2/tp2.md).

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
3
1
5
4
10
2
2
``` 

Donde los datos se interpretan de la siguiente manera: 
- La primera línea indica el valor correspondiente a la cantidad de días consideradods ($n$).
- Las siguientes $n$ líneas indican las ganancias de cada día ($e_i$).
- Las últimas $n$ líneas indican la energía correspondiente desde el día 1 hasta el día $n$, entrenando sin día de descanso previo ($s_i$).

Al finalizar el programa, se imprime en la terminal la ganancia óptima calculada por el algoritmo y la solución se exporta al directorio `./salida`

---

### Tests

Se incluye un conjunto de pruebas con los ejemplos provistos por el curso y algunos casos adicionales, que pueden ejecutarse desde el directorio `tp_2` con el siguiente comando:

```
$ python3 ./test.py
```

También con el comando:

```
$ python3 -m unittest -v test.py
```

---
