# Trabajo Práctico 1 - Problema 3 (Backtracking)

## Requisitos

- Python 3.10 o superior
- Bibliotecas para mediciones: numpy, scipy, matplotlib, seaborn

## Estructura

- `problema_3.py`: resolución principal del laberinto por backtracking y ejecución por archivo.
- `generar_test_data.py`: generador de laberintos para pruebas automáticas.
- `run_test_data.sh`: ejecución por lote de todos los casos en `test_data`.
- `mediciones_p3.ipynb`: notebook de mediciones y ajuste teórico.
- `test_data/`: casos de entrada en formato CSV matricial.

## Formato de casos de prueba (`test_data/*.csv`)

Cada archivo representa una matriz rectangular con valores separados por coma:

- `X`: pared
- `-` o espacio en blanco: camino
- `E`: posición inicial de la aspiradora
- `S`: salida del laberinto

Ejemplo:

```csv
X,X,X,X
X,E,-,X
X,-,S,X
X,X,X,X
```

## Ejecución

### Ejecutar un caso puntual

```bash
python3 problema_3.py test_data/enunciado_8x8.csv
```

### Ejecutar todos los casos de prueba

```bash
chmod +x run_test_data.sh
./run_test_data.sh
```

El resultado se guarda en `results.txt`.

### Regenerar casos de prueba

```bash
python3 generar_test_data.py
```

## Output

Para cada archivo se informa:

- ruta del archivo procesado,
- dimensiones del laberinto,
- coordenadas de entrada y salida,
- si se encontró o no camino,
- longitud del camino encontrado,
- laberinto original,
- laberinto con camino marcado (si se encontró).

## Notebook de mediciones

El archivo `mediciones_p3.ipynb` contiene:

- generación de instancias de laberintos con camino garantizado,
- medición de tiempos promedio con `time_algorithm`,
- conversión de tiempos a milisegundos,
- ajuste por mínimos cuadrados contra una referencia cuadrática `O(n^2)`,
- gráfico de tiempos medidos vs curva teórica,
- gráfico de error absoluto del ajuste.

### Requisitos adicionales para notebook

- Tener Jupyter disponible en el entorno de Python.
