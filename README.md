# 📝 Bloco de Notas API

Uma API RESTful moderna para gerenciamento de notas, desenvolvida com **FastAPI**, **PostgreSQL** e **Redis**. Projeto educativo com arquitetura limpa e boas práticas.

## 🛠️ Stack Tecnológica

### Backend
- **Python 3.12+** - Linguagem principal
- **FastAPI** - Framework web moderno e rápido
- **Uvicorn** - Servidor ASGI de alta performance

### Banco de Dados & Cache
- **PostgreSQL** - Banco de dados relacional principal
- **Redis** - Cache em memória para otimização
- **SQLAlchemy** - ORM para comunicação com o banco

### Ferramentas & Infra
- **Docker** - Containerização dos serviços
- **Docker Compose** - Orquestração de containers
- **PDM** - Gerenciador de pacotes Python moderno
- **Swagger UI** - Documentação interativa automática

### Validação & Segurança
- **Pydantic** - Validação de dados e serialização
- **Python-dotenv** - Gerenciamento de variáveis de ambiente

## 🚀 Como Rodar o Projeto Localmente

### Pré-requisitos
- **Python 3.12 ou superior**
- **Docker e Docker Compose** instalados
- **Git** para clonar o repositório

### 📥 Passo 1: Clonar e Configurar

```bash
# Clone o projeto
git clone https://github.com/RobertSouDev/bloco-notas-api.git
cd bloco-notas-api

# Verifique a estrutura do projeto
ls -la
```

### 🔧 Passo 2: Configurar Ambiente e Variáveis
## Criar arquivo .env

```bash
# Crie o arquivo .env na raiz do projeto
touch .env
```

## Adicionar conteúdo ao .env:
```env
# Configurações do PostgreSQL
DATABASE_URL=postgresql://user:password@localhost:5432/notepad

# Configurações do Redis
REDIS_URL=redis://localhost:6379
```

## 🐳 Passo 3: Subir os Containers Docker
```bash
# Iniciar PostgreSQL e Redis
docker compose up -d

# Verificar se os containers estão rodando
docker ps

# Deve mostrar:
# postgres-notes (PostgreSQL na porta 5432)
# redis-notes (Redis na porta 6379)
```

## 📦 Passo 4: Configurar Ambiente Python
```bash
# Inicializar o PDM (se não tiver feito)
pdm init

# Instalar todas as dependências
pdm add fastapi uvicorn sqlalchemy psycopg2-binary redis python-dotenv pydantic

# Ou instalar baseado no pyproject.toml existente
pdm install
```
## 🎯 Passo 5: Executar a Aplicação
```bash
# Rodar a API com auto-reload para desenvolvimento
pdm run uvicorn app.main:app --reload

# A API estará disponível em: http://localhost:8000
```

# 📚 Documentação Interativa

```text
http://localhost:8000/docs
```

## Funcionalidades do Swagger:
* 📖 Documentação automática de todos os endpoints

* 🧪 Testar APIs diretamente na interface

* 📝 Ver exemplos de requests e responses

* 🔍 Explorar schemas de dados

<hr/>

# 🗂️ Estrutura do Projeto
```text
bloco-notas-api/
├── app/                           # Código fonte da aplicação
|   ├── services/
|       ├── cache.py                   # Configuração Redis
|       └── database.py                # Configuração PostgreSQL + SQLAlchemy
│   ├── __init__.py
│   ├── main.py                    # Aplicação FastAPI principal
│   ├── models.py                  # Modelos de dados (SQLAlchemy)
│   ├── schemas.py                 # Schemas Pydantic
│   ├── crud.py                    # Operações de banco (CREATE, READ, UPDATE, DELETE)
│   └── routes.py                  # Endpoints da API
├── docker-compose.yml             # Configuração Docker
├── .env                           # Variáveis de ambiente (CRIAR ESTE ARQUIVO)
├── .env.example                   # Exemplo de variáveis
├── pyproject.toml                 # Dependências e configuração PDM
├── pdm.lock                       # Lock das dependências
└── README.md                      # Este arquivo
```

## 🛣️ Endpoints da API

<table border="1">
  <thead>
    <tr>
      <th>Método</th>
      <th>Endpoint</th>
      <th>Descrição</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GET</td>
      <td>/</td>
      <td>Status da API</td>
      <td>200</td>
    </tr>
    <tr>
      <td>GET</td>
      <td>/health</td>
      <td>Health check</td>
      <td>200</td>
    </tr>
    <tr>
      <td>POST</td>
      <td>/api/v1/notas/</td>
      <td>Criar nova nota</td>
      <td>201</td>
    </tr>
    <tr>
      <td>GET</td>
      <td>/api/v1/notas/</td>
      <td>Listar todas as notas</td>
      <td>200</td>
    </tr>
    <tr>
      <td>GET</td>
      <td>/api/v1/notas/{id}</td>
      <td>Buscar nota por ID</td>
      <td>200</td>
    </tr>
    <tr>
      <td>PUT</td>
      <td>/api/v1/notas/{id}</td>
      <td>Atualizar nota</td>
      <td>200</td>
    </tr>
    <tr>
      <td>DELETE</td>
      <td>/api/v1/notas/{id}</td>
      <td>Deletar nota</td>
      <td></td>
    </tr>
  </tbody>
</table>

## 🧪 Exemplos de Uso
```bash
curl -X POST "http://localhost:8000/api/v1/notas/" \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Minha Primeira Nota",
    "conteudo": "Este é o conteúdo da minha nota de exemplo."
  }'
```
## Listar Todas as Notas

```bash
curl "http://localhost:8000/api/v1/notas/"
```

## Buscar Nota por ID

```bash
curl "http://localhost:8000/api/v1/notas/1"
```
## Atualizar uma Nota

```bash
curl -X PUT "http://localhost:8000/api/v1/notas/1" \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Título Atualizado",
    "conteudo": "Conteúdo atualizado com novas informações."
  }'
```

## Deletar uma Nota

```bash
curl -X DELETE "http://localhost:8000/api/v1/notas/1"
```
<br/>

#  Comandos Úteis
```bash
# Iniciar serviços
docker compose up -d

# Parar serviços
docker compose down

# Ver logs em tempo real
docker compose logs -f

# Ver status dos containers
docker ps

# Acessar PostgreSQL via terminal
docker exec -it postgres-notes psql -U user -d notepad

# Acessar Redis via terminal
docker exec -it redis-notes redis-cli
```

## Desenvolvimento

```bash
# Rodar com auto-reload
pdm run uvicorn app.main:app --reload

# Rodar em produção
pdm run uvicorn app.main:app --host 0.0.0.0 --port 8000

# Verificar dependências
pdm list

# Adicionar nova dependência
pdm add <package-name>
```
## Banco de Dados

```bash
# Conectar ao PostgreSQL
docker exec -it postgres-notes psql -U user -d notepad

# Comandos úteis no psql:
# \l - Listar bancos de dados
# \dt - Listar tabelas
# \d+ notas - Ver estrutura da tabela notas
# SELECT * FROM notas; - Ver todos os registros
```

# 🐛 Solução de Problemas
## Erro de Conexão com PostgreSQL
```shell
# Verificar se PostgreSQL está rodando
docker ps | grep postgres

# Se não estiver, reiniciar
docker compose restart postgres
```

## Erro de Conexão com Redis

```bash
# Testar conexão com Redis
docker exec redis-notes redis-cli ping
# Deve retornar: PONG
```

## Portas Ocupadas
```bash
# Verificar processos nas portas
sudo lsof -i :5432  # PostgreSQL
sudo lsof -i :6379  # Redis
sudo lsof -i :8000  # FastAPI
```

## Problemas com PDM

```bash
# Recriar ambiente virtual
pdm venv create
pdm install
```

### 👨‍💻 Autor
#### Robert Roger
#### Desenvolvedor full stack

### 📄 Licença
### Este projeto é para fins educacionais.

