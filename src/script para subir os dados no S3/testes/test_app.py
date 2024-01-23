import pacote_script_upload_s3 as pacote

chave_publica = ""
chave_privada = ""
session_token = ""


gerenciador_buckets = pacote.gerenciar_buckets.GerenciarBuckets()
def teste_exibir_buckets():
    buckets = ['base-de-dados-integrational-g3', 'cnpj-integrational-g3', 'dados-ibge-integrational-g3', 'inep-integrational-g3', 'microdados-rais-caged-integrational-g3', 'pof-ibge-integrational-g3', 'pof-parceiro-integrational-g3', 'receita-federal-integrational-g3', 'sus-integrational-g3', 'zip-postal-integrational-g3']
    assert type(gerenciador_buckets.exibir_buckets(buckets)) == list  
    assert len(gerenciador_buckets.exibir_buckets(buckets)) == len(buckets)

def teste_exibir_buckets_error():
    buckets = "certamente nao e uma lista"
    assert gerenciador_buckets.exibir_buckets(buckets) == "Error: Lista de buckets inválida"

def teste_fornecer_bucket():
    buckets = ['base-de-dados-integrational-g3', 'cnpj-integrational-g3']
    bucket_fornecido = 'base-de-dados-integrational-g3'
    resposta_bucket = gerenciador_buckets.definir_destino(buckets,bucket_fornecido)
    assert bucket_fornecido == resposta_bucket
    
def teste_fornecer_bucket_error():
    buckets = ['base-de-dados-integrational-g3', 'cnpj-integrational-g3']
    bucket_fornecido = 'bucket incorreto'
    resposta_bucket = gerenciador_buckets.definir_destino(buckets,bucket_fornecido)
    assert resposta_bucket == None
    
def teste_conectar_aws():
    conexao = pacote.aws_utils.ConexaoAWS(chave_publica,chave_privada,session_token)
    assert conexao != None

def teste_conectar_aws_erro():
    conexao = pacote.aws_utils.ConexaoAWS([1,2,3,4],[1,2,3,4],[1,2,3,4])
    conexao == "Ocorreu um erro ao conectar-se à AWS S3"
    
def teste_enviar_arquivo_erro():
    conexao = pacote.aws_utils.ConexaoAWS(chave_publica,chave_privada,session_token)
    assert conexao.enviar_arquivo('base-de-dados-integrational-g3','teste.csv') == "Erro ao enviar o arquivo  para o bucket "
    

    

    
    
