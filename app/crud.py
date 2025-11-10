from sqlalchemy.orm import Session
from . import models, schemas
from .services.cache import get_redis
import json

redis_client = get_redis()

def criar_nota(db: Session, nota: schemas.NotaCreate):
    db_nota = models.Nota(**nota.model_dump())
    db.add(db_nota)
    db.commit()
    db.refresh(db_nota)
    
    
    redis_client.delete("notas:todas")
    
    return db_nota

def listar_notas(db: Session, skip: int = 0, limit: int = 100):
    
    cache_key = "notas:todas"
    cached = redis_client.get(cache_key)
    
    if cached:
        return json.loads(cached)
    
    notas = db.query(models.Nota).offset(skip).limit(limit).all()
    
    notas_dict = [{"id": nota.id, "titulo": nota.titulo, "conteudo": nota.conteudo, 
                   "data_criacao": nota.data_criacao.isoformat()} for nota in notas]
    redis_client.setex(cache_key, 300, json.dumps(notas_dict))
    
    return notas

def obter_nota_por_id(db: Session, nota_id: int):
    cache_key = f"nota:{nota_id}"
    cached = redis_client.get(cache_key)
    
    if cached:
        return json.loads(cached)
    
    nota = db.query(models.Nota).filter(models.Nota.id == nota_id).first()
    
    if nota:
        nota_dict = {"id": nota.id, "titulo": nota.titulo, "conteudo": nota.conteudo,
                     "data_criacao": nota.data_criacao.isoformat()}
        redis_client.setex(cache_key, 300, json.dumps(nota_dict))
    
    return nota


def atualizar_nota(db: Session, nota_id: int, nota_update: schemas.NotaCreate):
    db_nota = db.query(models.Nota).filter(models.Nota.id == nota_id).first()
    
    if db_nota:
        db_nota.titulo = nota_update.titulo
        db_nota.conteudo = nota_update.conteudo
        
        db.commit()
        db.refresh(db_nota)
        
        redis_client.delete("notas:todas")
        redis_client.delete(f"nota:{nota_id}")
        
        return db_nota
    return None

def deletar_nota(db: Session, nota_id: int):
    db_nota = db.query(models.Nota).filter(models.Nota.id == nota_id).first()
    
    if db_nota:
        db.delete(db_nota)
        db.commit()
        
        redis_client.delete("notas:todas")
        redis_client.delete(f"nota:{nota_id}")
        
        return True
    return False