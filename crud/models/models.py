from sqlalchemy import Column, Integer, String
from crud.config.config import Base

class Agenda(Base):
    __tablename__ = "Agenda"
    
    codigo = Column(Integer, primary_key = True, index = True)
    nombre = Column(String)
    telefono = Column(String)
    correo = Column(String)
    