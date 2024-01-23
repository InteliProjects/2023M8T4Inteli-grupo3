# Script para subir dados no S3


## Descrição:


Esse pacote tem como objetivo realizar o upload de arquivos nos buckets criados na S3, responsáveis por armazenar todos os dados que podem ser utilizados para o cubo de dados. Com esse código será possível estabelecer uma conexão com AWS S3 e selecionar para qual bucket os arquivos serão enviados e de que pastas eles serão coletados. Além disso, vale mencionar que para esse envio é realizado um tratamento e padronização nos dados  padronizando todo o arquivo em apenas uma coluna "value" e adicionando  informações como data de ingestão e uso. Assim garantindo uma consistência entre os dados. 

## Classes


Para o código foram criadas 3 classes:


ConexaoAWS, no codigo aws_utils.py para estabelecer conexão com a aws e realizar o envio dos arquivos para o S3

ConexaoAzure, no codigo azure_utils.py para estabelecer conexão com a Azure e realizar o envio de arquivos para o Blob(para ser utilizado em uma futura implementação)

GerenciarBuckets, no código gerenciar_buckets.py, para informar os buckets disponíveis e auxiliar na seleção do bucket para envio dos arquivos

ManipuladorDataframe, essa nova classe foi criada com intuito de patronizar os dados no formato definido no topico de ETL, presente na documentação, assim padronizando todos os arquivos que serão enviados

TransformarCSV, essa classe e responsavel por realizar os pré-proscessamento e as traformações nescessarias nos dados.


## Como utilizar o pacote:


Para utilizar o pacote os seguintes passos devem ser seguidos.


1 - Garanta que o ambiente AWS labs no qual o projeto está sendo feito esteja sendo executado


2 - Pelo terminal acesse acesse a pasta em que se encontra esse read.me


3 - Instale o pacote

```py
  pip install .
```




4 - Execute o pacote

```py
  python3 -m pacote_script_upload_s3
```



5 - Forneça os dados requisitados requisitados por input


Chaves da AWS,Escolha de bucket e pasta de origem


6- Pronto seus dados foram enviados para o bucket desejado !




## Adequação ao Azure


Para uma futura implementação do código em um cloud Azure foi criada a classe ConexaoAzure no código azure_utils.py, nela estão funções para conexão ao Azure e envio de códigos para o Blob, ferramenta equivalente ao S3.


## Testes


Teste 1/teste_exibir_buckets(): Teste utilizado para verificar o funcionamento da função de exibir buckets


Teste 2/teste_exibir_buckets_error(): Teste utilizado para verificar se o código para exibição dos buckets está corretamente lidando com falhas


Teste 3/teste_fornecer_bucket(): Teste utilizado para verificar se a função para verificar o formato do bucket está corretamente funcionando


Teste 4/teste_fornecer_bucket_error(): Teste para verificar se a função a função para verificar o formato do bucket está lidando corretamente com inputs inadequados


Teste 5/teste_conectar_aws(): Teste para verificar se o código de conexão da AWS está efetuando corretamente a conexão


Teste 6/teste_conectar_aws_erro(): Teste para verificar se o código de conexão da AWS está lidando corretamente com erros de conexão


Teste 7/teste_enviar_arquivo_erro(): Teste para ver se o código de envio de arquivos para o S3 está lidando corretamente com erros de envio


Observação: foi evitado executar o código de envio para o S3 para evitar o envio de dados não utilizados e gastos com AWS S3.


## Como Executar os testes


Para executar os passos siga os seguintes passos:


1- No arquivo test_app.py, localizado na pasta de testes preencha as linhas com as suas informações:


chave_publica = ""


chave_privada = ""


session_token = ""


2 - Garanta que o ambiente AWS labs no qual o projeto está sendo feito esteja sendo executado


3 - Pelo terminal acesse acesse a pasta em que se encontra esse read.me

4- Instale o pytest

```py
  pip install pytest
```


5- Inicie os testes com a seguinte linha de comando:


```py
  pytest
```


5- Os resultados do sete testes aparecerão para você

6 - Exemplo(resultado obtido nos testes pelo grupo):

![image](https://github.com/2023M8T4Inteli/grupo3/assets/99202408/87bf72d8-79ce-448d-8ee8-958407e976de)



















