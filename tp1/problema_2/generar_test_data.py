import random
from pathlib import Path


SEED = 12345
SIZES = [6, 8, 10, 12, 15, 20, 30]
EXTRA_EDGES_FACTOR = 2


def generar_ejes(n: int, extra_factor: int = EXTRA_EDGES_FACTOR):
    """
    Genera un grafo conexo no dirigido representado como ejes (a, b, costo)
    con a < b para compatibilidad con la lógica del programa original.
    """
    usados = set()
    ejes = []

    # Base conexa: cadena 1-2-3-...-n
    for a in range(1, n):
        b = a + 1
        c = random.randint(10, 500)
        usados.add((a, b))
        ejes.append((a, b, c))

    max_ejes = (n * (n - 1)) // 2
    max_extra = max_ejes - (n - 1)
    objetivo_extra = min(extra_factor * n, max_extra)
    while len(ejes) < (n - 1 + objetivo_extra):
        a = random.randint(1, n)
        b = random.randint(1, n)
        if a == b:
            continue
        if a > b:
            a, b = b, a
        if (a, b) in usados:
            continue

        c = random.randint(10, 500)
        usados.add((a, b))
        ejes.append((a, b, c))

    return ejes


def guardar_caso(path: Path, origen: int, n: int, ejes):
    with path.open("w", encoding="utf-8") as f:
        f.write(f"{origen},{n}\n")
        for a, b, c in ejes:
            f.write(f"{a},{b},{c}\n")


def main():
    random.seed(SEED)
    base = Path(__file__).resolve().parent
    out_dir = base / "test_data"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Limpia casos previos para evitar mezclar tamaños viejos y nuevos.
    for txt_file in out_dir.glob("*.txt"):
        txt_file.unlink()

    # Caso del enunciado (normalizado con a < b)
    ejes_enunciado = [
        (1, 2, 66),
        (2, 3, 122),
        (2, 4, 126),
        (3, 4, 80),
        (3, 5, 148),
        (4, 5, 126),
        (5, 6, 49),
        (6, 7, 101),
        (7, 8, 69),
        (7, 9, 72),
        (8, 9, 45),
        (8, 11, 56),
        (10, 11, 30),
        (9, 10, 46),
    ]
    guardar_caso(out_dir / "enunciado_11.txt", origen=1, n=11, ejes=ejes_enunciado)

    for n in SIZES:
        ejes = generar_ejes(n)
        guardar_caso(out_dir / f"{n}.txt", origen=1, n=n, ejes=ejes)

    print("Casos generados en:", out_dir)


if __name__ == "__main__":
    main()
