# Descrição

Essa função Lambda será responsável por deletar os dados do parceiro do S3, que devem ser expurgados a cada 15 dias. Para isso, a lambda precisará do nome do bucket em que esses dados estão armazenados, para assim poder apagar todos os arquivos contidos nesse bucket. Esse código utiliza a biblioteca boto3 para se comunicar com a AWS e um EventBrigde como trigger para ativar a função Lambda a cada 15 dias.