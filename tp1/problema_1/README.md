# 🧩 Problema 1 (División y Conquista)
Este módulo contiene la resolución del problema de la moneda falsa mediante el paradigma de División y Conquista, optimizando el número de pesadas necesarias utilizando una lógica de división en tres grupos (ternaria).

## 🛠️ Requisitos

- Python 3.10 o superior
- Bibliotecas: numpy, scipy, matplotlib, seaborn

## 📂 Estructura

- `problema_1.py`: implementación base para hallar el índice de la moneda falsa.
- `problema_1_pesada.py`: versión equivalente que además reporta cantidad de pesadas.
- `run_test_data.sh`: ejecuta todos los casos de `test_data` y guarda resultados en `results.txt`.
- `mediciones_p1.ipynb`: notebook de mediciones y ajuste teórico.

## 📝 Formato de casos de prueba (`test_data/*.txt`)

Cada archivo debe respetar este formato:

1. Primera línea: `solucion,monedas`
2. Segunda línea: `indice_falsa,peso_0,peso_1,...,peso_n-1`

Ejemplo:

```txt
solucion,monedas
3,10,10,10,9,10
```

## ⚡ Ejecución

### 🔍 Ejecutar un caso puntual
Para obtener solo el índice de la moneda falsa:

```bash
python3 problema_1.py test_data/100.txt
```

Para incluir el conteo de pesadas en la balanza:

```bash
python3 problema_1_pesada.py test_data/100.txt
```

### 🧪 Ejecutar todos los casos de prueba

```bash
chmod +x run_test_data.sh
./run_test_data.sh
```

El resultado por lote se guarda en `results.txt`.

## 📤 Output

Para cada archivo se informa:

- ruta del archivo procesado,
- índice esperado,
- índice obtenido,
- si coincide o no,
- cantidad de pesadas (en `problema_1_pesada.py`).

## 📊 Notebook de mediciones

El archivo `mediciones_p1.ipynb` contiene:

- generación de instancias de monedas con una única falsa,
- medición de tiempo promedio en milisegundos,
- medición de cantidad de pesadas,
- ajuste de tiempo contra referencia lineal `O(n)`,
- ajuste de pesadas contra referencia logarítmica `O(log_3 n)`,
- gráficos de mediciones y error absoluto.

### 📓 Requisitos adicionales para notebook

- Tener Jupyter disponible en el entorno de Python.
