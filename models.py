# models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Empresa(Base):
    __tablename__ = "empresas"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

class Maquina(Base):
    __tablename__ = "maquinas"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)

class Medicion(Base):
    __tablename__ = "mediciones"
    id = Column(Integer, primary_key=True, index=True)
    maquina_id = Column(Integer, ForeignKey("maquinas.id"), nullable=False)
    temperatura = Column(Float, nullable=False)
    presion     = Column(Float, nullable=False)
    voltaje     = Column(Float, nullable=False)
    corriente   = Column(Float, nullable=False)
    rpm         = Column(Float, nullable=False)
    timestamp   = Column(DateTime(timezone=True), server_default=func.now())
