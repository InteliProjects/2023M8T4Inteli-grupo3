import boto3

def lambda_handler(event, context):
    # Nome do bucket
    bucket_name = 'teste--lambda--rafa'

    # Criação de uma instância do cliente S3
    s3_client = boto3.client('s3')

    # Listagem de objetos no bucket
    objects = s3_client.list_objects(Bucket=bucket_name)

    # Verifica se há objetos no bucket
    if 'Contents' in objects:
        # Exclui cada objeto no bucket
        for obj in objects['Contents']:
            s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])

    return {
        'statusCode': 200,
        'body': 'Todos os arquivos foram removidos do bucket.'
    }