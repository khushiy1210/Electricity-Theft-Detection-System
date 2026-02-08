# from fastapi import FastAPI
# from pydantic import BaseModel
# import pandas as pd
# import joblib
# import os
#
# app = FastAPI()
#
# model, feature_cols = joblib.load("model_advanced.pkl")
# os.makedirs("history", exist_ok=True)
#
# class Input(BaseModel):
#     cust_id: str
#     transformer_id: str
#     timestamp: str
#     kw_usage: float
#     voltage: float
#     current: float
#     pf: float
#     short_circuit: int
#     meter_reset: int
#     meter_reverse: int
#     transformer_total: float
#
# def update_history(data):
#     path = f"history/{data['cust_id']}.csv"
#     df_new = pd.DataFrame([data])
#
#     if os.path.exists(path):
#         df_old = pd.read_csv(path)
#         df = pd.concat([df_old, df_new]).tail(50)
#     else:
#         df = df_new
#
#     df.to_csv(path, index=False)
#     return df
#
# def engineer_features(df):
#     return {
#         "kw_usage_mean": float(df.kw_usage.mean()),
#         "kw_usage_max": float(df.kw_usage.max()),
#         "kw_usage_min": float(df.kw_usage.min()),
#         "kw_usage_std": float(df.kw_usage.std() or 0),
#
#         "voltage_mean": float(df.voltage.mean()),
#         "voltage_std": float(df.voltage.std() or 0),
#
#         "current_mean": float(df.current.mean()),
#         "current_max": float(df.current.max()),
#
#         "pf_mean": float(df.pf.mean()),
#
#         "short_circuit_sum": int(df.short_circuit.sum()),
#         "meter_reset_sum": int(df.meter_reset.sum()),
#         "meter_reverse_sum": int(df.meter_reverse.sum()),
#
#         "imbalance": float(df.transformer_total.iloc[-1] - df.kw_usage.sum())
#     }
#
# print("Prediction probability:", prob)
#
# @app.post("/predict")
# def predict(data: Input):
#     df_hist = update_history(data.dict())
#     feats = engineer_features(df_hist)
#
#     X = pd.DataFrame([feats])[feature_cols]
#
#     pred = model.predict(X)[0]
#     prob = model.predict_proba(X)[0][1]
#
#     # 🔥 Convert NumPy → Python
#     safe_features = {k: float(v) for k, v in feats.items()}
#
#     return {
#         "cust_id": data.cust_id,
#         "is_theft": bool(int(pred)),
#         "confidence": float(prob),
#         "features": safe_features
#     }
