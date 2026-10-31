# Gestión y verificación de fuentes

## Registro central

Mantener [`../fuentes/registro_fuentes.csv`](../fuentes/registro_fuentes.csv) como catálogo común. Una fila representa un documento, conjunto de datos o publicación efectivamente localizado; no crear filas hipotéticas ni completar campos por conjetura.

Campos: ID estable `id`; `categoria_fuente`; institución y autores; título y tipo documental; fecha de publicación y consulta; URL original/DOI; período estadístico; cobertura geográfica y poblacional; página/tabla/sección; versión; estado, persona y fecha de verificación; licencia, restricciones, ubicación permitida, proyectos y notas.

Categorías mutuamente distinguibles para este registro: `fuente_primaria`, `fuente_secundaria` y `literatura_academica`. La literatura académica debe señalar en notas si presenta investigación/datos originales o sintetiza evidencia previa; “académica” no significa automáticamente “fuente primaria”.

Usar fechas ISO `AAAA-MM-DD` cuando la fuente las declare. Dejar vacío lo desconocido. No confundir fecha de consulta, publicación, fecha de verificación y período estadístico.

## Verificación mínima

1. Abrir la fuente original y confirmar autoría, título y versión.
2. Confirmar que el enlace apunta al documento o conjunto concreto.
3. Registrar cobertura temporal, geográfica y poblacional.
4. Revisar licencia, términos, privacidad y posibilidad de redistribución.
5. Registrar fecha de consulta cuando el contenido pueda cambiar o no tenga versión persistente.
6. Guardar una copia solo si está permitido; conservar URL y metadatos cuando no lo esté.

No usar agregadores, resultados de buscador o resúmenes de terceros como sustituto de la fuente original si el original está disponible.

## Ledger de afirmaciones y relaciones

En cada proyecto, `trazabilidad/evidencias.csv` tiene una fila por dato reportado, cita o afirmación empírica. Debe incluir `source_id`, formulación exacta (o cita cotejada), valor/unidad cuando aplique, localizador de origen y `evidence_id`. No basta con que exista una fuente en la bibliografía: la afirmación concreta debe rastrearse al lugar de donde se obtuvo.

`trazabilidad/relaciones.csv` conecta source/evidence IDs con variables, figuras, entradas bibliográficas y conclusiones. `registro_figuras.csv` y `registro_conclusiones.csv` conservan la procedencia y el respaldo de esos elementos. Usar IDs estables y no reciclarlos.

## Estados de verificación

- `pendiente`: aún no cotejada.
- `verificada`: cotejada contra el original y localizador confirmado.
- `verificada_parcial`: algunos metadatos o elementos no pudieron comprobarse; explicar cuáles.
- `no_verificada`: se conoce una referencia, pero no se pudo confirmar su contenido/origen.
- `inaccesible`: original no accesible durante la revisión; no usar para respaldar una afirmación publicada.
- `descartada`: fuente inadecuada o registro erróneo; conservar nota de descarte en vez de reutilizar el ID.

Marcar como verificada una fuente no verifica automáticamente toda afirmación que se le atribuya. Cada evidencia debe cotejarse individualmente y registrar persona y fecha.
