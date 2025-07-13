# Usa uma imagem base oficial do Python
FROM python:3.10-slim-buster

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt primeiro para otimizar o cache do Docker
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o restante do código da sua aplicação para o diretório de trabalho
# Certifique-se de que gemini_proxy.py e outras pastas (imagens, styles) estejam na raiz do contexto do Docker
COPY . .

# Expõe a porta que a aplicação FastAPI vai usar (8000)
EXPOSE 8000

# Comando para rodar a aplicação usando Uvicorn
# Removido --reload para um ambiente de contêiner.
# Se seu arquivo principal é gemini_proxy.py, então 'gemini_proxy:app' está correto.
CMD ["python", "-m", "uvicorn", "gemini_proxy:app", "--host", "0.0.0.0", "--port", "8000"]