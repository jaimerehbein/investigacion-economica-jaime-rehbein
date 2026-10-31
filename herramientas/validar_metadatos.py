#!/usr/bin/env python3
"""Comprueba que cada proyecto conserve las secciones científicas mínimas.

La herramienta valida estructura documental, no la veracidad de los datos ni
la calidad de una investigación. La verificación de fuentes requiere revisión
humana contra los documentos originales.
"""

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "investigaciones"
REQUIRED_HEADINGS = (
    "Pregunta de investigación",
    "Objetivos",
    "Hipótesis",
    "Revisión de literatura",
    "Marco teórico",
    "Metodología",
    "Diccionario de variables",
    "Fuentes de información",
    "Análisis empírico",
    "Resultados",
    "Limitaciones",
    "Conclusiones",
    "Bibliografía",
)
REQUIRED_DIRS = ("graficos", "documentos", "datos", "codigo")
TRACEABILITY_FILES = (
    "README.md",
    "evidencias.csv",
    "relaciones.csv",
    "registro_figuras.csv",
    "registro_conclusiones.csv",
)
SOURCE_REGISTRY = ROOT / "fuentes" / "registro_fuentes.csv"


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        return reader.fieldnames or [], list(reader)


def main() -> int:
    errors: list[str] = []
    projects = sorted(path for path in PROJECTS.iterdir() if path.is_dir())

    if not SOURCE_REGISTRY.is_file():
        print("ERROR: falta el registro central de fuentes.")
        return 1

    source_fields, source_rows = read_csv(SOURCE_REGISTRY)
    if "id" not in source_fields or "estado_verificacion" not in source_fields:
        errors.append("registro_fuentes.csv: faltan columnas obligatorias")
    source_ids = [row.get("id", "").strip() for row in source_rows]
    if len(source_ids) != len(set(source_ids)):
        errors.append("registro_fuentes.csv: hay IDs de fuente duplicados")
    known_source_ids = {source_id for source_id in source_ids if source_id}

    if not projects:
        print("ERROR: no se encontraron carpetas de investigación.")
        return 1

    for project in projects:
        readme = project / "README.md"
        if not readme.is_file():
            errors.append(f"{project.name}: falta README.md")
            continue

        content = readme.read_text(encoding="utf-8").casefold()
        for heading in REQUIRED_HEADINGS:
            if heading.casefold() not in content:
                errors.append(f"{project.name}: falta sección '{heading}'")

        for directory in REQUIRED_DIRS:
            if not (project / directory / "README.md").is_file():
                errors.append(
                    f"{project.name}: falta {directory}/README.md"
                )

        trace_dir = project / "trazabilidad"
        for filename in TRACEABILITY_FILES:
            if not (trace_dir / filename).is_file():
                errors.append(f"{project.name}: falta trazabilidad/{filename}")

        evidence_file = trace_dir / "evidencias.csv"
        if evidence_file.is_file():
            fields, rows = read_csv(evidence_file)
            if "source_id" not in fields or "evidence_id" not in fields:
                errors.append(
                    f"{project.name}: evidencias.csv no contiene IDs requeridos"
                )
            for row_number, row in enumerate(rows, start=2):
                source_id = row.get("source_id", "").strip()
                if not source_id or source_id not in known_source_ids:
                    errors.append(
                        f"{project.name}: evidencia fila {row_number} refiere fuente inexistente"
                    )

    if errors:
        print("Validación estructural: ERROR")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validación estructural y de referencias: OK ({len(projects)} proyectos).")
    print(
        "Nota: valida estructura e IDs; no comprueba la veracidad de fuentes, "
        "evidencias o conclusiones."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
