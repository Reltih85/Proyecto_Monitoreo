# crea_tablas.py
from database import engine, Base
from models import Empresa, Maquina, Medicion

# Esto leerá los __tablename__ y Column() de tus clases y generará las tablas
Base.metadata.create_all(bind=engine)
print("✅ Tablas creadas.")
