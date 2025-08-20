import requests
import json
import os

LLM_API_URL = os.getenv("LLM_API_URL", "http://localhost:11434/api/chat")
LLM_MODEL = os.getenv("LLM_MODEL", "llama2")

def generate_summary(incident, pred_sessions, pred_revenue):
    prompt = f"""
You are a business impact summarizer for SRE incidents. Generate a concise, neutral, third-person summary for stakeholders. Avoid personal pronouns. Use structured, report-style language.

Format:
"Incident {incident['incident_id']} was classified as {incident['severity']} severity, affecting the {incident['affected_services']} service between {incident['start_time']} and {incident['end_time']} on {incident['start_time'].split('T')[0]}. Approximately {incident['traffic']} users and {incident['user_sessions']} sessions were impacted. The root cause was {incident['root_cause']}, resolved in {incident['resolution_time']} minutes. Estimated impact includes {int(pred_sessions)} lost sessions and ${int(pred_revenue)} in potential revenue loss. This incident highlights the importance of resilient infrastructure and rapid recovery protocols."

Incident Details:
- Incident ID: {incident['incident_id']}
- Start Time: {incident['start_time']}
- End Time: {incident['end_time']}
- Affected Services: {incident['affected_services']}
- Traffic: {incident['traffic']}
- User Sessions: {incident['user_sessions']}
- Severity: {incident['severity']}
- Root Cause: {incident['root_cause']}
- Resolution Time: {incident['resolution_time']} minutes
- Predicted Sessions Affected: {int(pred_sessions)}
- Predicted Revenue Loss: ${int(pred_revenue)}
"""


    payload = {
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }

    try:
        response = requests.post(LLM_API_URL, json=payload)
        response.raise_for_status()

        try:
            response_json = response.json()
            summary = response_json.get("message", {}).get("content", "").strip()

            if not summary:
                raise ValueError("Empty summary from LLM")

        except (json.JSONDecodeError, ValueError) as e:
            print("⚠️ LLM response parsing error:", e)
            print("🔎 Raw response:", response.text)

            # Fallback summary
            summary = (
                f"Incident {incident['incident_id']} was classified as {incident['severity']} severity, "
                f"affecting the {incident['affected_services']} service between {incident['start_time']} and {incident['end_time']}. "
                f"Approximately {incident['traffic']} users and {incident['user_sessions']} sessions were impacted. "
                f"The root cause was {incident['root_cause']}, resolved in {incident['resolution_time']} minutes. "
                f"Estimated impact includes {int(pred_sessions)} lost sessions and ${int(pred_revenue)} in potential revenue loss."
            )

    except requests.RequestException as e:
        print("❌ LLM request error:", e)
        summary = "Summary generation failed due to LLM request error."

    return summary