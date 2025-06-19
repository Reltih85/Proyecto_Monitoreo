# init_db.py
from database import engine, Base
from models import Empresa, Maquina, Medicion

# Esto va a ejecutar en la BD todas las sentencias CREATE TABLE necesarias
Base.metadata.create_all(bind=engine)
print("✅ Tablas creadas correctamente.")
