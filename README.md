# Evaluación de la Calidad del Software a través del Diseño de Experimentos, Pruebas Combinatorias, Cobertura de Decisión y Análisis Estático - Por Brano Matute

Este repositorio contiene el desarrollo de actividades relacionadas con el **diseño de pruebas**, la **cobertura de código** y el **análisis estático**, aplicados tanto a una especificación de software mediante **Diseño de Experimentos (DOE)** como al algoritmo de búsqueda binaria desarrollado previamente. El proyecto incluye generación de casos de prueba con combinación por pares, medición de cobertura de decisión y detección de anomalías estructurales en el código.

Todas las herramientas necesarias están preinstaladas dentro de un **DevContainer**, por lo que no es necesario realizar instalaciones adicionales.

## Herramientas utilizadas

- **allpairspy** — Generación de casos de prueba usando combinación por pares (pairwise).
- **pytest** — Framework para ejecutar pruebas automatizadas.
- **pytest-cov** — Extensión para medir cobertura de código, incluyendo cobertura de decisión.
- **pylint** — Análisis estático del código para detectar anomalías.
- **pandas** — Manipulación de datos de apoyo en la generación y análisis de tablas.

## Comandos utilizados en la parte 1

- Ejecutar el script que genera los casos de prueba

**cd Parte1**


**python pairwise_ecommerce.py**


## Comandos utilizados en la parte 2  - Seccion 1

- Medir cobertura de código (incluye cobertura de decisión)

**cd Parte2/Seccion1**


**pytest --cov=busqueda_binaria --cov-branch**

- Generar reporte de cobertura en formato XML

**cd Parte2/Seccion1**


**pytest --cov=busqueda_binaria --cov-branch --cov-report=xml**


## Comandos utilizados en la parte 2  - Seccion 2

- Ejecutar análisis estático con Pylint y exportar el informe a un archivo .txt

**cd Parte2/Seccion2**


**pylint busqueda_binaria_anomalias.py > reporte_pylint.txt**
