# import pandas as pd
# import joblib
# from sklearn.ensemble import RandomForestClassifier
#
# df = pd.read_csv("advanced_usage.csv")
# labels = pd.read_csv("labels.csv")
#
# df["timestamp"] = pd.to_datetime(df["timestamp"])
#
# # aggregate per customer
# agg = df.groupby("cust_id").agg({
#     "kw_usage": ["mean", "max", "min", "std"],
#     "voltage": ["mean", "std"],
#     "current": ["mean", "max"],
#     "pf": "mean",
#     "short_circuit": "sum",
#     "meter_reset": "sum",
#     "meter_reverse": "sum"
# })
#
# agg.columns = ["_".join(c) for c in agg.columns]
# agg = agg.reset_index()
#
# data = agg.merge(labels, on="cust_id")
#
# feature_cols = [c for c in data.columns if c not in ["cust_id", "is_theft"]]
#
# X = data[feature_cols]
# y = data["is_theft"]
#
# model = RandomForestClassifier(n_estimators=200, random_state=42)
# model.fit(X, y)
#
# joblib.dump((model, feature_cols), "model_advanced.pkl")
#
# print("✔ Model trained")
# print("Features:", feature_cols)


import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("advanced_usage.csv")
labels = pd.read_csv("labels.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])

agg = df.groupby("cust_id").agg({
    "kw_usage": ["mean","max","min","std"],
    "voltage": ["mean","std"],
    "current": ["mean","max"],
    "pf": "mean",
    "short_circuit": "sum",
    "meter_reset": "sum",
    "meter_reverse": "sum"
})

agg.columns = ["_".join(c) for c in agg.columns]
agg = agg.reset_index()

data = agg.merge(labels, on="cust_id")

print(data["is_theft"].value_counts())  # SHOULD show both True & False

feature_cols = [c for c in data.columns if c not in ["cust_id","is_theft"]]

X = data[feature_cols]
y = data["is_theft"]

model = RandomForestClassifier(n_estimators=300, random_state=42)
model.fit(X, y)

joblib.dump((model, feature_cols), "model_advanced.pkl")

print("✔ Model trained")
