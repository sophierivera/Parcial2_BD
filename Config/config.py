class Config:
    """
    Clase de configuración para rutas y parámetros del ETL.
    """
    INPUT_PATH = 'Extract/results.csv'
    SQLITE_DB_PATH = 'Extract/results.db'
    SQLITE_TABLE = 'ride_bookings_clean'