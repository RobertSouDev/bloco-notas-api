from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from . import crud, schemas
from .services.database import get_db

router = APIRouter()

@router.post("/todos/", response_model=schemas.TodoResponse, status_code=201)
def criar_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.criar_todo(db=db, todo=todo)

@router.get("/todos/", response_model=List[schemas.TodoResponse])
def listar_todos(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    concluido: Optional[bool] = Query(None, description="Filtrar por status de conclusão"),
    db: Session = Depends(get_db)
):
    todos = crud.listar_todos(db, skip=skip, limit=limit, concluido=concluido)
    return todos

@router.get("/todos/{todo_id}", response_model=schemas.TodoResponse)
def obter_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.obter_todo_por_id(db, todo_id=todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo não encontrado")
    return todo

@router.put("/todos/{todo_id}", response_model=schemas.TodoResponse)
def atualizar_todo(todo_id: int, todo_update: schemas.TodoUpdate, db: Session = Depends(get_db)):
    todo_atualizado = crud.atualizar_todo(db, todo_id=todo_id, todo_update=todo_update)
    if todo_atualizado is None:
        raise HTTPException(status_code=404, detail="Todo não encontrado")
    return todo_atualizado

@router.patch("/todos/{todo_id}/concluir", response_model=schemas.TodoResponse)
def marcar_como_concluido(todo_id: int, db: Session = Depends(get_db)):
    todo_atualizado = crud.atualizar_todo(db, todo_id=todo_id, todo_update=schemas.TodoUpdate(concluido=True))
    if todo_atualizado is None:
        raise HTTPException(status_code=404, detail="Todo não encontrado")
    return todo_atualizado

@router.delete("/todos/{todo_id}", status_code=204)
def deletar_todo(todo_id: int, db: Session = Depends(get_db)):
    sucesso = crud.deletar_todo(db, todo_id=todo_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Todo não encontrado")
    return None