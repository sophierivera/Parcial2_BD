from Config.config import Config
from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader
from Visualize.plots import create_plots
import os

def main():
    # Extraer datos
    extractor = Extractor(Config.INPUT_PATH)
    raw_data = extractor.extract()

    if raw_data is not None:
        # Limpiar los datos
        transformer = Transformer(raw_data)
        cleaned_data = transformer.clean()

        # Verificar que los datos limpios no están vacíos
        if cleaned_data.empty:
            print("Error: Los datos limpios están vacíos.")
            return

        # Crear la carpeta de destino para el archivo CSV si no existe
        os.makedirs(os.path.dirname(Config.OUTPUT_PATH), exist_ok=True)

        # Guardar los datos limpios en un archivo CSV
        loader = Loader(cleaned_data)
        print(f"Guardando archivo limpio en {Config.OUTPUT_PATH}")
        loader.to_csv(Config.OUTPUT_PATH)

        # Verificar si el archivo CSV se ha guardado
        if not os.path.exists(Config.OUTPUT_PATH):
            print(f"Error: No se ha encontrado el archivo CSV en {Config.OUTPUT_PATH}")
            return

        # Crear las gráficas
        print("Generando las gráficas...")
        create_plots(Config.OUTPUT_PATH)

    else:
        print("No se pudo extraer el archivo de datos.")

if __name__ == "__main__":
    main()
