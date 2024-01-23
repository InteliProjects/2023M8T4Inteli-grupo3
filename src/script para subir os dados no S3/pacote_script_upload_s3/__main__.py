from . import *

buckets = ['pof--integrational-g3', 'api--integrational-g3', 'cnpj--integrational-g3']

def iniciar_aplicacao():
    aws_access_key_id = input("Sua chave pública AWS:")
    secret_key = input("Sua chave privada AWS: ")
    s_token = input("Seu token AWS: ")
    conexao_aws = aws_utils.ConexaoAWS(secret_key,aws_access_key_id,s_token)
    gerenciador_dataframe = gerenciar_dataframe.ManipuladorDataframe()
    gerenciador_buckets = gerenciar_buckets.GerenciarBuckets()
    gerenciador_buckets.exibir_buckets(buckets)

    escolha_bucket = input("Digite o nome do bucket para onde deseja enviar os arquivos: ")
    bucket_escolhido = gerenciador_buckets.definir_destino(buckets,escolha_bucket)

    if bucket_escolhido:
        dir_path = input("Digite o caminho da pasta de onde os arquivos devem ser enviados: ")
        os.chdir(dir_path)
        for file in os.listdir(dir_path):
            if os.path.isfile(file):
                df = gerenciador_dataframe.validar(file)
                df = gerenciador_dataframe.padronizar_dataframe(df,f'{file}',bucket_escolhido)
                dados = gerenciador_dataframe.transformar_csv(df)
                conexao_aws.enviar_arquivo(dados, bucket_escolhido, file)
                print(f'{file} enviado para o bucket {bucket_escolhido} com sucesso.')
            else:
                return print(f'{file} não é um arquivo válido.')
        return print('Todos os arquivos foram enviados com sucesso.')
    
iniciar_aplicacao()
