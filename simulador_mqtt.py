# simulador_mqtt.py
import time, json, random
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT   = 1883
TOPIC  = "sensores/molienda"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

while True:
    payload = {
        "maquina_id": 1,
        "temperatura": round(random.uniform(60, 90), 2),
        "presion":     round(random.uniform(10, 20), 2),
        "voltaje":     round(random.uniform(210,230), 2),
        "corriente":   round(random.uniform(5,10),   2),
        "rpm":         round(random.uniform(1400,1600),2)
    }
    client.publish(TOPIC, json.dumps(payload))
    print("Dato publicado:", payload)
    time.sleep(3)
