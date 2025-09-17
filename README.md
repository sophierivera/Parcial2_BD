# ETLProject

## Descripción
Este proyecto implementa un pipeline ETL (Extract, Transform, Load) para procesar y limpiar datos de viajes de Uber, utilizando el dataset disponible en Kaggle: [Uber Ride Analytics Dashboard](https://www.kaggle.com/datasets/yashdevladdha/uber-ride-analytics-dashboard).

El objetivo es extraer los datos crudos, transformarlos mediante limpieza y normalización, y cargarlos en un archivo listo para análisis.

## Estructura del Proyecto

```
ETLProject/
├── Extract/
│   └── extractor.py
├── Transform/
│   └── transformer.py
├── Load/
│   └── loader.py
├── Config/
│   └── config.py
```

## Uso del DataFrame
El archivo principal de datos es `ncr_ride_bookings.csv`, que contiene información sobre reservas de viajes, cancelaciones, valoraciones, métodos de pago y más.

### Columnas principales:
- Date: Fecha de la reserva
- Time: Hora de la reserva
- Booking ID: Identificador único de la reserva
- Booking Status: Estado de la reserva (Completada, Cancelada, etc.)
- Customer ID: Identificador del cliente
- Vehicle Type: Tipo de vehículo
- Pickup Location: Origen
- Drop Location: Destino
- Avg VTAT: Tiempo promedio de llegada del vehículo
- Avg CTAT: Tiempo promedio de llegada del cliente
- Cancelled Rides by Customer: Cancelación por cliente
- Reason for cancelling by Customer: Motivo de cancelación por cliente
- Cancelled Rides by Driver: Cancelación por conductor
- Driver Cancellation Reason: Motivo de cancelación por conductor
- Incomplete Rides: Viaje incompleto
- Incomplete Rides Reason: Motivo de viaje incompleto
- Booking Value: Monto total del viaje
- Ride Distance: Distancia recorrida (km)
- Driver Ratings: Calificación al conductor
- Customer Rating: Calificación del cliente
- Payment Method: Método de pago

## Ejecución del pipeline ETL
1. Ajusta las rutas de entrada y salida en `Config/config.py` si es necesario.
2. Ejecuta el flujo ETL desde un script principal:

```python
from Config.config import Config
from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader

extractor = Extractor(Config.INPUT_PATH)
df = extractor.extract()
transformer = Transformer(df)
df_clean = transformer.clean()
loader = Loader(df_clean)
loader.to_csv(Config.OUTPUT_PATH)
```

Esto generará un archivo limpio listo para análisis o visualización.

## Fuente de datos
Dataset original: [Uber Ride Analytics Dashboard - Kaggle](https://www.kaggle.com/datasets/yashdevladdha/uber-ride-analytics-dashboard)