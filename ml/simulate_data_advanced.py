# import numpy as np
# import pandas as pd
# import random
# from datetime import datetime, timedelta
#
# np.random.seed(42)
# random.seed(42)
#
# def simulate(customers=50, readings=100):
#     rows = []
#     labels = {}
#
#     start = datetime.now()
#
#     for cid in range(customers):
#         cust_id = f"CUST{cid:04d}"
#         is_thief = random.random() < 0.25
#         labels[cust_id] = is_thief
#
#         base = random.uniform(0.8, 2.0)
#
#         for i in range(readings):
#             ts = start + timedelta(minutes=15 * i)
#
#             usage = base + np.random.normal(0, 0.2)
#             if is_thief and i > readings // 2:
#                 usage *= random.uniform(0.3, 0.6)
#
#             rows.append([
#                 cust_id,
#                 "T1",
#                 ts,
#                 max(usage, 0.1),
#                 random.normalvariate(220, 8),
#                 random.normalvariate(2.0, 0.3),
#                 random.uniform(0.75, 0.95),
#                 int(random.random() < 0.01),
#                 int(random.random() < 0.005),
#                 int(random.random() < 0.01)
#             ])
#
#     df = pd.DataFrame(rows, columns=[
#         "cust_id", "transformer_id", "timestamp",
#         "kw_usage", "voltage", "current", "pf",
#         "short_circuit", "meter_reset", "meter_reverse"
#     ])
#
#     df.to_csv("advanced_usage.csv", index=False)
#
#     pd.DataFrame([
#         {"cust_id": k, "is_theft": v} for k, v in labels.items()
#     ]).to_csv("labels.csv", index=False)
#
#     print("✔ Data generated")
#
# simulate()


from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()

model, feature_cols = joblib.load("model_advanced.pkl")

history = pd.read_csv("advanced_usage.csv")

def get_alert(prob):
    if prob > 0.85: return "CRITICAL"
    if prob > 0.7: return "HIGH"
    if prob > 0.5: return "MEDIUM"
    return "LOW"

@app.post("/predict")
def predict(data: dict):
    global history

    history = pd.concat([history, pd.DataFrame([data])], ignore_index=True)

    cust_hist = history[history.cust_id == data["cust_id"]]

    agg = cust_hist.agg({
        "kw_usage":["mean","max","min","std"],
        "voltage":["mean","std"],
        "current":["mean","max"],
        "pf":"mean",
        "short_circuit":"sum",
        "meter_reset":"sum",
        "meter_reverse":"sum"
    })

    agg.columns = ["_".join(c) for c in agg.columns]
    X = agg[feature_cols]

    prob = model.predict_proba(X)[0][1]

    return {"theft_probability": float(prob), "alert": get_alert(prob)}

