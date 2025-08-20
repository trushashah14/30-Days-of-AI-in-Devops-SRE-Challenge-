import os
import pandas as pd
import requests
from dotenv import load_dotenv
import re

load_dotenv()

LLM_API_URL = os.getenv("LLM_API_URL", "http://localhost:11434/api/chat")
LLM_MODEL = os.getenv("LLM_MODEL", "llama2")

def extract_numbers_from_llm_output(output):
    # Extract two numbers (revenue_loss, sessions_affected) from LLM output
    matches = re.findall(r'(\d{3,})', output)
    if len(matches) >= 2:
        return f"{matches[0]},{matches[1]}"
    return "PARSE_ERROR,PARSE_ERROR"

def estimate_impact_llm(incident, historical_data):
    prompt = (
        "Estimate the business impact for this incident. "
        "Return ONLY two numbers separated by a comma: revenue_loss,sessions_affected.\n"
        f"Start: {incident['start_time']}\n"
        f"End: {incident['end_time']}\n"
        f"Affected services: {incident['affected_services']}\n"
        f"Traffic: {incident['traffic']}\n"
        f"User sessions: {incident.get('user_sessions', 'N/A')}\n"
        f"Severity: {incident.get('severity', 'N/A')}\n"
        f"Root cause: {incident.get('root_cause', 'N/A')}\n"
        f"Resolution time: {incident.get('resolution_time', 'N/A')}\n"
        "Historical impact data:\n"
        f"{historical_data}\n"
        "Output format: revenue_loss,sessions_affected"
    )
    payload = {
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        resp = requests.post(LLM_API_URL, json=payload)
        resp.raise_for_status()
        # Ollama returns a single JSON object, not streaming lines
        try:
            result = resp.json()
            answer = ""
            if "message" in result and "content" in result["message"]:
                answer = result["message"]["content"].strip()
            else:
                answer = resp.text.strip()
        except Exception:
            # If JSON decode fails, fallback to raw text
            answer = resp.text.strip()
    except Exception as e:
        print(f"❌ LLM API error: {e} (URL: {LLM_API_URL})")
        return "LLM_API_ERROR,LLM_API_ERROR"
    if not answer:
        print("⚠️ No response from LLM. Try a simpler prompt or check Ollama logs.")
        return "NO_LLM_RESPONSE,NO_LLM_RESPONSE"
    parsed = extract_numbers_from_llm_output(answer)
    print(f"LLM raw output: {answer}")
    print(f"LLM parsed output: {parsed}")
    return parsed

def train_llm_on_historical_data(historical_data):
    print("Training phase: Preparing historical incident data for LLM context.")
    return historical_data

def predict_impact_for_incidents(df, historical_data):
    estimates = []
    for _, row in df.iterrows():
        print(f"Predicting impact for incident {row['incident_id']}...")
        estimate = estimate_impact_llm(row, historical_data)
        print(f"LLM Estimate: {estimate}")
        estimates.append(estimate)
    df["llm_estimate"] = estimates
    df.to_csv("incident_estimates.csv", index=False)
    print("Estimates saved to incident_estimates.csv")

def main():
    # Use incidents.csv ONLY for historical training/context
    historical_df = pd.read_csv("incidents.csv")
    historical_data = historical_df[["affected_services", "traffic", "user_sessions", "severity", "root_cause", "resolution_time", "actual_revenue_loss", "actual_sessions_affected"]].to_string(index=False)
    train_llm_on_historical_data(historical_data)

    # Use synthetic_incidents.csv ONLY for prediction
    if os.path.exists("synthetic_incidents.csv"):
        df = pd.read_csv("synthetic_incidents.csv")
        predict_impact_for_incidents(df, historical_data)
    else:
        print("No synthetic_incidents.csv found. Please provide synthetic incidents for prediction.")

if __name__ == "__main__":
    main()