# subscriber.py
import json
import paho.mqtt.client as mqtt
from database import SessionLocal
from models import Medicion

BROKER = "localhost"
TOPIC  = "sensores/molienda"

def on_connect(client, userdata, flags, rc):
    print("✅ Conectado al broker MQTT con código:", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("📨 Mensaje recibido:", data)

    db = SessionLocal()
    try:
        # Asume que tu payload trae exactamente los campos de Medicion
        medicion = Medicion(**data)
        db.add(medicion)
        db.commit()
        print(f"   ↳ Guardado en BD con id={medicion.id}")
    except Exception as e:
        print("   ❌ Error al insertar en BD:", e)
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    print(f"🚀 Conectando a {BROKER}:1883…")
    client.connect(BROKER, 1883, 60)
    client.loop_forever()
