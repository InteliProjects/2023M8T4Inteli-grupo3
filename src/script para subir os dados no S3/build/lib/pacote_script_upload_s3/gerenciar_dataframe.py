import datetime
import pandas as pd
import json
from io import BytesIO


class ManipuladorDataframe:

    def validar(self, arquivo_csv):
        if arquivo_csv.startswith("cnpj"):
            dfcnpj = pd.read_csv(arquivo_csv, sep=';')
            arquivobuffer = self.transformar_csv(dfcnpj)
            dfcnpj2 = pd.read_csv(arquivobuffer)
            return dfcnpj2
        else:
            return pd.read_csv(arquivo_csv)
        
        

    def padronizar_dataframe(self,dataframe, use, tag):
        df = dataframe.copy()
        df['value'] = df.apply(lambda row: json.loads(row.to_json()), axis=1)
        df['use'] = use
        df['tag'] = tag
        df['data_ingestao'] = datetime.datetime.now()
        df = df[['value', 'use', 'tag', 'data_ingestao']]
        return df
    
    def transformar_csv(self, dataframe):
        df = dataframe
        buffer = BytesIO()  
        df.to_csv(buffer, index=False)
        buffer.seek(0)  
        return buffer