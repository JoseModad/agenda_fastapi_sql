from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException

from crud.config.config import SessionLocal
from crud.models import models
from crud.schemas.schemas import *
from typing import List


agenda = APIRouter()

# Dependencia

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
        

# Mostrar contacto Agenda

def leer_contacto(db: Session, codigo: int):
    return db.query(models.Agenda).filter(models.Agenda.codigo == codigo).first()

@agenda.get("/agenda/{codigo}", tags = ["Agenda"], response_model = AgendaSalida)
def Mostrar_Contacto(codigo: int, db: Session = Depends(get_db)):
    tblAgenda = leer_contacto(db, codigo = codigo)
    if tblAgenda is None:
        raise HTTPException(status_code = 404, detail = "Contacto no encontrado")
    return tblAgenda


# Mostrar contactos Agenda


def leer_contactos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Agenda).offset(skip).limit(limit).all()


@agenda.get("/agenda/", tags = ["Agenda"], response_model = list[AgendaSalida])
def Mostrar_Contactos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tblAgenda = leer_contactos(db, skip = skip, limit = limit)
    return tblAgenda



# Crear contactos Agenda

def Crear_contacto_agenda(db: Session, agend: AgendaEntrada):
    tblAgenda = models.Agenda(nombre = agend.nombre, telefono = agend.telefono, correo = agend.correo)
    db.add(tblAgenda)
    db.commit()
    db.refresh(tblAgenda)
    return tblAgenda

@agenda.post("/agenda/{codigo}", tags = ["Agenda"], response_model = AgendaEntrada)
def Crear_Contacto(agend: AgendaEntrada, db: Session = Depends(get_db)):
    return Crear_contacto_agenda(db = db, agend = agend)
        
        
# Eliminar contacto Agenda

def eliminar_Contacto_Agenda(db: Session, codigo: int):
    tblAgenda = leer_contacto(db = db, codigo = codigo)
    db.delete(tblAgenda)
    db.commit()     


@agenda.delete("/agenda/{codigo}", tags = ["Agenda"])
def eliminar_Contacto(codigo: int, db: Session = Depends(get_db)):
    tblAgenda = leer_contacto(db, codigo = codigo)
    if not tblAgenda:
        raise HTTPException(status_code = 404, detail = "No se encontro ningun contacto para eliminar")
    try:
        eliminar_Contacto_Agenda(db = db, codigo = codigo)
    except Exception as e:
        raise HTTPException(status_code = 400, detail = "No se puede eliminar: {e}")
    return {"Estado de eliminacion": "Exito"}
        
        
        
        
        
        