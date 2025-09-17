# ETLProject

## Descripción
Este proyecto implementa un pipeline ETL (Extract, Transform, Load) para analizar resultados de partidos de fútbol y generar visualizaciones con Seaborn y Matplotlib.

## Estructura del Proyecto

Trabajo4/
│── Config/      
│── Extract/      
│── Transform/      
│── Load/           
│── Visualize/    
│── main.py         
│── requirements.txt
│── README.md

```

## Uso del DataFrame
El archivo principal de datos es results.csv, que contiene información sobre partidos de fútbol internacionales, incluyendo torneos, equipos, resultados y condiciones del partido.

### Columnas principales:
- date: Fecha del partido
- home_team: Equipo local
- away_team: Equipo visitante
- home_score: Goles anotados por el equipo local
- away_score: Goles anotados por el equipo visitante
- tournament: Nombre del torneo
- city: Ciudad donde se jugó el partido
- country: País donde se jugó el partido
- neutral: Indica si el partido fue en campo neutral (True / False)

## Ejecución del pipeline ETL
1. Ajusta las rutas de entrada y salida en Config/config.py si es necesario.
2. Ejecuta el flujo ETL desde el script principal main.py o manualmente con:

```python
from Config.config import Config
from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader

# 1. Extraer datos
extractor = Extractor(Config.INPUT_PATH)
df = extractor.extract()

# 2. Transformar datos
transformer = Transformer(df)
df_clean = transformer.clean()

# 3. Cargar datos
loader = Loader(df_clean)
loader.to_csv(Config.OUTPUT_PATH)          # Guarda el CSV limpio
loader.to_sqlite(Config.SQLITE_DB_PATH)    # Guarda en SQLite

```

Esto generará un archivo limpio listo para análisis o visualización.

## Fuente de datos
Dataset original: [Resultados de futbol entre 1872 y 2017 - Kaggle](https://www.kaggle.com/datasets/ramnquintana/resultados-de-futbol-entre-1872-y-2017?resource=download)