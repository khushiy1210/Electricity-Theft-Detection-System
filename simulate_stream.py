# import pandas as pd
# import requests
# import time
#
# df = pd.read_csv("advanced_usage.csv")
#
# for _, row in df.iterrows():
#     payload = {
#         "cust_id": row.cust_id,
#         "transformer_id": row.transformer_id,
#         "timestamp": str(row.timestamp),
#         "kw_usage": float(row.kw_usage),
#         "voltage": float(row.voltage),
#         "current": float(row.current),
#         "pf": float(row.pf),
#         "short_circuit": int(row.short_circuit),
#         "meter_reset": int(row.meter_reset),
#         "meter_reverse": int(row.meter_reverse),
#         "transformer_total": 60.0
#     }
#
#     r = requests.post("http://localhost:8000/predict", json=payload)
#     print(r.json())
#     time.sleep(0.3)

import pandas as pd
import requests
import time

df = pd.read_csv("advanced_usage.csv")

for _, row in df.iterrows():
    payload = row.to_dict()
    payload["timestamp"] = str(payload["timestamp"])

    r = requests.post("http://127.0.0.1:8000/predict", json=payload)
    print(r.json())
    time.sleep(0.2)

