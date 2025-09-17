import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración de estilo pastel
sns.set_palette("pastel")
sns.set_style("whitegrid")

# Crear carpeta de salida
output_dir = "Visualize/Plots"
os.makedirs(output_dir, exist_ok=True)

# Cargar dataset limpio
df = pd.read_csv("Extract/Files/results_clean.csv")

# -------------------- 📊 Gráfica 1: Cantidad de registros por tipo de vehículo --------------------
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="vehicle_type")
plt.title("Cantidad de viajes por tipo de vehículo")
plt.xlabel("Tipo de vehículo")
plt.ylabel("Cantidad de viajes")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(f"{output_dir}/viajes_por_tipo.png")
plt.close()

# -------------------- 📊 Gráfica 2: Promedio de tarifa por ciudad --------------------
avg_fare = df.groupby("city")["fare_amount"].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=avg_fare, x="city", y="fare_amount")
plt.title("Promedio de tarifa por ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Tarifa promedio")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(f"{output_dir}/promedio_tarifa_ciudad.png")
plt.close()

# -------------------- 📊 Gráfica 3: Distancia vs Tarifa --------------------
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="distance_km", y="fare_amount", alpha=0.6)
plt.title("Relación entre distancia y tarifa")
plt.xlabel("Distancia (km)")
plt.ylabel("Tarifa ($)")
plt.tight_layout()
plt.savefig(f"{output_dir}/distancia_vs_tarifa.png")
plt.close()

print(f"✅ Gráficas generadas en {output_dir}")



