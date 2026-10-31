# Investigación económica — Jaime Rehbein

Repositorio público de protocolos, documentos y análisis reproducibles en economía e investigación aplicada.

- **Autor:** Jaime Rehbein
- **Área:** Economía e investigación aplicada
- **País:** Chile
- **Estado inicial:** estructura y plantillas; no contiene investigaciones terminadas, resultados ni bases de datos.

## Índice de investigaciones

| Tema | Carpeta | Estado inicial |
|---|---|---|
| Economía regional de Aysén | [`investigaciones/01-economia-regional-aysen/`](investigaciones/01-economia-regional-aysen/) | Proyecto de investigación |
| Productividad y crecimiento económico | [`investigaciones/02-productividad-crecimiento/`](investigaciones/02-productividad-crecimiento/) | Proyecto de investigación |
| Desigualdad y distribución del ingreso | [`investigaciones/03-desigualdad-distribucion-ingreso/`](investigaciones/03-desigualdad-distribucion-ingreso/) | Proyecto de investigación |
| Salmonicultura y encadenamientos productivos | [`investigaciones/04-salmonicultura-encadenamientos/`](investigaciones/04-salmonicultura-encadenamientos/) | Proyecto de investigación |
| Economía pública y contratación municipal | [`investigaciones/05-economia-publica-contratacion-municipal/`](investigaciones/05-economia-publica-contratacion-municipal/) | Proyecto de investigación |
| Economía digital e inteligencia artificial | [`investigaciones/06-economia-digital-inteligencia-artificial/`](investigaciones/06-economia-digital-inteligencia-artificial/) | Proyecto de investigación |

## Principios editoriales y científicos

1. No se inventan datos, indicadores, fuentes, referencias, citas, fechas, resultados ni enlaces.
2. Toda fuente se verifica en el documento original, repositorio oficial o sitio del editor antes de registrarse.
3. Se distinguen pregunta, objetivos, hipótesis, método, resultados y conclusiones. Una hipótesis no es un hallazgo.
4. Los proyectos sin análisis ejecutado declaran expresamente que no tienen resultados.
5. Todo indicador publicado documenta procedencia, período, unidad, transformaciones y metodología.
6. Se respetan licencias, términos de uso, privacidad y restricciones de acceso. No se versionan datos personales ni bases restringidas.
7. El material demostrativo no se utiliza como evidencia. Si se incorpora para probar código, se marca exactamente **“DATOS FICTICIOS — SOLO DEMOSTRACIÓN”** y se mantiene fuera de los análisis sustantivos.
8. Los análisis se revisan por una persona; las herramientas de IA pueden asistir, pero no certificar fuentes ni publicar automáticamente.

El estándar completo está en [`metodologia/estandar-editorial.md`](metodologia/estandar-editorial.md).

## Estructura

```text
.
├── investigaciones/       # seis protocolos, uno por tema
├── metodologia/           # estándar, trazabilidad, publicación y reproducibilidad
├── plantillas/            # plantillas de protocolo y procedencia
├── fuentes/               # registro central de fuentes verificadas (inicialmente vacío)
├── herramientas/          # utilidades de validación sin dependencias externas
└── .gitignore
```

Cada carpeta de investigación incluye `README.md` y subcarpetas para gráficos, documentos, datos y código reproducible. Las carpetas comienzan vacías de evidencia: sus README explican qué debe incorporarse y qué no.

## Flujo de trabajo

1. Definir pregunta y alcance en el README del proyecto.
2. Buscar y verificar fuentes originales; registrar sus metadatos en `fuentes/registro_fuentes.csv` y en la ficha de procedencia del proyecto.
3. Documentar permisos, licencia y restricciones antes de descargar o redistribuir datos.
4. Crear un diccionario de variables y un plan de análisis antes de estimar.
5. Guardar código y notebooks reproducibles en `codigo/`; no incluir secretos, datos personales ni archivos con acceso restringido.
6. Ejecutar el análisis sobre los datos autorizados y registrar entorno, decisiones, resultados y limitaciones.
7. Someter el documento a revisión antes de cambiar su estado editorial.

La procedencia se registra en `fuentes/registro_fuentes.csv`; cada proyecto contiene `trazabilidad/evidencias.csv`, `trazabilidad/relaciones.csv`, `trazabilidad/registro_figuras.csv` y `trazabilidad/registro_conclusiones.csv`. Estos registros vinculan el documento original con localizadores, variables, figuras, bibliografía y conclusiones. Los formatos y estados se explican en [`metodologia/gestion-fuentes.md`](metodologia/gestion-fuentes.md). Los criterios para una eventual publicación están en [`metodologia/criterios-publicacion.md`](metodologia/criterios-publicacion.md).

## Reproducción

En esta etapa no hay análisis empíricos que reproducir ni dependencias científicas que instalar. La utilidad de validación usa solo la biblioteca estándar de Python:

```bash
python herramientas/validar_metadatos.py
```

Cuando un proyecto incorpore código, su README deberá declarar versión de Python, dependencias, instrucciones, entradas requeridas (sin incluir datos restringidos), salidas esperadas y pasos exactos para reproducirlo. Usar Jupyter Notebook cuando facilite la exposición del análisis; mantener la lógica reutilizable en módulos `.py`.

## Licencia

**No se asigna licencia todavía.** Se elegirá cuando se revisen las condiciones de uso de datos, documentos, código y materiales de terceros. Hasta entonces, no se debe asumir autorización para reutilizar o redistribuir esos materiales.

## Publicación en GitHub

Esta carpeta está preparada para ser un repositorio independiente. Para publicarla, inicializa Git dentro de esta carpeta, revisa el contenido y configura el remoto de GitHub. Antes de cada publicación, confirma que no se incluyeron datos restringidos, archivos personales, credenciales o fuentes sin verificar.
