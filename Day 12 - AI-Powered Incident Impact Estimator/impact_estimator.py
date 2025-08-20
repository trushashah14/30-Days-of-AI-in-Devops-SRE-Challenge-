import pandas as pd
import joblib
from generate_summary import generate_summary

# Load models and encoder
model_sessions = joblib.load("model_sessions.pkl")
model_revenue = joblib.load("model_revenue.pkl")
severity_encoder = joblib.load("severity_encoder.pkl")

# Load input data
df = pd.read_csv("synthetic_incidents.csv")

# Prepare output columns
pred_sessions_list = []
pred_revenue_list = []
summary_list = []

for _, incident in df.iterrows():
    print(f"\n🔍 Predicting for {incident['incident_id']}...")

    # Encode severity
    severity_encoded = severity_encoder.transform([[incident["severity"]]])[0][0]

    # Prepare features
    features = pd.DataFrame([{
        "traffic": incident["traffic"],
        "user_sessions": incident["user_sessions"],
        "resolution_time": incident["resolution_time"],
        "severity_encoded": severity_encoded
    }])

    # Predict
    pred_sessions = model_sessions.predict(features)[0]
    pred_revenue = model_revenue.predict(features)[0]

    # Generate summary
    summary = generate_summary(incident, pred_sessions, pred_revenue)

    # Store results
    pred_sessions_list.append(int(pred_sessions))
    pred_revenue_list.append(int(pred_revenue))
    summary_list.append(summary)

# Save results
df["predicted_sessions_affected"] = pred_sessions_list
df["predicted_revenue_loss"] = pred_revenue_list
df["business_impact_summary"] = summary_list
df.to_csv("incident_estimates.csv", index=False)

print("\n✅ Predictions and summaries saved to incident_estimates.csv")