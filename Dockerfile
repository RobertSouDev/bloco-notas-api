FROM python:3.12-slim

WORKDIR /app

# Instalar PDM
RUN pip install --no-cache-dir pdm

# Configurar PDM
ENV PDM_IGNORE_SAVED_PYTHON=1

# Copiar arquivos de configuração do PDM
COPY pyproject.toml pdm.lock* ./

# Instalar dependências usando PDM
RUN pdm install --prod --no-lock

# Copiar código da aplicação
COPY . .

# Expor porta
EXPOSE 8000

# Comando para rodar a aplicação usando PDM
CMD ["pdm", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

