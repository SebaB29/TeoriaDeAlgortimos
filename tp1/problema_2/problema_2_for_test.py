import os
import sys


INF = 15000


def dijkstra(n, v, cost, sol, dist):

    sol[v] = 1
    dist[v] = 0
    for _ in range(n - 1):
        dist_min = 15000
        u = -1
        for j in range(n):
            if dist[j] <= dist_min and sol[j] == 0:
                dist_min = dist[j]
                u = j
        if (u == -1):
            break
        sol[u] = 1
        for j in range(n):
            if dist[j] >= (dist[u] + cost[u][j]):
                dist[j] = dist[u] + cost[u][j]
    return


def construir_matriz_costos_desde_ejes(n, ejes):
    """
    Construye la matriz de costos replicando la lógica del código original:
    - Carga ejes dirigidos A->B
    - Completa ausentes con INF
    - Fuerza simetría copiando la parte superior a la inferior
    """
    cost = [[0] * n for _ in range(n)]

    for a, b, c in ejes:
        # El código original copia triángulo superior en el inferior.
        # Por eso normalizamos para guardar en la parte superior.
        if a <= b:
            cost[a - 1][b - 1] = c
        else:
            cost[b - 1][a - 1] = c

    for i in range(n):
        for j in range(n):
            if cost[i][j] == 0:
                cost[i][j] = INF

    for i in range(n):
        for j in range(i):
            cost[i][j] = cost[j][i]

    return cost


def ejecutar_dijkstra(n, cost, origen):
    """
    Ejecuta Dijkstra desde un vértice origen (1-based) y retorna distancias.
    """
    v = origen - 1
    dist = [0] * n
    sol = [0] * n

    for i in range(n):
        dist[i] = cost[v][i]
        sol[i] = 0

    dijkstra(n, v, cost, sol, dist)
    return dist


def serializar_txt(nombre_txt):
    """
    Formato esperado:
    - Primera línea: origen,n
    - Siguientes líneas: a,b,costo
    """
    with open(nombre_txt, "r", encoding="utf-8") as archivo:
        primera = archivo.readline().strip()
        if not primera:
            raise ValueError("Archivo vacío")

        origen_str, n_str = [x.strip() for x in primera.split(",")]
        origen = int(origen_str)
        n = int(n_str)

        ejes = []
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            a_str, b_str, c_str = [x.strip() for x in linea.split(",")]
            ejes.append((int(a_str), int(b_str), int(c_str)))

    return origen, n, ejes


def resolver_archivo_txt(nombre_txt):
    origen, n, ejes = serializar_txt(nombre_txt)
    cost = construir_matriz_costos_desde_ejes(n, ejes)
    dist = ejecutar_dijkstra(n, cost, origen)
    return origen, dist


def imprimir_resultados(origen, dist):
    print("SALIDA", "LLEGADA", "DISTANCIA")
    for i in range(len(dist)):
        if dist[i] < INF:
            print(origen, " ", i + 1, " ", dist[i])


def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    n = int(input("INGRESE EL NUMERO DE VERTICES: "))
    print(n)
    cost = [[0] * n for _ in range(n)]
    dist = [0] * n
    sol = [0] * n
    A = 1

    # Bucle para ingresar los vertices y sus costos
    while (True):

        print("INGRESE EL CUADRO DE COSTOS (INGRESE 0, 0 PARA TERMINAR)")
        print('')
        A, B = map(int, input("EL EJE: ").split())  # El (0, 0) es para salir

        if (A == 0 and B == 0):
            break

        cost[A - 1][B - 1] = int(input("COSTO DEL EJE "))

    # Los pares de vertices sin costos se les asigna un costo de 15000 ya que se consideran inaccesibles.
    for i in range(n):
        for j in range(n):
            if (cost[i][j] == 0):
                cost[i][j] = INF

    # Genera una matriz simetrica ya que el grafo es dirigido.
    for i in range(n):
        for j in range(i):
            cost[i][j] = cost[j][i]

    # Bucle para realizar Dijkstra y volver al bucle anterior en caso de necesitarlo.
    while (True):
        v = int(input("INGRESE EL VERTICE DE SALIDA ")) - 1
        # Asigna los valores la lista de distancias mínimas del nodo destino v, y su lista de soluciones en 0.
        for i in range(n):
            dist[i] = cost[v][i]
            sol[i] = 0

        dijkstra(n, v, cost, sol, dist)
        imprimir_resultados(v + 1, dist)
        RES = input("OTRA VEZ? (SI/NO) ")
        if RES == "NO":
            break


if __name__ == "__main__":
    if len(sys.argv) == 2:
        archivo = sys.argv[1]
        origen, distancias = resolver_archivo_txt(archivo)
        print(archivo)
        imprimir_resultados(origen, distancias)
    else:
        main()
