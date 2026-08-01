"""Renderiza una página (o una banda de ella) del escaneo de Hipertexto 8 a PNG.

El PDF es un escaneo de 304 páginas sin capa de texto usable, así que transcribir
exige mirar la página. A 200 dpi y recortando la banda de interés, las expresiones
con signos de agrupación se leen sin ambigüedad — que es donde el OCR falla.

    python scripts/pagina_hipertexto8.py 14                    # página completa
    python scripts/pagina_hipertexto8.py 14 --y 0.62 0.83      # banda vertical
    python scripts/pagina_hipertexto8.py 14 --y 0.6 0.9 --x 0.5 1.0 --dpi 260

Escribe en tmp/hipertexto8/ (ignorado por git).
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PDF = Path(
    r"C:\Users\orian\OneDrive\Documentos\IE Los Andes\Libros\Libros santillana 8 y 9"
    r"\hipertexto-matematicas-8.pdf"
)
SALIDA = ROOT / "tmp" / "hipertexto8"
POPPLER = Path(
    r"C:\Users\orian\.cache\codex-runtimes\codex-primary-runtime\dependencies\native"
    r"\poppler\Library\bin\pdftoppm.exe"
)


def _pdftoppm() -> str:
    if POPPLER.exists():
        return str(POPPLER)
    encontrado = shutil.which("pdftoppm")
    if not encontrado:
        raise SystemExit("No se encontró pdftoppm (poppler ni MiKTeX).")
    return encontrado


def renderizar(pagina: int, dpi: int) -> Path:
    SALIDA.mkdir(parents=True, exist_ok=True)
    prefijo = SALIDA / f"p{pagina:03d}_{dpi}"
    destino = prefijo.with_suffix(".png")
    if not destino.exists():
        subprocess.run(
            [_pdftoppm(), "-f", str(pagina), "-l", str(pagina), "-r", str(dpi), "-png",
             "-singlefile", str(PDF), str(prefijo)],
            check=True,
            capture_output=True,
        )
    return destino


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pagina", type=int, help="número de página del PDF (1-304)")
    parser.add_argument("--dpi", type=int, default=200)
    parser.add_argument("--y", type=float, nargs=2, metavar=("Y0", "Y1"),
                        help="banda vertical en fracción de la altura, p. ej. 0.6 0.9")
    parser.add_argument("--x", type=float, nargs=2, metavar=("X0", "X1"),
                        help="banda horizontal en fracción del ancho")
    parser.add_argument("--max-lado", type=int, default=2200,
                        help="lado máximo del PNG resultante")
    args = parser.parse_args()

    completa = renderizar(args.pagina, args.dpi)
    im = Image.open(completa)
    if not (args.y or args.x):
        print(completa, im.size)
        return 0

    w, h = im.size
    x0, x1 = args.x or (0.0, 1.0)
    y0, y1 = args.y or (0.0, 1.0)
    rec = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
    if max(rec.size) > args.max_lado:
        escala = args.max_lado / max(rec.size)
        rec = rec.resize((int(rec.width * escala), int(rec.height * escala)), Image.LANCZOS)
    destino = SALIDA / f"p{args.pagina:03d}_{int(y0*100)}{int(y1*100)}_{int(x0*100)}{int(x1*100)}.png"
    rec.save(destino)
    print(destino, rec.size)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
