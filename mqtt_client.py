# mqtt_client.py
import logging
import paho.mqtt.client as mqtt

# Configura logging en DEBUG para ver todo el flujo MQTT
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s')
logger = logging.getLogger()

BROKER = "localhost"
PORT   = 1883
TOPIC  = "sensores/molienda"

def on_connect(client, userdata, flags, rc):
    print(f"✅ Conectado al broker MQTT con código: {rc}")
    client.subscribe(TOPIC)

def on_subscribe(client, userdata, mid, granted_qos):
    print(f"📡 Subscripción confirmada a '{TOPIC}' | mid={mid} qos={granted_qos}")

def on_message(client, userdata, msg):
    print(f"📨 Mensaje recibido en '{msg.topic}': {msg.payload.decode()}")

client = mqtt.Client()
# Enlaza el logger de Paho al logger de Python
client.enable_logger(logger)

client.on_connect   = on_connect
client.on_subscribe = on_subscribe
client.on_message   = on_message

print(f"🚀 Iniciando conexión a {BROKER}:{PORT}…")
client.connect(BROKER, PORT, keepalive=60)

# Loop para procesar red y callbacks
client.loop_forever()
