from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TodoBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    concluido: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    concluido: Optional[bool] = None

class TodoResponse(TodoBase):
    id: int
    data_criacao: datetime
    data_atualizacao: datetime

    class Config:
        from_attributes = True