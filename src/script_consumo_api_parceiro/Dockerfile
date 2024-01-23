# Use a imagem base do Python
FROM python:3.10.6-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos para o diretório de trabalho
COPY . .

# Comando para executar a aplicação quando o contêiner iniciar
CMD ["python", "app.py"]