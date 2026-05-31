<p align="center">
  <img src="logo_hria.png" width="300">
</p>
# HRIA — HR Intelligence & Bias Analysis

## Resumen Ejecutivo

HRIA (HR Intelligence & Bias Analysis) es un proyecto de análisis exploratorio de datos (EDA) desarrollado para DataTalent Solutions con el objetivo de diseñar programas de reskilling basados en evidencia y orientar a candidatos hacia las oportunidades más reales del mercado laboral de datos.

A partir del análisis de **19.725 ofertas de empleo** y fuentes complementarias del mercado español, identificamos qué perfiles ofrecen una mayor probabilidad de inserción laboral, qué habilidades son más demandadas, qué sectores generan más oportunidades y cuál es el retorno económico potencial de una transición profesional hacia los roles de datos.

### Hallazgos principales

* El **66% de las ofertas** corresponden a perfiles Mid-Senior.
* **Data Analyst** es la puerta de entrada más accesible para perfiles junior.
* El salto salarial de **Entry Level a Mid-Senior supera el 35%**.
* El mercado español prioriza habilidades como **Cloud Computing, Java, Python, Azure, Git y AWS**.
* El retorno económico estimado permite amortizar un programa de reskilling en menos de un año.

---

# Problema de Negocio

DataTalent Solutions necesitaba responder una pregunta estratégica:

> ¿Cómo diseñar un programa de reskilling alineado con la demanda real del mercado laboral y maximizar las oportunidades de colocación de sus alumnos?

Para ello era necesario comprender:

* Qué roles presentan mayor accesibilidad para nuevos profesionales.
* Qué habilidades técnicas demanda el mercado.
* Qué sectores concentran las oportunidades laborales.
* Qué retorno económico puede esperar un alumno.
* Qué limitaciones presentan los datos utilizados para tomar decisiones.

---

# Dataset Utilizado

### Dataset principal

* LinkedIn Job Postings Dataset (Kaggle)
* 19.725 ofertas analizadas
* Roles relacionados con datos y tecnología
* Información sobre:

  * Salarios
  * Seniority
  * Industrias
  * Skills
  * Aplicaciones y visualizaciones

### Fuentes complementarias

Para validar los resultados en el contexto español se incorporaron:

* Fundación Telefónica / OrientaHub (Infojobs, Tecnoempleo,etc)

Periodo analizado:

* LinkedIn Jobs 2024
* Mercado español: diciembre 2025 – abril 2026

---

# Metodología

El proyecto siguió un flujo completo de análisis exploratorio de datos (EDA).

## 1. Exploración

* Inspección de variables
* Identificación de tipos de datos
* Análisis descriptivo
* Evaluación de valores nulos

## 2. Limpieza

* Tratamiento de registros incompletos
* Normalización de categorías
* Validación de consistencia
* Revisión de outliers

## 3. Análisis

* Estadística descriptiva
* Comparaciones entre grupos
* Análisis salarial
* Análisis de skills
* Segmentación por industria
* Evaluación de competitividad

## 4. Sesgos

* Identificación de sesgos de selección
* Evaluación de datos faltantes
* Limitaciones geográficas
* Riesgos para la toma de decisiones

---

# Hallazgos Clave

## ¿Qué rol priorizar?

<!-- FASE 4 - VISUALIZACIÓN 10 -->
<!-- Accesibilidad Junior vs Salario -->

<p align="center">
  <img src="charts_phase4/viz10_accesibilidad_vs_salario.png" width="900">
</p>

<p align="center">
  <em>Figura 1. Accesibilidad de los principales roles de datos para perfiles junior.</em>
</p>
### Data Analyst es la mejor puerta de entrada

El 38,5% de las ofertas para Data Analyst son accesibles para perfiles junior, frente al 22% para Data Scientist y el 18% para Data Engineer.

### Implicación

La primera colocación es significativamente más probable comenzando por Data Analyst.

### Recomendación

Diseñar programas de entrada orientados a Data Analyst y utilizarlo como primer escalón profesional.

---

## ¿Qué salario esperar?

<!-- FASE 4 - VISUALIZACIÓN 9 -->
<!-- Salario mediano por rol -->

<p align="center">
  <img src="charts_phase4/viz9_salario_por_rol.png" width="900">
</p>

<p align="center">
  <em>Figura 2. Comparativa salarial entre Data Analyst, Data Engineer y Data Scientist.</em>
</p>

### El mayor salto salarial ocurre entre Entry y Mid-Senior

El incremento salarial estimado supera los 35.000 dólares anuales.

### Implicación

El valor económico del reskilling aparece principalmente al alcanzar niveles Mid-Senior.

### Recomendación

Comunicar el retorno económico del programa utilizando este tramo de progresión profesional.

---

## ¿Qué skills enseñar?

<!-- VALIDACIÓN MERCADO ESPAÑOL -->

<p align="center">
  <img src="charts_phase4/viz3_1_skills_spain.png" width="1000">
</p>

<p align="center">
  <em>Figura 3. Top skills técnicas demandadas en España.</em>
</p>

### El mercado español prioriza habilidades concretas

Top tecnologías identificadas:

1. Cloud Computing
2. Java
3. Python
4. JavaScript
5. Microsoft Azure
6. Git
7. AWS
8. Microservices
9. Docker
10. Artificial Intelligence

### Implicación

Las empresas demandan perfiles capaces de combinar programación, cloud y buenas prácticas de desarrollo.

### Recomendación

Construir el currículo sobre:

* Cloud
* Python
* Git
* Azure / AWS
* Metodologías ágiles
* Comunicación de datos

---

## ¿Qué industrias contratar?

Aunque IT Services lidera el volumen de contratación, existen oportunidades relevantes en:

* Healthcare
* Finance
* Manufacturing
* Defense

### Implicación

La especialización sectorial puede convertirse en una ventaja competitiva.

### Recomendación

Crear itinerarios específicos por industria.

---

## Competencia del Mercado

<p align="center">
  <img src="charts_phase4/viz5_scatter_vistas_solicitudes.png" width="900">
</p>

Solo el 39% de las ofertas muestran solicitudes reales.

Sin embargo, la correlación entre vistas y solicitudes alcanza:

**r = 0,72**

### Implicación

Las vistas pueden utilizarse como indicador universal de competitividad.

### Recomendación

Desarrollar servicios de inteligencia laboral basados en la dificultad estimada de cada oferta.

---

# Sesgos y Limitaciones

El análisis identifica ocho sesgos principales.

<!-- FASE 4 - VISTAS VS SOLICITUDES -->

<!-- INTRODUCCIÓN SESGOS -->

<p align="center">
  <img src="charts_phase4/viz_intro_sesgo.png" width="1000">
</p>

<p align="center">
  <em>Figura 5. Principales sesgos detectados en el dataset.</em>
</p>

## 1. Sesgo MNAR Salarial

* 68% de las ofertas no publican salario.
* Los salarios observados pueden estar sobreestimados.

## 2. Sesgo Geográfico

* 87% de las ofertas proceden de Estados Unidos.
* Los salarios no son directamente extrapolables a España.

## 3. Sesgo de Selección

* Predominio de grandes empresas con marca empleadora.

## 4. Ausencia de Variables Demográficas

* No es posible analizar diferencias por género.

## 5. Sesgo Temporal

* Datos concentrados en 2024.

## 6. Agregación de Skills

* Las categorías pueden ocultar tecnologías específicas.

## 7. Sesgo de Supervivencia

* No existen datos fiables de cierre de ofertas.

## 8. Solicitudes Subestimadas

* Solo una parte de las vacantes muestra aplicaciones reales.

### Conclusión

Los sesgos no invalidan el análisis.

Su identificación permite interpretar correctamente los resultados y evitar decisiones erróneas.

---

# Recomendaciones

1. Priorizar Data Analyst como puerta de entrada.
2. Diseñar itinerarios progresivos hacia Engineer y Scientist.
3. Construir el currículo sobre Cloud, Python, Git y tecnologías cloud.
4. Incorporar módulos de negocio y comunicación.
5. Crear especializaciones sectoriales.
6. Utilizar métricas de competitividad basadas en vistas.
7. Complementar el análisis con fuentes específicas del mercado español.

---

# Equipo

Proyecto desarrollado por el equipo HRIA para DataTalent Solutions.

**HRIA — HR Intelligence & Bias Analysis**

Análisis basado en evidencia para programas de reskilling y orientación profesional en el mercado de datos.
