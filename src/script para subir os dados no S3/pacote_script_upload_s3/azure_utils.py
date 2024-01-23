from azure.storage.blob import BlobServiceClient, ContentSettings

class ConexaoAzure:
    def conectar_azure():
        account_name = 'sua-conta-azure'
        account_key = 'sua-chave-de-conta-azure'
        container_name = 'seu-container-azure'

        blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)
        container_client = blob_service_client.get_container_client(container_name)
        return container_client

    def enviar_arquivo_azure(cliente, caminho_local, blob_name):
        with open(caminho_local, 'rb') as data:
            cliente.upload_blob(name=blob_name, data=data, content_settings=ContentSettings(content_type='text/plain'))