import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OrdinalEncoder

# Load and preprocess training data
df = pd.read_csv("incidents.csv")

# Encode severity
severity_encoder = OrdinalEncoder(categories=[["minor", "major", "critical"]])
df["severity_encoded"] = severity_encoder.fit_transform(df[["severity"]])

# Select features and targets
features = ["traffic", "user_sessions", "resolution_time", "severity_encoded"]
X = df[features]
y_sessions = df["actual_sessions_affected"]
y_revenue = df["actual_revenue_loss"]

# Train models
model_sessions = RandomForestRegressor().fit(X, y_sessions)
model_revenue = RandomForestRegressor().fit(X, y_revenue)

# Save models and encoder
joblib.dump(model_sessions, "model_sessions.pkl")
joblib.dump(model_revenue, "model_revenue.pkl")
joblib.dump(severity_encoder, "severity_encoder.pkl")

print("✅ ML models and encoder saved.")