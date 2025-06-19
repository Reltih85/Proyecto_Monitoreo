# schemas.py
from pydantic import BaseModel
from datetime import datetime

class MedicionSchema(BaseModel):
    id: int
    maquina_id: int
    temperatura: float
    presion: float
    voltaje: float
    corriente: float
    rpm: float
    timestamp: datetime

    class Config:
        orm_mode = True
