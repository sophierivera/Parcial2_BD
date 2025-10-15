from Config.config import Config
import sqlite3
import os

class Loader:

    def __init__(self, df):
        self.df = df

    def to_csv(self, output_path):
        try:
            
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            self.df.to_csv(output_path, index=False)
            print(f"Datos guardados en {output_path}")
        except Exception as e:
            print(f"Error al guardar datos: {e}")
