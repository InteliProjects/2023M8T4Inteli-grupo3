import boto3

class ConexaoAWS:
    def __init__(self, secret_key, aws_access_key_id, token):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = secret_key
        self.aws_session_token = token
        try:
            self.s3 = boto3.client('s3', aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key, aws_session_token=self.aws_session_token)
            print("Conexão bem-sucedida com a AWS S3.")
        except Exception as e:
            return ("Ocorreu um erro ao conectar-se à AWS S3")

    # def enviar_arquivo(self, bucket, file):
    #     try:
    #         with open(file, 'rb') as dados:
    #             self.s3.upload_fileobj(dados, bucket, file)
    #         print(f"Arquivo '{file}' enviado com sucesso para o bucket '{bucket}'.")
    #         return (True)
    #     except Exception as e:
    #         return("Erro ao enviar o arquivo  para o bucket ")
    def enviar_arquivo(self, dados, bucket, file):
        try:
            self.s3.upload_fileobj(dados, bucket, file)
            print(f"Arquivo '{file}' enviado com sucesso para o bucket '{bucket}'.")
            return (True)
        except Exception as e:
            return("Erro ao enviar o arquivo  para o bucket ")