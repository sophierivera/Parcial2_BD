# Análisis de Sentimiento de Noticias Financieras – DJIA Stock

## Descripción General

Este proyecto realiza un análisis de sentimiento sobre titulares de noticias relacionados con el índice **Dow Jones Industrial Average (DJIA)**.  
El objetivo es analizar cómo los sentimientos expresados en los medios financieros pueden reflejarse en la evolución del mercado bursátil.

El proyecto implementa un proceso **ETL (Extracción, Transformación y Carga)** para limpiar, analizar y visualizar los datos del conjunto de noticias financieras.

---

## Estructura del Proyecto

```
P2/
│
├── Config/
│   └── config.py
│
├── Extract/
│   ├── loader.py
│   └── Files/
│       ├── stock_sentiment_analysis.csv
│       └── stock_senti_analysis_clean.csv
│
├── Transform/
│   └── cleaner.py
│
├── Visualize/
│   └── plots.py
│
├── main.py
└── README.md
```

---

## Descripción del Proceso ETL

### 1. Extracción
Se lee el archivo fuente `stock_sentiment_analysis.csv` (dataset de Kaggle: *Sentiment Analysis for DJIA Stock*).  
El proceso detecta automáticamente la codificación correcta del archivo para evitar errores de lectura.

### 2. Transformación
- Limpieza de valores nulos y duplicados.  
- Conversión de la columna de fecha (`Date`) al formato estándar de `datetime`.  
- Normalización de etiquetas de sentimiento (`Label`).  
- Cálculo de métricas adicionales como la longitud promedio de titulares.  
- Generación de un archivo limpio `stock_senti_analysis_clean.csv` en `Extract/Files/`.

### 3. Carga y Visualización
Los datos procesados se visualizan mediante gráficos estadísticos que permiten observar:
- Distribución general de sentimientos.
- Tendencias mensuales del sentimiento promedio.
- Relación entre la longitud de los titulares y el sentimiento predominante.

Las gráficas se guardan automáticamente en la carpeta `Visualize/Plots/`.

---

## Instrucciones de Ejecución

1. Clona este repositorio o descárgalo localmente:
   ```bash
   git clone https://github.com/usuario/Trabajo4-Deportes.git
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta el proyecto:
   ```bash
   python3 main.py
   ```

4. Los resultados se almacenarán en:
   - `Extract/Files/stock_senti_analysis_clean.csv`
   - `Visualize/Plots/` (gráficas generadas)

---

## Resultados y Conclusiones

El análisis muestra una predominancia de sentimientos **neutros y positivos** en los titulares financieros del DJIA.  
Las tendencias mensuales sugieren que los cambios de sentimiento suelen correlacionarse con eventos macroeconómicos importantes.  
Este enfoque demuestra el potencial del análisis de texto para comprender la percepción del mercado y apoyar decisiones financieras.

---

## Fuente de Datos

**Dataset original:**  
[Sentiment Analysis for DJIA Stock - Kaggle](https://www.kaggle.com/code/shubhamptrivedi/sentiment-analysis-for-dow-jones-djia-stock/input)
