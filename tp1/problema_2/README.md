# Trabajo Práctico 1 - Problema 2 (Greedy)

## Requisitos

- Python 3.10 o superior
- Bibliotecas: numpy, scipy, matplotlib, seaborn

## Estructura

- `problema_2.py`: traducción directa e interactiva (mantiene el estilo del código original).
- `problema_2_for_test.py`: versión adaptada para pruebas automáticas por archivo.
- `generar_test_data.py`: generador de instancias para benchmarking.
- `run_test_data.sh`: ejecución por lote de todos los casos en `test_data`.
- `mediciones_p2.ipynb`: notebook de mediciones y ajuste teórico.

## Formato de casos de prueba (`test_data/*.txt`)

Cada archivo de entrada debe tener:

1. Primera línea: `origen,n`
2. Líneas siguientes: `a,b,costo`

Ejemplo:

```txt
1,11
1,2,66
2,3,122
...
```

## Ejecución

### Ejecutar un caso puntual

```bash
python3 problema_2_for_test.py test_data/enunciado_11.txt
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

La salida muestra una tabla con:

- `SALIDA`: vértice origen
- `LLEGADA`: vértice destino
- `DISTANCIA`: distancia mínima calculada

## Notebook de mediciones

El archivo `mediciones_p2.ipynb` contiene:

- Generación de instancias de grafos conectados.
- Medición de tiempos promedio con `time_algorithm`.
- Conversión de tiempos a milisegundos.
- Ajuste por mínimos cuadrados contra una referencia `O(n^2)`.
- Gráfico de tiempos medidos vs curva teórica.
- Gráfico de error absoluto del ajuste.

### Requisitos adicionales para notebook

- Tener Jupyter disponible en el entorno de Python.
