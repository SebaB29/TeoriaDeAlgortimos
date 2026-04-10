# 🧠 TP1: Paradigmas de Algoritmos

Este repositorio contiene la resolución del **Trabajo Práctico 1** de la materia **Teoría de Algoritmos** (Curso Echevarría). El trabajo consiste en el diseño, implementación y análisis de cuatro problemas clásicos utilizando diferentes técnicas de diseño.

## 📑 Índice
1. [⚖️ Problema 1: División y Conquista](#-problema-1-división-y-conquista)
2. [🧭 Problema 2: Greedy](#-problema-2-greedy)
3. [🤖 Problema 3: Backtracking](#-problema-3-backtracking)
4. [🧩 Problema 4: Programación Dinámica](#-problema-4-programación-dinámica)
5. [🛠️ Especificaciones](#-especificaciones)
6. [👥 Equipo](#-equipo)

---

## ⚖️ Problema 1: División y Conquista
**El problema de la moneda falsa:** Dada una bolsa con $n$ monedas donde exactamente una es más liviana que el resto, se debe identificar cuál es utilizando una balanza de dos platillos.

* **Estrategia:** Diseño de un algoritmo que divide el conjunto de monedas en subgrupos para reducir el espacio de búsqueda exponencialmente sin recurrir a ordenamientos.
* **Análisis:** Cálculo del orden de complejidad temporal y validación mediante pruebas con tamaños de datos crecientes ($n=100$ a $n=50.000$).
* **Visualización:** Relación entre el tiempo de ejecución, la cantidad de pesadas realizadas y la curva teórica de complejidad.

## 🧭 Problema 2: Greedy
**Análisis Arqueológico (Dijkstra):** Traducción y análisis técnico de un código en lenguaje BASIC (`paolo.bas`) que opera sobre grafos para encontrar rutas óptimas.

* **Identificación:** Análisis de la lógica de selección de vértices y actualización de distancias para replicar el comportamiento en Python.
* **Regla Greedy:** Identificación de la regla de elección local óptima y justificación de por qué el algoritmo pertenece a este paradigma.
* **Estructuras de Datos:** Gestión de cuadros de costos, arreglos de distancias y estados de visita de nodos.

## 🤖 Problema 3: Backtracking
**La Aspiradora de Casanova:** Implementación de un algoritmo de búsqueda para que una aspiradora robot encuentre la salida de un laberinto rectangular codificado de forma matricial.

* **Restricciones de Movimiento:** El robot solo puede realizar tres operaciones: `Ver adelante` (pared, camino o salida), `Avanzar` y `Girar 90º a la izquierda`.
* **Diseño:** Exploración del espacio de soluciones mediante recursión con retroceso, identificando supuestos y condiciones de borde.
* **Pruebas:** Generación de sets de datos aleatorios de tamaño $m \times n$ y análisis de los tiempos de ejecución obtenidos.

## 🧩 Problema 4: Programación Dinámica
**Descomposición Mínima en Palíndromos:** Determinar el menor número de palíndromos en los que se puede descomponer una cadena dada (ej: `ARACALACANA` $\rightarrow$ 3).

* **Ecuación de Recurrencia:** Definición formal del estado y la transición óptima para minimizar las particiones.
* **Propiedades:** Justificación de la **Subestructura Óptima** y de los **Subproblemas Superpuestos**.
* **Optimización:** Implementación mediante **Memoization** para asegurar una complejidad temporal eficiente de $O(n^2)$ frente al enfoque recursivo simple.

---

## 🛠️ Especificaciones
* **Lenguaje:** Python 3.x.
* **Entorno:** Notebooks de Google Colab.
* **Análisis de Complejidad:** Cada algoritmo incluye su correspondiente análisis teórico basado en el pseudocódigo y comparativas con los tiempos de ejecución medidos.

## 👥 Equipo

El equipo de trabajo para el desarrollo de este Trabajo Práctico está conformado por:

| Integrante             |
| :--------------------- |
| Sebastián Brizuela     |
| Nicolas Chen           |
| Santiago Ignacio Janon |
| Nicolas Lanseros       |
| Joaquin Ordoñez        |

---
