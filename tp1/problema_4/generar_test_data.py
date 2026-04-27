import random
from pathlib import Path

from problema_4 import min_palindromos


SEED = 12345
SIZES = [100, 200, 300, 400, 500, 600]
ALFABETO = "ABCDE"


def generar_cadena_aleatoria(n: int) -> str:
    return "".join(random.choice(ALFABETO) for _ in range(n))


def guardar_caso(path: Path, esperado: int, cadena: str) -> None:
    with path.open("w", encoding="utf-8") as f:
        f.write("resultado,cadena\n")
        f.write(f"{esperado},{cadena}\n")


def main() -> None:
    random.seed(SEED)
    base = Path(__file__).resolve().parent
    out_dir = base / "test_data"
    out_dir.mkdir(parents=True, exist_ok=True)

    for txt_file in out_dir.glob("*.txt"):
        txt_file.unlink()

    enunciado = {"enunciado_aracalacana.txt": "ARACALACANA"}

    for nombre, cadena in enunciado.items():
        esperado = min_palindromos(cadena)
        guardar_caso(out_dir / nombre, esperado, cadena)

    for n in SIZES:
        cadena = generar_cadena_aleatoria(n)
        esperado = min_palindromos(cadena)
        guardar_caso(out_dir / f"random_{n}.txt", esperado, cadena)

    print("Casos generados en:", out_dir)


if __name__ == "__main__":
    main()
