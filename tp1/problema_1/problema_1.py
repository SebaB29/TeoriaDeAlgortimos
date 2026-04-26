import sys


def sumar_subarreglo(M: list, inicio: int, fin: int) -> float:
    """
    Calcula la suma de los pesos en el subarreglo definido por [inicio, fin] inclusive.
    Itera sobre índices para evitar la copia de arreglos en memoria (slicing).
    Equivale algorítmicamente a colocar las monedas en la balanza.
    """
    suma = 0
    for i in range(inicio, fin + 1):
        suma += M[i]
    return suma


def encontrar_moneda_falsa_recursivo(M: list, inicio: int, fin: int) -> int:
    """
    Función recursiva Top-Down que halla el índice de la moneda falsa.
    """
    # 1. Caso Base: Si queda una sola moneda, es la defectuosa
    n = fin - inicio + 1
    if n == 1:
        return inicio

    # 2. División: Cálculo de subconjuntos
    k = n // 3
    resto = n % 3

    # Ajuste para mantener el equilibrio de cardinalidad
    if resto == 2:
        k += 1

    # Definición explícita de fronteras (índices)
    fin_A = inicio + k - 1
    inicio_B = inicio + k
    fin_B = inicio + 2 * k - 1

    # 3. "Pesada": Comparación explícita de sumatorias
    suma_A = sumar_subarreglo(M, inicio, fin_A)
    suma_B = sumar_subarreglo(M, inicio_B, fin_B)

    # 4. Conquista y recursión
    if suma_A < suma_B:
        return encontrar_moneda_falsa_recursivo(M, inicio, fin_A)
    elif suma_B < suma_A:
        return encontrar_moneda_falsa_recursivo(M, inicio_B, fin_B)
    else:
        # La moneda defectuosa está en el grupo C (resto del arreglo)
        inicio_C = inicio + 2 * k
        return encontrar_moneda_falsa_recursivo(M, inicio_C, fin)


def buscar_moneda_falsa(M: list) -> int:
    """
    Función principal que inicializa la búsqueda.
    Retorna el índice donde se encuentra la moneda más liviana.
    """
    if not M:
        raise ValueError("El conjunto de monedas no puede estar vacío.")

    return encontrar_moneda_falsa_recursivo(M, 0, len(M) - 1)


def serializar_txt(nombre_txt):
    """
    Lee un archivo txt con el formato de casos de prueba de monedas.

    Formato esperado:
    - Primera línea: "solucion,monedas"
    - Segunda línea: "indice_falsa,peso_0,peso_1,...,peso_n-1"

    Ejemplo:
        solucion,monedas
        3,10,10,10,9,10

    Argumentos:
        nombre_txt: Ruta del archivo txt

    Devuelve:
        Tupla (solucion, monedas), donde:
        - solucion es el índice esperado de la moneda falsa
        - monedas es la lista de pesos
    """
    with open(nombre_txt, 'r') as archivo:
        # Ignoramos la primera línea
        next(archivo)

        linea_datos = archivo.readline().strip()
        if not linea_datos:
            raise ValueError("Formato invalido: falta la linea de datos.")

        valores = [int(x.strip())
                   for x in linea_datos.split(',') if x.strip() != ""]
        if len(valores) < 2:
            raise ValueError(
                "Formato invalido: se esperaba solucion y al menos una moneda.")

        solucion = valores[0]
        monedas = valores[1:]

    return solucion, monedas


# Para ejecutar:
# python3 problema_1.py test_data/100.txt (u otro txt con el mismo formato)

# Para correr los test completos:
# $ chmod +x run_test_data.sh
# $ ./run_test_data.sh
if __name__ == "__main__":
    # Leemos los argumentos
    argumentos = sys.argv
    if len(argumentos) != 2:
        raise AssertionError("Error: se esperaba solo 2 argumentos")

    # Leemos el caso de prueba (solucion esperada y lista de monedas)
    solucion_esperada, monedas = serializar_txt(argumentos[1])

    # Ejecutamos el algoritmo de division y conquista
    solucion_obtenida = buscar_moneda_falsa(monedas)

    print(argumentos[1])
    print("Indice esperado: " + str(solucion_esperada))
    print("Indice obtenido: " + str(solucion_obtenida))
    print("Coincide: " + ("Sí" if solucion_esperada == solucion_obtenida else "No"))
