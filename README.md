# Monopoly Data Analytics

Proyecto de Analítica de Datos y Aprendizaje Automático enfocado en el estudio del comportamiento de los jugadores de Monopoly mediante simulaciones a gran escala.

---

# Descripción

Este proyecto tiene como objetivo analizar miles de partidas simuladas de Monopoly para identificar patrones de juego, estudiar el impacto de diferentes estrategias económicas y construir un modelo de Machine Learning capaz de predecir si un jugador perderá la partida.

Para ello, se utilizó un simulador desarrollado en Python que fue modificado para registrar el estado financiero y estratégico de cada jugador en cada turno. Posteriormente, los datos fueron procesados y analizados utilizando Databricks, PySpark, SQL y Scikit-learn.

---

# Objetivos

- Generar un conjunto de datos a partir de simulaciones de Monopoly.
- Analizar el comportamiento de los jugadores mediante preguntas de investigación.
- Identificar los factores que más influyen en el patrimonio de un jugador.
- Analizar la evolución económica durante las partidas.
- Construir un modelo predictivo utilizando Random Forest.
- Visualizar los resultados mediante un dashboard interactivo.

---

# Tecnologías utilizadas

- Python
- Pandas
- PySpark
- SQL
- Databricks
- Matplotlib
- Scikit-learn
- Git
- GitHub

---

# Conjunto de datos

Cada fila del conjunto de datos representa el estado de un jugador durante un turno específico de una partida.

## Variables principales

| Variable | Descripción |
|----------|-------------|
| game_id | Identificador de la partida |
| turn | Número de turno |
| player | Nombre del jugador |
| player_number | Número del jugador |
| position | Casilla actual del tablero |
| dice_value | Resultado del lanzamiento de dados |
| cash | Dinero disponible |
| mortgageable_amount | Valor hipotecable de las propiedades |
| net_worth | Patrimonio total del jugador |
| total_properties | Cantidad de propiedades |
| monopolies | Monopolios (grupos completos de color) |
| houses | Número de casas |
| hotels | Número de hoteles |
| bank_cash | Dinero restante del banco |
| has_lost | Variable objetivo que indica si el jugador perdió la partida |

---

# Análisis Exploratorio de Datos (EDA)

El análisis exploratorio se desarrolló a partir de preguntas de investigación específicas en lugar de gráficos descriptivos tradicionales.

Se analizaron aspectos como:

- Posiciones del tablero más visitadas.
- Relación entre la cantidad de propiedades y el patrimonio.
- Impacto de los monopolios sobre la riqueza del jugador.
- Contribución de cada tipo de activo al patrimonio.
- Variables con mayor correlación respecto al patrimonio.
- Características de los jugadores con mejor desempeño.
- Evolución del patrimonio a lo largo de la partida.

---

# Análisis mediante SQL

Se realizaron consultas analíticas utilizando SQL en Databricks para obtener indicadores relevantes sobre el comportamiento de las partidas.

Entre los análisis realizados se incluyen:

- Estadísticas descriptivas.
- Agregaciones.
- Rankings.
- Indicadores de rendimiento.
- Consultas comparativas entre jugadores.

---

# Modelo de Machine Learning

Se desarrolló un modelo de clasificación utilizando **Random Forest** para predecir si un jugador perderá la partida según su estado actual.

## Variables utilizadas

- Dinero disponible
- Patrimonio
- Propiedades
- Monopolios
- Casas
- Hoteles
- Activos hipotecables
- Posición en el tablero
- Visitas a la cárcel
- Otros indicadores estratégicos

## Algoritmo

- Random Forest Classifier
- Biblioteca: Scikit-learn
- Tipo de problema: Clasificación Binaria

---

# Dashboard

Como resultado final se construyó un dashboard interactivo en Databricks que resume los principales hallazgos del proyecto.

Incluye:

- Indicadores clave (KPIs)
- Visualizaciones del análisis exploratorio
- Resultados de consultas SQL
- Evolución del patrimonio
- Importancia de variables del modelo
- Resultados del modelo predictivo

---

# Resultados principales

Los análisis permitieron identificar que:

- La obtención de monopolios incrementa significativamente el patrimonio.
- Existe una fuerte relación entre la cantidad de propiedades y la riqueza del jugador.
- Algunas casillas presentan frecuencias de visita considerablemente mayores.
- El modelo Random Forest identifica correctamente las variables con mayor influencia sobre la probabilidad de perder una partida.

---

# Trabajo futuro

Como posibles extensiones del proyecto se plantean:

- Incorporar agentes con diferentes estrategias de juego.
- Implementar modelos de Reinforcement Learning.
- Comparar diferentes algoritmos de Machine Learning.
- Estimar probabilidades de victoria durante la partida.
- Simular partidas con más de dos jugadores.
- Desarrollar modelos de series temporales para estudiar la evolución del patrimonio.

---

# Referencias

- Reglas oficiales de Monopoly (Hasbro)
- Documentación de Databricks
- Documentación de Apache Spark
- Documentación de Scikit-learn

---

# Autor

**Alejandra González, German Guzzo, Philip NG, Alejandro Otero**

Universidad Tecnológica de Panamá

Facultad de Ingeniería de Sistemas Computacionales

2026
