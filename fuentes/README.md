# Registro central de fuentes

[`registro_fuentes.csv`](registro_fuentes.csv) es el catálogo central compartido por los seis proyectos. Por ahora contiene únicamente encabezados; no se han incorporado fuentes verificadas.

## Categorías

- `fuente_primaria`: documento, registro o conjunto de datos original producido por la entidad o persona responsable de la información (por ejemplo, microdatos/documentos originales o normativa).
- `fuente_secundaria`: compilación, informe, síntesis o análisis que reutiliza o interpreta fuentes originales.
- `literatura_academica`: artículo, libro, tesis o documento de investigación académica. La ficha también debe indicar si aporta evidencia original o sintetiza estudios previos.

La categoría describe el tipo de material consultado, no garantiza su calidad ni sustituye la verificación. No llamar “primaria” a una fuente solo porque presenta cifras.

## Campos de procedencia

El CSV registra autoría/institución, título y tipo documental; fecha de publicación y consulta; URL original/DOI; período estadístico; cobertura geográfica y poblacional; ubicación precisa (página, tabla o sección); versión, licencia/restricciones y proyectos relacionados.

`estado_verificacion` debe usar uno de estos valores: `pendiente`, `verificada`, `verificada_parcial`, `no_verificada`, `inaccesible` o `descartada`. Una fuente solo puede marcarse `verificada` tras cotejarla con el original. Registrar quién y cuándo hizo la verificación. Dejar vacío todo dato desconocido.

La trazabilidad entre una fuente, evidencia, variables, gráficos y conclusiones se documenta en `trazabilidad/` dentro de cada investigación. Ver [`../metodologia/gestion-fuentes.md`](../metodologia/gestion-fuentes.md).
