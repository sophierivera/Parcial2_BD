import pandas as pd

class Transformer:
    """
    Clase para transformar y limpiar los datos de titulares de noticias.
    """
    def __init__(self, df):
        self.df = df

    def clean(self):
        df = self.df.copy()

        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

        df = df.dropna(subset=['Date', 'Label'])

        df = df.drop_duplicates()
        top_cols = [col for col in df.columns if col.startswith("Top")]
        for col in top_cols:
            df[col] = (
                df[col]
                .fillna('')
                .astype(str)
                .str.strip()
                .str.replace(r'\s+', ' ', regex=True)
            )

        df['Label'] = pd.to_numeric(df['Label'], errors='coerce').fillna(0).astype(int)

        self.df = df
        return self.df
