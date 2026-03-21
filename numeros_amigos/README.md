# 🤝 TP0: Números Amigos

Este repositorio contiene la resolución del Trabajo Práctico 0 de la materia **Teoría de Algoritmos** (Curso Echevarría) de la Facultad de Ingeniería de la Universidad de Buenos Aires (FIUBA).

## 📑 Índice
1. [📋 Descripción del Problema](#-descripción-del-problema)
2. [🚀 Optimización Realizada](#-optimización-realizada)
3. [📉 Análisis de Complejidad](#-análisis-de-complejidad)
4. [📊 Resultados y Rendimiento](#-resultados-y-rendimiento)
5. [🛠️ Especificaciones](#-especificaciones)

## 📋 Descripción del Problema
El objetivo es diseñar e implementar un algoritmo eficiente para encontrar todos los pares de **números amigos** en un rango dado $[0, MAX)$.

* **Definición:** Dos números son amigos si la suma de los divisores propios del primero es igual al segundo, y viceversa.
* **Ejemplo clásico:** 220 y 284.
    * Divisores de 220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110. Suma = 284.
    * Divisores de 284: 1, 2, 4, 71 y 142. Suma = 220.

## 🚀 Optimización Realizada
El algoritmo original proporcionado por la cátedra era eficaz pero ineficiente, tardando **581 segundos** para $MAX = 100.000$. La reingeniería aplicada logró reducir este tiempo significativamente mediante:

1.  **Reducción del límite de búsqueda:** Se modificaron los bucles internos para buscar divisores solo hasta la raíz cuadrada del número ($\sqrt{n}$), lo que disminuye drásticamente las iteraciones.
2.  **Poda de búsqueda:** Se omiten cálculos para casos donde el par ya fue evaluado o no cumple con las condiciones básicas de amistad.

## 📉 Análisis de Complejidad
* **Algoritmo Original:** $\approx O(n^{2})$.
* **Algoritmo Propuesto:** $\approx O(n \sqrt{n})$.



## 📊 Resultados y Rendimiento
Las mediciones de tiempo (realizadas en Google Colab) para el algoritmo propuesto son las siguientes:

| Rango (MAX) | Tiempo [s] |
| :--- | :--- |
| 50.000 | 0.4870 |
| 100.000 | 1.6828 |
| 150.000 | 3.2780 |
| 200.000 | 3.8927 |
| 250.000 | 6.3505 |

## 🛠️ Especificaciones
* **Lenguaje:** Python 3.10.
* **Restricción:** Se mantuvo el prototipo original de la función `amigos(MAX)` para asegurar una reingeniería transparente.
* **Números Perfectos:** Se optó por incluirlos en el resultado final para mantener la paridad con el comportamiento del código original.
