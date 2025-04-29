import asyncio
import websockets
import json
import subprocess

async def handle_connection(websocket, path):
    print(f"New client connected: {path}")
    async for message in websocket:
        print(f"Received message: {message}")
        try:
            schedule = json.loads(message)
            on_time = schedule['onTime']
            off_time = schedule['offTime']
            print(f"Publishing to MQTT: ON={on_time}, OFF={off_time}")
            result = subprocess.run(
                ['mosquitto_pub', '-t', 'light/schedule', '-m', f'{on_time},{off_time}'],
                capture_output=True, text=True
            )
            print(f"mosquitto_pub stdout: {result.stdout}")
            if result.stderr:
                print(f"mosquitto_pub stderr: {result.stderr}")
            await websocket.send('Schedule received and published to MQTT')
            print("Sent confirmation to client")
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            await websocket.send(f'Error: Invalid JSON format')
        except subprocess.CalledProcessError as e:
            print(f"MQTT publish error: {e}")
            await websocket.send(f'Error: Failed to publish to MQTT')
        except Exception as e:
            print(f"Error: {e}")
            await websocket.send(f'Error: {str(e)}')

print("Starting WebSocket server on ws://localhost:8765")
try:
    start_server = websockets.serve(handle_connection, 'localhost', 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
except Exception as e:
    print(f"Server failed to start: {e}")