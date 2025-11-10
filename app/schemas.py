from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NotaBase(BaseModel):
    titulo: str
    conteudo: str

class NotaCreate(NotaBase):
    pass

class NotaResponse(NotaBase):
    id: int
    data_criacao: datetime

    class Config:
        from_attributes = True