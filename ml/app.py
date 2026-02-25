from fastapi import FastAPI
from database import SessionLocal
from models import MeterReading, Alert, CustomerProfile
from datetime import datetime, timedelta
import pandas as pd
import joblib

app = FastAPI(title="Smart Grid Intelligence API")

model, feature_cols = joblib.load("model_advanced.pkl")

COOLDOWN_MINUTES = 15


def get_level(prob):
    if prob >= 0.80:
        return "CRITICAL"
    elif prob >= 0.50:
        return "HIGH"
    elif prob >= 0.30:
        return "MEDIUM"
    return "LOW"


@app.get("/health")
def health():
    return {"status": "Smart Grid Running"}


@app.post("/predict")
async def predict(data: dict):

    db = SessionLocal()

    try:
        timestamp = datetime.fromisoformat(
            data["timestamp"].replace("Z", "+00:00")
        )

        # ===============================
        # Save Meter Reading
        # ===============================
        reading = MeterReading(
            cust_id=data["cust_id"],
            transformer_id=data.get("transformer_id", "T1"),
            timestamp=timestamp,
            kw_usage=data["kw_usage"],
            voltage=data["voltage"],
            current=data["current"],
            pf=data["pf"],
            short_circuit=data["short_circuit"],
            meter_reset=data["meter_reset"],
            meter_reverse=data["meter_reverse"]
        )

        db.add(reading)
        db.commit()

        # ===============================
        # Get last 50 readings
        # ===============================
        readings = db.query(MeterReading)\
            .filter(MeterReading.cust_id == data["cust_id"])\
            .order_by(MeterReading.timestamp.desc())\
            .limit(50).all()

        df = pd.DataFrame([{
            "kw_usage": r.kw_usage,
            "voltage": r.voltage,
            "current": r.current,
            "pf": r.pf,
            "short_circuit": r.short_circuit,
            "meter_reset": r.meter_reset,
            "meter_reverse": r.meter_reverse
        } for r in readings])

        if df.empty:
            return {"error": "Not enough data"}

        agg = df.groupby(lambda x: 0).agg({
            "kw_usage": ["mean", "max", "min", "std"],
            "voltage": ["mean", "std"],
            "current": ["mean", "max"],
            "pf": "mean",
            "short_circuit": "sum",
            "meter_reset": "sum",
            "meter_reverse": "sum"
        })

        agg.columns = ["_".join(col) for col in agg.columns]
        agg = agg.fillna(0)

        for col in feature_cols:
            if col not in agg.columns:
                agg[col] = 0

        X = agg[feature_cols]
        prob = model.predict_proba(X)[0][1]

        # ===============================
        # NEIGHBOR ANALYSIS
        # ===============================
        neighbors = db.query(MeterReading)\
            .filter(MeterReading.transformer_id == reading.transformer_id)\
            .order_by(MeterReading.timestamp.desc())\
            .limit(50).all()

        if neighbors:
            neighbor_avg = sum(r.kw_usage for r in neighbors) / len(neighbors)
            if reading.kw_usage < 0.4 * neighbor_avg:
                prob += 0.15

        # ===============================
        # TRANSFORMER LOAD MISMATCH
        # ===============================
        transformer_readings = db.query(MeterReading)\
            .filter(MeterReading.transformer_id == reading.transformer_id)\
            .order_by(MeterReading.timestamp.desc())\
            .limit(100).all()

        transformer_total = sum(r.kw_usage for r in transformer_readings)

        if transformer_total > 0:
            expected_avg = transformer_total / len(transformer_readings)
            if reading.kw_usage < 0.3 * expected_avg:
                prob += 0.10

        prob = min(prob, 1.0)
        level = get_level(prob)

        # ===============================
        # ALERT COOLDOWN
        # ===============================
        last_alert = db.query(Alert)\
            .filter(Alert.cust_id == data["cust_id"])\
            .order_by(Alert.created_at.desc())\
            .first()

        create_alert = True

        if last_alert:
            if datetime.utcnow() - last_alert.created_at < timedelta(minutes=COOLDOWN_MINUTES):
                create_alert = False

        # ===============================
        # SAVE ALERT + UPDATE PROFILE
        # ===============================
        if level in ["HIGH", "CRITICAL"] and create_alert:

            alert = Alert(
                cust_id=data["cust_id"],
                transformer_id=reading.transformer_id,
                probability=prob,
                alert_level=level,
                created_at=datetime.utcnow()
            )

            db.add(alert)

            profile = db.query(CustomerProfile)\
                .filter(CustomerProfile.cust_id == data["cust_id"])\
                .first()

            if not profile:
                profile = CustomerProfile(cust_id=data["cust_id"])
                db.add(profile)

            profile.total_alerts += 1
            profile.current_level = level
            profile.last_alert_time = datetime.utcnow()

            if level == "CRITICAL":
                profile.risk_level = "DANGEROUS"

            db.commit()

        return {
            "customer": data["cust_id"],
            "probability": float(prob),
            "level": level,
            "timestamp": str(datetime.utcnow())
        }

    finally:
        db.close()