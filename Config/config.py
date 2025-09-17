class Config:
    """
    Clase de configuración para rutas y parámetros del ETL.
    """
    INPUT_PATH = 'Extract/Files/results.csv'
    SQLITE_DB_PATH = 'Extract/Files/results.db'
    SQLITE_TABLE = 'ride_bookings_clean'
    OUTPUT_PATH = 'Extract/Files/results_clean.csv'   # 👈 CSV limpio
