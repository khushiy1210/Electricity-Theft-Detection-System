# import pandas as pd
#
# def create_features(df):
#     df["power_calc"] = df["voltage"] * df["current"] * df["pf"] / 1000
#
#     df["current_to_usage_ratio"] = df["current"] / (df["kw_usage"] + 0.1)
#     df["voltage_deviation"] = abs(df["voltage"] - 230)
#     df["pf_drop"] = 1 - df["pf"]
#
#     df["tamper_score"] = (
#         df["meter_reverse"] +
#         df["meter_reset"] +
#         df["short_circuit"]
#     )
#
#     return df[[
#         "kw_usage",
#         "voltage",
#         "current",
#         "pf",
#         "current_to_usage_ratio",
#         "voltage_deviation",
#         "pf_drop",
#         "tamper_score"
#     ]]




from fastapi import FastAPI
import pandas as pd
import joblib
from features import create_features

app = FastAPI()

# Load trained model
model = joblib.load("model_advanced.pkl")

def get_alert_level(prob):
    if prob > 0.85:
        return "CRITICAL"
    elif prob > 0.70:
        return "HIGH"
    elif prob > 0.50:
        return "MEDIUM"
    else:
        return "LOW"

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    features = create_features(df)

    prob = model.predict_proba(features)[0][1]
    alert = get_alert_level(prob)

    return {
        "theft_probability": round(float(prob), 3),
        "alert_level": alert
    }
