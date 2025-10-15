class Config:
    """
    Clase de configuración para rutas y parámetros del ETL.
    """
    INPUT_PATH = 'Extract/Files/stock_senti_analysis.csv'
    SQLITE_DB_PATH = 'Extract/Files/stock_senti_analysis.db'
    SQLITE_TABLE = 'ride_bookings_clean'
    OUTPUT_PATH = 'Extract/Files/stock_senti_analysis_clean.csv'   
