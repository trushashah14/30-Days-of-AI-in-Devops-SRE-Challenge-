import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

# Jira credentials from .env
email = os.getenv("JIRA_EMAIL")
api_token = os.getenv("JIRA_API_TOKEN")
domain = os.getenv("JIRA_DOMAIN")  # e.g., trushashah1402.atlassian.net (no https:// and no trailing slash)
project_key = os.getenv("JIRA_PROJECT_KEY")

url = f"https://{domain}/rest/api/3/issue"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Sample tickets
tickets = [
    {
        "summary": "VPN access failing for remote users",
        "description": "Multiple users report inability to connect via VPN since 9 AM EST. Error: 'Connection timed out.'",
        "labels": ["network", "vpn", "incident"]
    },
    {
        "summary": "DNS resolution delay in production",
        "description": "DNS queries are taking 2–3 seconds longer than usual. Affects service discovery.",
        "labels": ["dns", "latency", "prod"]
    },
    {
        "summary": "High CPU usage on PostgreSQL cluster",
        "description": "CPU spikes observed on DB nodes during ETL jobs. Query optimization needed.",
        "labels": ["database", "postgres", "performance"]
    },
    {
        "summary": "Backup job failed for customer DB",
        "description": "Nightly backup failed with error: 'Permission denied.' Affects customer data integrity.",
        "labels": ["backup", "db", "critical"]
    },
    {
        "summary": "API returns 500 error on login",
        "description": "Login API intermittently fails with 500 status. Logs show null pointer exception.",
        "labels": ["api", "bug", "login"]
    },
    {
        "summary": "UI not loading on Safari browser",
        "description": "Users report blank screen on Safari. Works fine on Chrome and Firefox.",
        "labels": ["frontend", "ui", "browser"]
    },
    {
        "summary": "Payment gateway integration broken",
        "description": "Payment requests are not reaching the gateway. Timeout after 30s.",
        "labels": ["payment", "integration", "timeout"]
    }
]

# Jira Cloud REST API v3 requires the "description" field to be in Atlassian Document Format (ADF).
def adf_description(text):
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [
                    {"type": "text", "text": text}
                ]
            }
        ]
    }

# Create tickets
for ticket in tickets:
    payload = {
        "fields": {
            "project": {
                "key": project_key
            },
            "summary": ticket["summary"],
            "description": adf_description(ticket["description"]),
            "issuetype": {
                "name": "Task"
            },
            "labels": ticket["labels"]
        }
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            auth=HTTPBasicAuth(email, api_token),
            json=payload,
            timeout=15  # seconds
        )
        if response.status_code == 201:
            print(f"✅ Created: {ticket['summary']}")
        else:
            print(f"❌ Failed: {ticket['summary']} — {response.status_code} {response.text}")
    except requests.exceptions.ConnectTimeout:
        print(f"❌ Timeout: Could not connect to Jira for ticket '{ticket['summary']}'")
    except Exception as e:
        print(f"❌ Error: {ticket['summary']} — {e}")