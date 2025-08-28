import os
import sys
import requests
import pandas as pd
import json
from dotenv import load_dotenv
import logging

try:
    import matplotlib.pyplot as plt
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    import matplotlib.pyplot as plt

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

load_dotenv()
GRAFANA_API_KEY = os.getenv("GRAFANA_API_KEY")
GRAFANA_URL = os.getenv("GRAFANA_URL", "http://localhost:3000")
GRAFANA_DS_UID = os.getenv("GRAFANA_DS_UID")   # ✅ correct datasource UID
GRAFANA_DASHBOARD_UID = os.getenv("GRAFANA_DASHBOARD_UID")  # ✅ must be short UID from /d/<uid>/

GRAFANA_DASHBOARD_ENDPOINT = f"{GRAFANA_URL}/api/dashboards/db"
HEADERS = {
    "Authorization": f"Bearer {GRAFANA_API_KEY}",
    "Content-Type": "application/json"
}


def generate_promql(natural_query):
    logging.info(f"Generating PromQL for query: {natural_query}")
    prompt = f"""
You are a PromQL expert. Convert the following natural-language query into a valid PromQL expression.
Only output the PromQL code, nothing else.
Examples:
Query: "Show me CPU usage over the last hour"
PromQL: 100 - avg by(instance) (rate(node_cpu_seconds_total{{mode="idle"}}[1h])) * 100
Query: "Show me memory usage for the last day"
PromQL: node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100
Query: "Show me disk usage"
PromQL: node_filesystem_avail_bytes / node_filesystem_size_bytes * 100
---
Query: "{natural_query}"
PromQL:
"""
    ollama_url = "http://localhost:11434/api/generate"
    payload = {"model": "llama3", "prompt": prompt, "options": {"num_predict": 100}}
    llm_output = ""
    try:
        logging.info("Sending prompt to Ollama Llama 3 model...")
        with requests.post(ollama_url, json=payload, stream=True, timeout=120) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if line:
                    try:
                        part = json.loads(line.decode())
                        llm_output += part.get("response", "")
                    except Exception as e:
                        logging.warning(f"Error decoding LLM response line: {e}")
    except Exception as e:
        logging.error(f"Ollama error: {e}")
        return ""

    promql = ""
    for line in llm_output.strip().split("\n"):
        line = line.strip()
        if line and not line.lower().startswith(("the answer is", "after reading", "i'd say")):
            promql = line
            break

    if promql and 'mode!="idle"' in promql:
        logging.warning("LLM used mode!=idle. Fixing to idle and inverting.")
        promql = "100 - avg by(instance) (rate(node_cpu_seconds_total{mode=\"idle\"}[1h])) * 100"

    logging.info(f"Generated PromQL: {promql}")
    return promql


def create_grafana_panel(promql, panel_title="LLM Generated Panel"):
    logging.info("Creating Grafana panel with PromQL...")
    if not GRAFANA_DASHBOARD_UID:
        logging.error("GRAFANA_DASHBOARD_UID not set in .env. Please set it to your dashboard UID.")
        return False

    dashboard_url = f"{GRAFANA_URL}/api/dashboards/uid/{GRAFANA_DASHBOARD_UID}"
    try:
        r = requests.get(dashboard_url, headers=HEADERS)
        r.raise_for_status()
        dashboard = r.json()["dashboard"]
    except Exception as e:
        logging.error(f"Error fetching dashboard: {e}")
        return False

    new_panel = {
        "datasource": {"type": "prometheus", "uid": GRAFANA_DS_UID},  # ✅ fixed
        "type": "timeseries",
        "title": panel_title,
        "targets": [{"refId": "A", "expr": promql, "interval": "", "format": "time_series", "instant": False}],
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": len(dashboard.get("panels", [])) * 8}
    }

    if "panels" not in dashboard:
        dashboard["panels"] = []
    dashboard["panels"].append(new_panel)

    payload = {"dashboard": dashboard, "overwrite": True}
    try:
        r = requests.post(GRAFANA_DASHBOARD_ENDPOINT, headers=HEADERS, data=json.dumps(payload))
        r.raise_for_status()
        logging.info("Panel added successfully.")
        return True
    except Exception as e:
        logging.error(f"Error updating dashboard: {e}")
        return False


def query_grafana(promql):
    logging.info(f"Querying Grafana with PromQL: {promql}")
    url = f"{GRAFANA_URL}/api/ds/query"
    payload = {
        "queries": [
            {
                "refId": "A",
                "expr": promql,
                "datasource": {"type": "prometheus", "uid": GRAFANA_DS_UID},  # ✅ fixed
                "intervalMs": 15000,
                "maxDataPoints": 43200
            }
        ],
        "from": "now-1h",
        "to": "now"
    }
    try:
        response = requests.post(url, headers=HEADERS, json=payload)
        response.raise_for_status()
        logging.info("Grafana query successful.")
        return response.json()
    except Exception as e:
        logging.error(f"Error querying Grafana: {e}")
        return {}


def display_results(data):
    logging.info("Displaying results...")
    frames = []
    if isinstance(data, dict):
        frames = data.get('results', {}).get('A', {}).get('frames', [])
    elif isinstance(data, list):
        frames = data

    if not frames:
        logging.warning("No frames found in Grafana response.")
        print("No data returned.")
        return

    for frame in frames:
        values = frame.get("data", {}).get("values", [])
        if not values or len(values) < 2:
            logging.warning("Frame has no values.")
            continue

        import datetime
        timestamps = [datetime.datetime.fromtimestamp(ts / 1000.0) for ts in values[0]]
        df = pd.DataFrame({"Time": timestamps, "Value": values[1]})
        print(df)

        try:
            plt.figure(figsize=(10, 5))
            plt.plot(df["Time"], df["Value"], marker="o", color="blue")
            plt.title("Grafana Query Results")
            plt.xlabel("Time")
            plt.ylabel("Value")
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            logging.warning(f"Could not plot results: {e}")


def main():
    logging.info("Starting Automated Natural Language to PromQL to Grafana Workflow")
    print("Type your natural language query below (or 'exit' to quit):")
    while True:
        query = input("Query: ")
        if query.strip().lower() == "exit":
            logging.info("Exiting workflow.")
            break
        promql = generate_promql(query)
        if not promql:
            print("Could not generate a valid PromQL query. Please try again.")
            continue
        print(f"Natural Query: {query}")
        print(f"Generated PromQL: {promql}")
        if create_grafana_panel(promql, panel_title=f"LLM: {query}"):
            print("Panel created in Grafana dashboard.")
        else:
            print("Failed to create panel in Grafana dashboard.")
        grafana_data = query_grafana(promql)
        print("Grafana raw response:", grafana_data)
        display_results(grafana_data)


if __name__ == "__main__":
    main()
