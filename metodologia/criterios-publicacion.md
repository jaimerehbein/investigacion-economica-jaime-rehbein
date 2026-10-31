# Criterios mínimos para considerar una investigación lista para publicación

Este checklist es una condición editorial mínima, no una certificación de calidad científica ni una revisión por pares. La investigación conserva el estado **Proyecto de investigación** hasta que todos los criterios aplicables estén documentados y una persona autora revise la versión final.

## 1. Pregunta y alcance

- [ ] Pregunta, objetivos, población/unidad de análisis, cobertura geográfica y período están definidos.
- [ ] Se distingue con claridad qué está dentro y fuera del alcance.
- [ ] Hipótesis (si aplica), mecanismos y resultados esperados están separados de los resultados observados.

## 2. Literatura, conceptos y referencias

- [ ] Revisión de literatura y marco teórico usan referencias existentes, verificadas en su fuente original.
- [ ] Cada referencia bibliográfica tiene un `source_id` en el registro central.
- [ ] Autoría, título, revista/editor, fecha, páginas, URL/DOI y versión coinciden con el original; campos no disponibles quedan declarados.
- [ ] Las citas textuales fueron cotejadas y señalan página o sección.

## 3. Fuentes, datos e indicadores

- [ ] Cada conjunto de datos tiene institución/productor, título, URL/identificador, fecha/versión, fecha de consulta cuando aplique y condiciones de uso registradas.
- [ ] Período estadístico, cobertura geográfica y poblacional, unidad, definiciones y fuente de cada variable están documentados.
- [ ] Se registran en el ledger las páginas, tablas, secciones, series o celdas de origen para afirmaciones y valores reportados.
- [ ] Restricciones, licencias, privacidad y permisos permiten el análisis y la publicación prevista.
- [ ] No se incluyen datos personales ni microdatos restringidos; datos no redistribuibles no se suben al repositorio.
- [ ] Valores faltantes, revisiones, rupturas de serie y transformaciones están descritos.

## 4. Método y reproducibilidad

- [ ] Diseño, estrategia de identificación/estimación, supuestos y limitaciones son explícitos.
- [ ] El código corre desde un entorno limpio con instrucciones y dependencias declaradas.
- [ ] Entradas, filtros, transformaciones y salidas se pueden rastrear; los datos originales no se sobrescriben.
- [ ] Notebooks, si se usan, fueron reiniciados y ejecutados de principio a fin; no contienen secretos ni datos restringidos en outputs.
- [ ] Las tablas y figuras se generan desde el código citado o se identifica de forma transparente cualquier elaboración manual.

## 5. Resultados, figuras y conclusiones

- [ ] Cada afirmación empírica se vincula a uno o más `evidence_id` y `source_id`.
- [ ] Cada figura declara fuentes, período, unidad, cobertura, metodología y notas; sus series y transformaciones son reproducibles.
- [ ] Los resultados corresponden a análisis efectivamente ejecutados; se distinguen estimaciones, asociaciones e inferencias causales.
- [ ] Conclusiones y recomendaciones tienen referencias a evidencia registrada y respetan su alcance.
- [ ] Resultados nulos, incertidumbre, robustez y limitaciones relevantes no se omiten.
- [ ] Los datos de prueba, si excepcionalmente se usan, llevan exactamente **“DATOS FICTICIOS — SOLO DEMOSTRACIÓN”** y no se presentan como evidencia.

## 6. Transparencia y decisión editorial

- [ ] README, fecha/versión, estado editorial, fuentes y método están actualizados.
- [ ] No quedan marcadores `Pendiente`, referencias sin verificar ni afirmaciones empíricas huérfanas.
- [ ] Se declaran financiación, conflictos de interés y asistencia de herramientas de IA cuando corresponda; la persona autora verifica y asume responsabilidad.
- [ ] Se ha elegido una licencia solo después de revisar derechos de código, datos, documentos y figuras de terceros.
- [ ] Revisión final de autoría completada; se registra persona revisora y fecha, sin describirla como revisión por pares si no lo fue.

## Transición de estado

Completar el checklist no convierte por sí solo un trabajo en “Publicado”. La persona autora debe seleccionar y declarar el estado correcto: **Borrador**, **En revisión**, **Publicado**, **Proyecto de investigación** o **Documento de trabajo**. Si existe cualquier criterio sustantivo pendiente, conservar un estado preliminar y explicar el pendiente.
