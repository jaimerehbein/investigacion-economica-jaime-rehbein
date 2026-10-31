# Trazabilidad de evidencia

Estos registros están vacíos: el proyecto aún no tiene fuentes ni resultados verificados. No completar con ejemplos ficticios.

- `evidencias.csv`: una fila por dato, cita textual, paráfrasis empírica o afirmación basada en evidencia. Registrar el `source_id` central y ubicación precisa (página, tabla, figura, sección, serie o celda). Los datos derivados deben incluir método de extracción y transformaciones.
- `relaciones.csv`: vincula fuente y evidencia con una variable, figura, conclusión o entrada bibliográfica por sus identificadores.
- `registro_figuras.csv`: vincula cada figura con fuentes y evidencias, período, cobertura, unidad y metodología.
- `registro_conclusiones.csv`: vincula cada conclusión con la evidencia que la sustenta y declara su alcance.

## Estados de verificación

Usar `pendiente`, `verificada`, `verificada_parcial`, `no_verificada`, `inaccesible` o `descartada`. Marcar `verificada` solo después de cotejar el documento original; registrar persona y fecha de verificación. Una fuente verificada no valida automáticamente cada afirmación: cada fila de evidencia también se revisa.

El catálogo de fuentes está en [`../../../fuentes/registro_fuentes.csv`](../../../fuentes/registro_fuentes.csv). La bibliografía se construye con fuentes registradas; no mantener referencias sin `source_id`. Ver criterios en [`../../../metodologia/gestion-fuentes.md`](../../../metodologia/gestion-fuentes.md).
