from sqlalchemy.orm import Session
from . import models, schemas

def criar_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def listar_todos(db: Session, skip: int = 0, limit: int = 100, concluido: bool = None):
    query = db.query(models.Todo)
    
    if concluido is not None:
        query = query.filter(models.Todo.concluido == concluido)
    
    todos = query.offset(skip).limit(limit).all()
    return todos

def obter_todo_por_id(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def atualizar_todo(db: Session, todo_id: int, todo_update: schemas.TodoUpdate):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    
    if db_todo:
        update_data = todo_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_todo, field, value)
        
        db.commit()
        db.refresh(db_todo)
        return db_todo
    return None

def deletar_todo(db: Session, todo_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    
    if db_todo:
        db.delete(db_todo)
        db.commit()
        return True
    return False