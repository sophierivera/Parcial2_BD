from Config.config import Config
from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader
from Visualize.plots import create_plots   # 👈 importamos las gráficas

def main():
    # Extraer datos
    extractor = Extractor(Config.INPUT_PATH)
    raw_data = extractor.extract()

    if raw_data is not None:
        # Transformar datos
        transformer = Transformer(raw_data)
        cleaned_data = transformer.clean()

        # Cargar datos
        loader = Loader(cleaned_data)
        loader.to_sqlite()

        # ✅ Guardar también el CSV limpio
        loader.to_csv("Extract/Files/results_clean.csv")

        # ✅ Generar las gráficas
        create_plots("Extract/Files/results_clean.csv")
    else:
        print("No se pudo extraer el archivo de datos.")

if __name__ == "__main__":
    main()


