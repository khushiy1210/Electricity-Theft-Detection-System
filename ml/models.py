from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
import datetime

class MeterReading(Base):
    __tablename__ = "meter_readings"

    id = Column(Integer, primary_key=True, index=True)
    cust_id = Column(String)
    transformer_id = Column(String)
    timestamp = Column(DateTime)
    kw_usage = Column(Float)
    voltage = Column(Float)
    current = Column(Float)
    pf = Column(Float)
    short_circuit = Column(Integer)
    meter_reset = Column(Integer)
    meter_reverse = Column(Integer)


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    cust_id = Column(String)
    transformer_id = Column(String)
    probability = Column(Float)
    alert_level = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class CustomerProfile(Base):
    __tablename__ = "customer_profiles"

    id = Column(Integer, primary_key=True)
    cust_id = Column(String, unique=True)

    risk_level = Column(String, default="NORMAL")
    total_alerts = Column(Integer, default=0)

    # 🔹 NEW FIELDS (Professional System)
    current_level = Column(String, default="LOW")   # Last alert level
    consecutive_high = Column(Integer, default=0)   # Track HIGH streak
    last_alert_time = Column(DateTime, nullable=True)  # Cooldown control