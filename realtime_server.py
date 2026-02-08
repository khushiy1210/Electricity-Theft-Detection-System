from fastapi import FastAPI, WebSocket
from kafka import KafkaConsumer
import json

app = FastAPI()

active_connections = []

@app.websocket("/ws/alerts")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)

    try:
        while True:
            await websocket.receive_text()
    except:
        active_connections.remove(websocket)
