import os


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
                cost[i][j] = 15000

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
        print("SALIDA", "LLEGADA", "DISTANCIA")
        for i in range(n):
            if dist[i] < 15000:
                print(v + 1, " ", i + 1, " ", dist[i])
        RES = input("OTRA VEZ? (SI/NO) ")
        if RES == "NO":
            break


main()
