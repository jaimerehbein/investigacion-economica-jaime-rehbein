# Reproducibilidad

Cada análisis debe poder ejecutarse desde un entorno limpio y explicar:

- versión de Python y sistema operativo probado;
- dependencias y versiones, idealmente fijadas una vez que el proyecto las use;
- comandos en orden, desde preparación hasta tablas y gráficos;
- ubicación y procedencia de cada entrada;
- transformaciones, filtros, unidades y tratamiento de faltantes;
- ubicación y formato de salidas;
- semilla aleatoria solo si el método realmente utiliza aleatoriedad;
- pasos que requieren acceso autorizado fuera del repositorio.

## Python y Jupyter

- Mantener funciones reutilizables en módulos `.py`; utilizar notebooks para exposición y exploración documentada.
- Reiniciar el kernel y ejecutar todas las celdas antes de publicar un notebook.
- Evitar rutas absolutas, tokens, credenciales y datos personales.
- No guardar datos restringidos en outputs del notebook.
- Declarar las entradas esperadas; no incluir datos hasta comprobar sus condiciones de uso.
- Separar datos originales inmutables, datos procesados y salidas; no sobrescribir el original.

Por ahora, el repositorio solo incluye una utilidad de metadatos que usa la biblioteca estándar. No hay análisis empíricos ni notebooks con resultados.
