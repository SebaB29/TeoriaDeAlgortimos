# Trabajo Practico 1 - TDA (2026 1C)

## Requisitos generales

- Python 3.10 o superior
- Para notebooks y graficos: numpy, scipy, matplotlib, seaborn

## Estructura de la raiz

- `problema_1/`: solucion de Division y Conquista + test_data + mediciones.
- `problema_2/`: solucion Greedy + test_data + mediciones.
- `problema_3/`: solucion Backtracking + test_data + mediciones.
- `problema_4/`: solucion Programacion Dinamica + test_data + mediciones.
- `util.py`: utilidades compartidas (incluye `time_algorithm` para mediciones).

Cada carpeta de problema contiene su propio `README.md` con formato de entrada, ejecucion y resultados.

## Ejecucion rapida por problema

### Problema 1

```bash
cd problema_1
bash run_test_data.sh
```

### Problema 2

```bash
cd problema_2
bash run_test_data.sh
```

### Problema 3

```bash
cd problema_3
bash run_test_data.sh
```

### Problema 4

```bash
cd problema_4
bash run_test_data.sh
```

En todos los casos, la salida por lote se guarda en `results.txt` dentro de la carpeta del problema.

## Regeneracion de sets de datos

Los problemas que tienen generador incluyen `generar_test_data.py`.

Ejemplo:

```bash
cd problema_4
python3 generar_test_data.py
```

## Notebooks de mediciones

- `problema_1/mediciones_p1.ipynb`
- `problema_2/mediciones_p2.ipynb`
- `problema_3/mediciones_p3.ipynb`
- `problema_4/mediciones_p4.ipynb`

Cada notebook incluye mediciones empiricas, ajuste a curva teorica y grafico de error.
