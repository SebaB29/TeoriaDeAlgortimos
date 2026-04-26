import sys
import time


def min_palindromos(cadena):  # O(n^2)
    """
    Calcula la cantidad mínima de palíndromos necesarios para descomponer la cadena S.
    Utiliza programación dinámica con una matriz de precálculo para verificar palíndromos en O(1)
    y un arreglo de optimización para determinar el número mínimo de cortes.
    Equivale algorítmicamente a encontrar la partición más eficiente de la estructura de la cadena.
    """
    n = len(cadena)  # O(1)
    if n == 0:  # O(1)
        return 0  # O(1)

    # Matriz de precálculo de palindromos
    es_palindromo = [[False for _ in range(n)] for _ in range(n)]  # O(n^2)

    for i in range(n - 1, -1, -1):  # O(n)
        for j in range(i, n):  # O(n)
            if cadena[i] == cadena[j]:  # O(1)
                if j - i <= 2 or es_palindromo[i + 1][j - 1]:  # O(1)
                    es_palindromo[i][j] = True  # O(1)

    # Array con cantidades de cortes para formar grupos de palindromos
    # EJEMPLO: ["C", "ASA"] -> 1 corte
    # EJEMPLO: ["ARA", "CALAC", "ANA"] -> 2 cortes
    cortes = [0] * n  # O(n)

    for i in range(n):  # O(n)

        if es_palindromo[0][i]:  # O(1)
            cortes[i] = 0  # O(1)

        else:  # O(1)
            # Buscamos el mejor punto de corte 'j'
            # Inicializamos con el peor caso: un corte por cada letra
            cortes[i] = i  # O(1)
            for j in range(i):  # O(n)
                if es_palindromo[j + 1][i]:  # O(1)
                    cortes[i] = min(cortes[i], cortes[j] + 1)  # O(1)

    # Como pide cantidad minima de palindromos -> cantidad minima de cortes + 1
    return cortes[n - 1] + 1  # O(1)


def serializar_txt(nombre_txt: str) -> tuple[int, str]:
    """
    Lee un archivo de prueba con el formato:
    - Primera linea: resultado,cadena
    - Segunda linea: esperado,cadena
    """
    with open(nombre_txt, "r", encoding="utf-8") as archivo:
        next(archivo)

        linea_datos = archivo.readline().strip()
        if not linea_datos:
            raise ValueError("Formato invalido: falta la linea de datos.")

        partes = linea_datos.split(",", maxsplit=1)
        if len(partes) != 2:
            raise ValueError(
                "Formato invalido: se esperaba 'esperado,cadena'.")

        esperado = int(partes[0].strip())
        cadena = partes[1].strip()

    return esperado, cadena


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise AssertionError(
            "Error: se esperaba exactamente 1 archivo txt como argumento")

    nombre_archivo = sys.argv[1]
    esperado, cadena = serializar_txt(nombre_archivo)

    inicio = time.perf_counter()
    obtenido = min_palindromos(cadena)
    fin = time.perf_counter()
    tiempo_ms = (fin - inicio) * 1000.0

    print(nombre_archivo)
    print("Longitud cadena: " + str(len(cadena)))
    print("Esperado: " + str(esperado))
    print("Obtenido: " + str(obtenido))
    print("Coincide: " + ("Si" if esperado == obtenido else "No"))
    print(f"Tiempo: {tiempo_ms:.6f} ms")
