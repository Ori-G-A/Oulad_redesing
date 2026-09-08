"""
tests/unit/test_architecture_layers.py
=======================================
R2 comprobado, no solo escrito. Del hallazgo P2 #9 de la auditoría
(2026-09-05): "los servicios importan el cliente de IA de infraestructura; el
dominio contiene carga de archivos pickle, entrenamiento y dependencias
numpy/sklearn".

Las capas solo son capas si algo las sostiene:

    domain/         → sin imports de capas superiores ni de librerías externas
    application/    → importa domain/, NO infrastructure/
    infrastructure/ → implementa lo que domain/ y application/ declaran
    interface/, api/→ pueden importar todo (son la composición)
"""

import ast
import pathlib

import pytest

_SRC = pathlib.Path(__file__).resolve().parents[2] / "src"

# Librerías que no pueden aparecer en domain/: el dominio es aritmética y reglas,
# no I/O ni modelos entrenados. `pickle` salió de aquí con IsotonicCalibrator.
_FORBIDDEN_IN_DOMAIN = {"numpy", "sklearn", "pandas", "pickle", "psycopg2", "sqlite3", "requests"}


def _modules(layer: str) -> list[pathlib.Path]:
    return sorted((_SRC / layer).rglob("*.py"))


def _imported_names(path: pathlib.Path) -> set[str]:
    """Módulos importados, incluidos los locales dentro de funciones."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            names.add(node.module)
    return names


def _ids(paths):
    return [str(p.relative_to(_SRC)) for p in paths]


@pytest.mark.parametrize("path", _modules("application"), ids=_ids(_modules("application")))
def test_application_does_not_import_infrastructure(path):
    offenders = sorted(
        name for name in _imported_names(path) if name.startswith("src.infrastructure")
    )
    assert not offenders, (
        f"{path.name} importa infraestructura: {offenders}. La capa de aplicación declara lo "
        "que necesita y la composición (api/routers, streamlit/app.py) se lo inyecta."
    )


@pytest.mark.parametrize("path", _modules("domain"), ids=_ids(_modules("domain")))
def test_domain_does_not_import_upper_layers(path):
    offenders = sorted(
        name
        for name in _imported_names(path)
        if name.startswith(("src.application", "src.infrastructure", "src.interface", "api."))
    )
    assert not offenders, f"{path.name} importa capas superiores: {offenders}."


@pytest.mark.parametrize("path", _modules("domain"), ids=_ids(_modules("domain")))
def test_domain_stays_free_of_io_and_ml_dependencies(path):
    offenders = sorted(
        name
        for name in _imported_names(path)
        if name.split(".")[0] in _FORBIDDEN_IN_DOMAIN
    )
    assert not offenders, (
        f"{path.name} depende de {offenders}. Eso es infraestructura: va en "
        "src/infrastructure/ y se inyecta (así se movió IsotonicCalibrator)."
    )
