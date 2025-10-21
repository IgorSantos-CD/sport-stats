#=============================
#DOCKERFILE - DESENVOLVIMENTO
#=============================

FROM python:3.13-slim

#Definindo diretório de trabalho
WORKDIR /app

#Evita criação de arquivos .pyc e melhora logs
ENV PYHTONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#Copia apenas o arquivo de configuração do Poetry
COPY pyproject.toml poetry.lock* ./

#Instala o Poetry
RUN pip install --no-cache-dir poetry

#Instala dependencias no sistema
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# Copia o restante do projeto
COPY . .

#Expõe a porta do FastAPI
EXPOSE 8000

#Comando padrão
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]