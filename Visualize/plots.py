import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from Config.config import Config

sns.set_palette("pastel")
sns.set_style("whitegrid")

def create_plots(output_path=None):
    output_path = output_path or Config.OUTPUT_PATH
    output_dir = "Visualize/Plots"
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(output_path):
        print(f"Error: el archivo {output_path} no existe.")
        return

    df = pd.read_csv(output_path)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])

    # - 1. Distribución de etiquetas -
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x="Label", hue="Label", palette="pastel", legend=False)
    plt.title("Distribución de sentimientos")
    plt.xlabel("Etiqueta (0 = Negativo, 1 = Positivo)")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/01_distribucion_etiquetas.png")
    plt.close()

    # - 2. Promedio de titulares por trimestre -
    df["num_headlines"] = df[[col for col in df.columns if col.startswith("Top")]].notnull().sum(axis=1)
    headlines_per_date = df.groupby(pd.Grouper(key="Date", freq="QE"))["num_headlines"].mean().reset_index()

    plt.figure(figsize=(9, 5))
    sns.lineplot(data=headlines_per_date, x="Date", y="num_headlines", marker="o", linewidth=2.2)
    plt.title("Promedio de titulares por trimestre")
    plt.xlabel("Fecha")
    plt.ylabel("Promedio de titulares")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/02_titulares_trimestre.png")
    plt.close()

    # - 3. Longitud promedio de titulares -
    top_cols = [col for col in df.columns if col.startswith("Top")]
    df["avg_title_length"] = df[top_cols].apply(
        lambda row: sum(len(str(x).split()) for x in row if isinstance(x, str) and x.strip()) / 
                    sum(1 for x in row if isinstance(x, str) and x.strip()) if any(isinstance(x, str) for x in row) else 0,
        axis=1
    )
    title_length_per_date = df.groupby(pd.Grouper(key="Date", freq="QE"))["avg_title_length"].mean().reset_index()

    plt.figure(figsize=(9, 5))
    sns.lineplot(data=title_length_per_date, x="Date", y="avg_title_length", marker="o", color="teal", linewidth=2.2)
    plt.title("Longitud promedio de titulares (trimestral)")
    plt.xlabel("Fecha")
    plt.ylabel("Palabras promedio por titular")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/03_longitud_titulares.png")
    plt.close()

    # - 4. Tendencia de sentimiento -
    sentiment_trend = (
        df.groupby([pd.Grouper(key="Date", freq="QE"), "Label"]).size().reset_index(name="count")
    )
    plt.figure(figsize=(9, 5))
    sns.lineplot(data=sentiment_trend, x="Date", y="count", hue="Label", linewidth=2.2, marker="o")
    plt.title("Tendencia de sentimiento por trimestre")
    plt.xlabel("Fecha")
    plt.ylabel("Cantidad de noticias")
    plt.legend(title="Sentimiento", labels=["Negativo (0)", "Positivo (1)"])
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/04_tendencia_sentimiento.png")
    plt.close()

    # - 5. Comparación titulares vs longitud -
    merged = pd.merge(headlines_per_date, title_length_per_date, on="Date")
    plt.figure(figsize=(9, 5))
    ax1 = plt.gca()
    sns.lineplot(data=merged, x="Date", y="num_headlines", ax=ax1, color="purple", linewidth=2.2, label="Titulares")
    ax2 = ax1.twinx()
    sns.lineplot(data=merged, x="Date", y="avg_title_length", ax=ax2, color="teal", linewidth=2.2, label="Longitud")
    ax1.set_xlabel("Fecha")
    ax1.set_ylabel("Titulares promedio", color="purple")
    ax2.set_ylabel("Longitud promedio", color="teal")
    plt.title("Comparación titulares vs longitud promedio (trimestral)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/05_comparacion_titulares_longitud.png")
    plt.close()

    print(f"Gráficas más limpias y legibles generadas en {output_dir}")
