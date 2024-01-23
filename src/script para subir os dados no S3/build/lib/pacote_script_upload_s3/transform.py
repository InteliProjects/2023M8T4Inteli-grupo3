import pandas as pd
import json

class TransformarCSV:

    def __init__(self, arquivo_csv):
        self.arquivo_csv = arquivo_csv
        self.df = None

    def ler_csv(self):
        self.df = pd.read_csv(self.arquivo_csv)

    def transformar_json(self):
        self.df['value'] = self.df['value'].apply(json.loads)
        self.df = pd.json_normalize(self.df['value'])
        self.df.dropna()

    def limpar_nulos(self):
        self.df = self.df.dropna()