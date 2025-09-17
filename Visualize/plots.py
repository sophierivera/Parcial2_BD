import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def create_plots(csv_path="Extract/Files/results_clean.csv", output_dir="Visualize"):
    # Cargar datos
    df = pd.read_csv(csv_path)

    # Crear carpeta si no existe
    os.makedirs(output_dir, exist_ok=True)

    # Estilo pastel
    sns.set_palette("pastel")
    plt.style.use("seaborn-v0_8-whitegrid")

    # === 1. Promedio de goles por torneo ===
    df["total_goals"] = df["home_score"] + df["away_score"]
    avg_goals_tournament = (
        df.groupby("tournament")["total_goals"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=avg_goals_tournament.values,
        y=avg_goals_tournament.index,
        palette="pastel"
    )
    plt.title("Promedio de goles por torneo (Top 10)", fontsize=14, weight="bold")
    plt.xlabel("Promedio de goles")
    plt.ylabel("Torneo")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "avg_goals_tournament.png"))
    plt.close()

    # === 2. Cantidad de partidos por país ===
    matches_country = df["country"].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=matches_country.values,
        y=matches_country.index,
        palette="pastel"
    )
    plt.title("Cantidad de partidos por país (Top 10)", fontsize=14, weight="bold")
    plt.xlabel("Cantidad de partidos")
    plt.ylabel("País")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "matches_by_country.png"))
    plt.close()

    # === 3. Partidos neutrales vs. no neutrales ===
    neutral_counts = df["neutral"].value_counts()

    plt.figure(figsize=(6, 6))
    plt.pie(
        neutral_counts,
        labels=["No Neutral", "Neutral"],
        autopct="%1.1f%%",
        colors=sns.color_palette("pastel"),
        startangle=90
    )
    plt.title("Distribución de partidos: neutrales vs. no neutrales", fontsize=14, weight="bold")
    plt.savefig(os.path.join(output_dir, "neutral_matches.png"))
    plt.close()

    print(f"✅ Gráficas pastel guardadas en {output_dir}/")


