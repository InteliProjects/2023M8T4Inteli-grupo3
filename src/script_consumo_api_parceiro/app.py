import requests
import boto3
import csv
from io import StringIO

bucket_de_destino = "api--integrational-g3"
tabelas = ["sale","category","establishment"]
chave_aws = "ASIAVOHTC676K3PDL6XI"
chave_privada = ""
token = ""

class ConexaoAWS:
    def __init__(self, secret_key, aws_access_key_id):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = secret_key
        self.aws_session_token = token
        try:
            self.s3 = boto3.client('s3', aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key, aws_session_token=self.aws_session_token)
            print("Conexão bem-sucedida com a AWS S3.")
        except Exception as e:
            print("Ocorreu um erro ao conectar-se à AWS S3")

    def enviar_dados_csv(self, bucket, dados_csv, nome_arquivo):
        try:
            dados_encoded = dados_csv.encode('utf-8')
            self.s3.put_object(Bucket=bucket, Key=nome_arquivo, Body=dados_encoded)
            print(f"Dados CSV enviados com sucesso para o bucket '{bucket}' com o nome '{nome_arquivo}'.")
            return True
        except Exception as e:
            print("Erro ao enviar os dados CSV para o bucket:", e)
            return False

class ApiParceiro:
    def obter_dados_api(self,tabela):
        url = "https://intelifunctiongetdata.azurewebsites.net/api/InteliFunctionGetData"
        params = {
            "code": "pZh3gmJW_87epswrWDuB7CvQle-KqjsVh2ZJUaifiXd4AzFuOEy98w==",
            "table": tabela,
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Falha ao obter os dados. Código de status:", response.status_code)
            return None

    def dados_para_csv(self, dados):
        if not dados:
            return ""

        csv_buffer = StringIO()
        csv_writer = csv.DictWriter(csv_buffer, fieldnames=dados[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(dados)
        return csv_buffer.getvalue()

def iniciar_aplicacao():
    aws_access_key_id = chave_aws
    secret_key = chave_privada

    conexao_aws = ConexaoAWS(secret_key, aws_access_key_id)

    api_parceiro = ApiParceiro()

    for tabela in tabelas:
        dados_api = api_parceiro.obter_dados_api(tabela)

        if dados_api:
            dados_csv = api_parceiro.dados_para_csv(dados_api)
            nome_arquivo = f'dados_api_{tabela}.csv'
            bucket_escolhido = bucket_de_destino

            conexao_aws.enviar_dados_csv(bucket_escolhido, dados_csv, nome_arquivo)

if __name__ == "__main__":
    iniciar_aplicacao()
