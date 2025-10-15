class Extractor:
    """
    Clase para extraer datos de archivos fuente.
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def extract(self):
        import pandas as pd


        encodings = ['utf-8', 'latin-1', 'ISO-8859-1', 'cp1252']

        for enc in encodings:
            try:
                df = pd.read_csv(self.file_path, encoding=enc)
                print(f"Archivo leído correctamente con codificación: {enc}")
                return df
            except UnicodeDecodeError:
                continue
            except Exception as e:
                print(f"Error con la codificación {enc}: {e}")
                return None

        print("No se pudo leer el archivo con ninguna codificación común.")
        return None
