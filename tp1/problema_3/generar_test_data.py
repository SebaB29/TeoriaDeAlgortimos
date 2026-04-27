import csv
import random
from pathlib import Path


SEED = 12345
SIZES = [8, 10, 12, 15, 20, 25, 30]
WALL_PROB = 0.28


def crear_laberinto_con_camino(filas: int, cols: int, prob_pared: float = WALL_PROB) -> list[list[str]]:
    if filas < 5 or cols < 5:
        raise ValueError("El laberinto minimo recomendado es 5x5.")

    lab = [["X" for _ in range(cols)] for _ in range(filas)]

    # Interior transitable inicial
    for i in range(1, filas - 1):
        for j in range(1, cols - 1):
            lab[i][j] = "-"

    entrada = (1, 1)
    salida = (filas - 2, cols - 2)

    # Camino garantizado desde entrada a salida (movimientos derecha/abajo)
    camino = {entrada}
    i, j = entrada
    while (i, j) != salida:
        if i == salida[0]:
            j += 1
        elif j == salida[1]:
            i += 1
        elif random.random() < 0.5:
            i += 1
        else:
            j += 1
        camino.add((i, j))

    # Agregamos paredes aleatorias sin bloquear el camino garantizado
    for r in range(1, filas - 1):
        for c in range(1, cols - 1):
            if (r, c) in camino:
                continue
            if random.random() < prob_pared:
                lab[r][c] = "X"

    lab[entrada[0]][entrada[1]] = "E"
    lab[salida[0]][salida[1]] = "S"
    return lab


def guardar_csv(laberinto: list[list[str]], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(laberinto)


def main() -> None:
    random.seed(SEED)
    base = Path(__file__).resolve().parent
    out_dir = base / "test_data"
    out_dir.mkdir(parents=True, exist_ok=True)

    for archivo in out_dir.glob("*.csv"):
        archivo.unlink()

    # Caso pequeno demostrativo
    enunciado = [
        ["X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "E", "-", "X", "-", "-", "-", "X"],
        ["X", "-", "-", "X", "-", "X", "-", "X"],
        ["X", "-", "X", "X", "-", "X", "-", "X"],
        ["X", "-", "-", "-", "-", "X", "-", "X"],
        ["X", "X", "X", "X", "-", "-", "-", "X"],
        ["X", "-", "-", "-", "-", "X", "S", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X"],
    ]
    guardar_csv(enunciado, out_dir / "enunciado_8x8.csv")

    for n in SIZES:
        lab = crear_laberinto_con_camino(n, n)
        guardar_csv(lab, out_dir / f"{n}x{n}.csv")

    print("Casos generados en:", out_dir)


if __name__ == "__main__":
    main()
