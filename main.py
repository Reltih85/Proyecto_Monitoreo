# main.py
from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Medicion
from schemas import MedicionSchema

app = FastAPI(title="API de Mediciones")

@app.get("/mediciones/", response_model=List[MedicionSchema])
def listar_mediciones(limit: int = 100, db: Session = Depends(get_db)):
    """
    Devuelve hasta `limit` mediciones más recientes.
    """
    resultados = (
        db.query(Medicion)
          .order_by(Medicion.timestamp.desc())
          .limit(limit)
          .all()
    )
    return resultados

@app.get("/mediciones/{medicion_id}", response_model=MedicionSchema)
def obtener_medicion(medicion_id: int, db: Session = Depends(get_db)):
    medicion = db.query(Medicion).get(medicion_id)
    if not medicion:
        raise HTTPException(status_code=404, detail="Medición no encontrada")
    return medicion
