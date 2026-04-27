import csv
import sys


# Funcion principal de inicializacion
def resolver_laberinto(entrada: tuple[int, int], salida: tuple[int, int], laberinto: list[list[str]]) -> list | None:
    visitados = set()
    camino = []

    # Se asume que la aspiradora arranca mirando hacia arriba (direccion 0)
    if buscar_camino(entrada, 0, salida, laberinto, visitados, camino):
        return camino
    return None


# Función recursiva de Backtracking
def buscar_camino(pos_actual, direccion, salida, laberinto, visitados, camino):
    # 1. Registrar estado espacial (independiente de la dirección)
    visitados.add(pos_actual)
    camino.append(pos_actual)

    # Condición de éxito: encontramos la salida
    if pos_actual == salida:
        return True

    # 2. Explorar el entorno físico girando hasta 4 veces
    dir_actual = direccion
    for _ in range(4):
        pos_sig = mirar_adelante(pos_actual, dir_actual)

        # Si la celda de enfrente está dentro del laberinto, no es pared y NUNCA fue pisada
        if (0 <= pos_sig[0] < len(laberinto) and
            0 <= pos_sig[1] < len(laberinto[0]) and
            laberinto[pos_sig[0]][pos_sig[1]] != "X" and
            pos_sig not in visitados):

            # Llamada recursiva (avanzamos físicamente a esa celda)
            if buscar_camino(pos_sig, dir_actual, salida, laberinto, visitados, camino):
                return True

        # Si había pared, o estaba visitada, o el camino explorado falló (retornó False):
        # Giramos 90 grados a la izquierda para probar el siguiente frente
        dir_actual = (dir_actual + 1) % 4

    # 3. BACKTRACKING LÓGICO: Probamos las 4 direcciones y ninguna sirvió.
    # Desapilamos esta celda porque no forma parte del camino de salida.
    camino.pop()
    return False


# Función auxiliar de sensor (traduce la dirección física a coordenadas de matriz)
# 0: Arriba, 1: Izquierda, 2: Abajo, 3: Derecha
def mirar_adelante(posicion: tuple[int, int], direccion: int) -> tuple[int, int]:
    if direccion == 0:
        return (posicion[0] - 1, posicion[1])
    if direccion == 1:
        return (posicion[0], posicion[1] - 1)
    if direccion == 2:
        return (posicion[0] + 1, posicion[1])
    # direccion == 3
    return (posicion[0], posicion[1] + 1)


def serializar_csv(nombre_csv: str) -> tuple[list[list[str]], tuple[int, int], tuple[int, int]]:
    """
    Lee un laberinto rectangular desde CSV.

    Formato esperado por celda:
    - "X" para pared
    - "-" o " " para camino libre
    - "E" para entrada
    - "S" para salida
    """
    laberinto = []
    entrada = None
    salida = None

    with open(nombre_csv, "r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        for i, fila in enumerate(reader):
            if not fila:
                continue

            fila_limpia = [celda.strip() for celda in fila]
            if laberinto and len(fila_limpia) != len(laberinto[0]):
                raise ValueError("Formato invalido: el laberinto debe ser rectangular.")

            for j, valor in enumerate(fila_limpia):
                if valor == "E":
                    if entrada is not None:
                        raise ValueError("Formato invalido: hay mas de una entrada E.")
                    entrada = (i, j)
                elif valor == "S":
                    if salida is not None:
                        raise ValueError("Formato invalido: hay mas de una salida S.")
                    salida = (i, j)

            laberinto.append(fila_limpia)

    if not laberinto:
        raise ValueError("Formato invalido: el archivo esta vacio.")
    if entrada is None or salida is None:
        raise ValueError("Formato invalido: se requiere exactamente una E y una S.")

    return laberinto, entrada, salida


def resolver_archivo_csv(nombre_csv: str) -> tuple[list[list[str]], tuple[int, int], tuple[int, int], list | None]:
    laberinto, entrada, salida = serializar_csv(nombre_csv)
    camino = resolver_laberinto(entrada, salida, laberinto)
    return laberinto, entrada, salida, camino


def imprimir_laberinto(laberinto: list[list[str]], camino: list[tuple[int, int]] | None = None) -> None:
    copia = [fila[:] for fila in laberinto]

    if camino:
        for i, j in camino:
            if copia[i][j] not in ("E", "S"):
                copia[i][j] = "*"

    for fila in copia:
        print(" ".join(str(celda) for celda in fila))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise AssertionError("Error: se esperaba exactamente 1 archivo CSV como argumento")

    nombre_archivo = sys.argv[1]
    laberinto, entrada, salida, camino = resolver_archivo_csv(nombre_archivo)

    print(nombre_archivo)
    print(f"Dimensiones: {len(laberinto)}x{len(laberinto[0])}")
    print(f"Entrada: {entrada}")
    print(f"Salida: {salida}")
    print("Camino encontrado: " + ("Si" if camino is not None else "No"))
    print("Longitud del camino: " + (str(len(camino)) if camino is not None else "0"))

    print("\nLaberinto original:")
    imprimir_laberinto(laberinto)

    if camino is not None:
        print("\nCamino recorrido:")
        print(camino)
        print("\nLaberinto con camino:")
        imprimir_laberinto(laberinto, camino)