import paho.mqtt.client as mqtt
import time
from datetime import datetime

light_state = "OFF"

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    client.subscribe("light/schedule")
    print("Subscribed to topic: light/schedule")

def on_message(client, userdata, msg):
    global light_state
    print(f"Received MQTT message on topic {msg.topic}: {msg.payload.decode()}")
    try:
        on_time, off_time = msg.payload.decode().split(',')
        print(f"Processing schedule: ON at {on_time}, OFF at {off_time}")
        while True:
            current_time = datetime.now().strftime('%H:%M:%S')
            if current_time == on_time and light_state != "ON":
                light_state = "ON"
                print(f"[{current_time}] Simulated Light: ON")
            elif current_time == off_time and light_state != "OFF":
                light_state = "OFF"
                print(f"[{current_time}] Simulated Light: OFF")
            time.sleep(1)
    except ValueError as e:
        print(f"Error parsing schedule: {e}")
    except Exception as e:
        print(f"Error: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Connecting to MQTT broker at localhost:1883")
try:
    client.connect("localhost", 1883, 60)
    client.loop_forever()
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")