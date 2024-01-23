class GerenciarBuckets:
    def exibir_buckets(self, buckets):

        if not isinstance(buckets, list):
            return "Error: Lista de buckets inválida"

        print("Lista de Buckets:")
        for i, bucket in enumerate(buckets):
            print(f"{i + 1}. {bucket}")
        return buckets

    def definir_destino(self, buckets, bucket_escolhido_usuario):
        bucket_escolhido = bucket_escolhido_usuario 
        if bucket_escolhido not in buckets:
            print("O nome do bucket inserido não está na lista de buckets. Por favor, insira um nome de bucket válido.")
            return None
        return bucket_escolhido