from fastapi import FastAPI
from .services.database import engine, Base
from .routes import router
import os
from dotenv import load_dotenv

load_dotenv()


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bloco de Notas API",
    description="API para gerenciar notas com FastAPI, PostgreSQL e Redis",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")
@app.get("/")

def root():
    return {"message": "Bloco de Notas API está rodando!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)