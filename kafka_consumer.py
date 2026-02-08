# from kafka import KafkaConsumer
# import json
# import psycopg2
# import uuid
# from datetime import datetime
#
# # 1️⃣ Connect to PostgreSQL
# conn = psycopg2.connect(
#     host="localhost",
#     database="theft_db",
#     user="postgres",
#     password="password"
# )
# cursor = conn.cursor()
#
# # 2️⃣ Kafka Consumer
# consumer = KafkaConsumer(
#     "theft_alerts",
#     bootstrap_servers="localhost:9092",
#     value_deserializer=lambda v: json.loads(v.decode("utf-8")),
#     auto_offset_reset="earliest",
#     enable_auto_commit=True
# )
#
# print("Kafka consumer started...")
#
# # 3️⃣ Consume messages
# for msg in consumer:
#     alert = msg.value
#
#     print("Received:", alert)
#
#     cursor.execute(
#         """
#         INSERT INTO alerts (id, cust_id, confidence, alert_level, latitude, longitude, detected_at)
#         VALUES (%s, %s, %s, %s, %s, %s, %s)
#         """,
#         (
#             str(uuid.uuid4()),
#             alert["cust_id"],
#             alert["confidence"],
#             alert["alert_level"],
#             alert.get("lat", 18.5204),   # default Pune coords
#             alert.get("lng", 73.8567),
#             datetime.now()
#         )
#     )
#
#     conn.commit()
# from fastapi import FastAPI, WebSocket
# from kafka import KafkaConsumer
# import json
#
# app = FastAPI()
#
# active_connections = []
#
# @app.websocket("/ws/alerts")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     active_connections.append(websocket)
#
#     try:
#         while True:
#             await websocket.receive_text()
#     except:
#         active_connections.remove(websocket)
