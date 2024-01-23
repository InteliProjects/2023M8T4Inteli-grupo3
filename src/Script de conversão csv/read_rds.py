import os
import pandas as pd
import pyreadr

def converter(pasta_de_arquivos):
    for arquivo in os.listdir(pasta_de_arquivos):
        if arquivo.endswith(".rds"):
            df = pyreadr.read_r(os.path.join(pasta_de_arquivos, arquivo))
            df[None].to_csv(os.path.join(pasta_de_arquivos, arquivo[:-4] + ".csv"), index=False)
    print("Conversão concluída!")
    
print("digite o caminho da sua pasta de arquivos:")
converter(input())