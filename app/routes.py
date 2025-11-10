from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, schemas
from .database import get_db

router = APIRouter()

@router.post("/notas/", response_model=schemas.NotaResponse)
def criar_nota(nota: schemas.NotaCreate, db: Session = Depends(get_db)):
    return crud.criar_nota(db=db, nota=nota)

@router.get("/notas/", response_model=List[schemas.NotaResponse])
def listar_notas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notas = crud.listar_notas(db, skip=skip, limit=limit)
    return notas

@router.get("/notas/{nota_id}", response_model=schemas.NotaResponse)
def obter_nota(nota_id: int, db: Session = Depends(get_db)):
    nota = crud.obter_nota_por_id(db, nota_id=nota_id)
    if nota is None:
        raise HTTPException(status_code=404, detail="Nota não encontrada")
    return nota
    