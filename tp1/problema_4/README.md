# 🧠 Problema 4 (Programacion Dinamica)
Este módulo contiene la resolución del problema de descomposición de cadenas en el menor número de palíndromos posible, utilizando un enfoque de Programación Dinámica con tabulación.

## 🛠️ Requisitos

- Python 3.10 o superior
- Bibliotecas para mediciones: numpy, scipy, matplotlib, seaborn

## 📂 Estructura

- `problema_4.py`: algoritmo de programacion dinamica para minimo numero de palindromos y ejecucion por archivo.
- `generar_test_data.py`: generador de sets de prueba manuales y aleatorios.
- `run_test_data.sh`: ejecucion por lote de todos los casos en `test_data`.
- `mediciones_p4.ipynb`: notebook de mediciones y ajuste teorico.
- `test_data/`: casos de entrada en formato txt.

## 📝 Formato de casos de prueba (`test_data/*.txt`)

Cada archivo de entrada debe tener:

1. Primera linea: `resultado,cadena`
2. Segunda linea: `esperado,cadena`

Ejemplo:

```txt
resultado,cadena
3,ARACALACANA
```

## ⚡ Ejecucion

### 🔍 Ejecutar un caso puntual

```bash
python3 problema_4.py test_data/enunciado_aracalacana.txt
```

### 🧪 Ejecutar todos los casos de prueba

```bash
chmod +x run_test_data.sh
./run_test_data.sh
```

El resultado se guarda en `results.txt`.

### 🎲 Generar casos de prueba

```bash
python3 generar_test_data.py
```

## 📤 Output

Para cada archivo se informa:

- ruta del archivo procesado,
- longitud de la cadena,
- resultado esperado,
- resultado obtenido,
- si coincide o no,
- tiempo de ejecucion por caso (en ms).

## 📊 Notebook de mediciones

El archivo `mediciones_p4.ipynb` contiene:

- generacion reproducible de cadenas de prueba,
- medicion de tiempos promedio con `time_algorithm`,
- conversion de tiempos a milisegundos,
- ajuste por minimos cuadrados contra referencia cuadratica `O(n^2)`,
- grafico de tiempos medidos vs curva teorica,
- grafico de error absoluto del ajuste.

### 📓 Requisitos adicionales para notebook

- Tener Jupyter disponible en el entorno de Python.
