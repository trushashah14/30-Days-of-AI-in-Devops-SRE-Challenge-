import os
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import logging
from dotenv import load_dotenv

load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Team mapping for Jira components
TEAM_COMPONENTS = {
    "network": "Network",
    "db": "Database",
    "app": "Application"
}

CATEGORY_KEYWORDS = {
    "network": ["vpn", "connectivity", "dns", "firewall", "router", "switch", "ping", "packet", "site unreachable"],
    "db": ["db", "database", "query", "sql", "connection", "timeout", "slow", "deadlock", "table"],
    "app": ["api", "application", "login", "error", "ui", "bug", "auth", "page", "service", "500", "exception"]
}

def categorize(text):
    logging.debug(f"Categorizing text: {text}")
    text = text.lower()
    for cat, keywords in CATEGORY_KEYWORDS.items():
        if any(word in text for word in keywords):
            logging.debug(f"Matched category '{cat}' for text: {text}")
            return cat
    logging.debug(f"No keyword match, defaulting to 'app' for text: {text}")
    return "app"  # Default to app if no match

def fetch_unassigned_jira_tickets(jira_url, jira_user, jira_token, jql="assignee is EMPTY AND status = 'To Do' AND component is EMPTY", max_results=20):
    logging.info("Fetching unassigned Jira tickets...")
    headers = {"Accept": "application/json"}
    params = {
        "jql": jql,
        "maxResults": max_results,
        "fields": "summary,description"
    }
    response = requests.get(
        f"{jira_url}/rest/api/2/search",
        headers=headers,
        params=params,
        auth=HTTPBasicAuth(jira_user, jira_token)
    )
    response.raise_for_status()
    issues = response.json()["issues"]
    tickets = []
    for issue in issues:
        summary = issue["fields"].get("summary", "")
        description = issue["fields"].get("description", "")
        tickets.append({
            "id": issue["key"],
            "summary": summary,
            "description": description
        })
    logging.info(f"Total unassigned tickets fetched: {len(tickets)}")
    return pd.DataFrame(tickets)

def assign_jira_component(jira_url, jira_user, jira_token, issue_key, component_name):
    logging.info(f"Tagging issue {issue_key} with component '{component_name}'...")
    # Extract project key from issue key (e.g., "MTT-14" -> "MTT")
    project_key = issue_key.split('-')[0]
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    # Get component ID from Jira (required for update)
    comp_resp = requests.get(
        f"{jira_url}/rest/api/2/project/{project_key}/components",
        headers={"Accept": "application/json"},
        auth=HTTPBasicAuth(jira_user, jira_token)
    )
    comp_resp.raise_for_status()
    components = comp_resp.json()
    comp_id = None
    for comp in components:
        if comp["name"].lower() == component_name.lower():
            comp_id = comp["id"]
            break
    if not comp_id:
        logging.error(f"Component '{component_name}' not found in project {project_key}.")
        return

    payload = {
        "update": {
            "components": [
                {"set": [{"id": comp_id}]}
            ]
        }
    }
    response = requests.put(
        f"{jira_url}/rest/api/2/issue/{issue_key}",
        headers=headers,
        json=payload,
        auth=HTTPBasicAuth(jira_user, jira_token)
    )
    if response.status_code == 204:
        logging.info(f"Issue {issue_key} successfully tagged with component '{component_name}'.")
    else:
        logging.error(f"Failed to tag issue {issue_key}: {response.status_code} {response.text}")

def train_classifier(history_csv="ticket_history.csv"):
    logging.info(f"Training ML classifier using {history_csv}...")
    df = pd.read_csv(history_csv)
    X = df["summary"] + " " + df["description"].fillna("")
    y = df["category"]
    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)
    clf = MultinomialNB()
    clf.fit(X_vec, y)
    logging.info("ML classifier trained successfully.")
    return vectorizer, clf

def ml_categorize(text, vectorizer, clf):
    logging.debug(f"ML categorizing text: {text}")
    X_vec = vectorizer.transform([text])
    prediction = clf.predict(X_vec)[0]
    logging.info(f"Predicted category: {prediction} for text: {text}")
    return prediction

def main():
    logging.info("Starting ticket triage workflow...")
    # Jira credentials from .env
    jira_url = os.getenv("JIRA_URL")  # e.g., https://trushashah1402.atlassian.net/
    jira_user = os.getenv("JIRA_EMAIL")
    jira_token = os.getenv("JIRA_API_TOKEN")

    # Train ML classifier from historical data
    vectorizer, clf = train_classifier("ticket_history.csv")

    # Fetch new, unassigned tickets
    df = fetch_unassigned_jira_tickets(jira_url, jira_user, jira_token)
    logging.info("Fetched unassigned Jira tickets:")
    logging.info(df[["id", "summary"]].to_string(index=False))

    # Only process issues from project 'MTT'
    df_mtt = df[df["id"].str.startswith("MTT-")]
    logging.info(f"Processing only issues from project 'MTT'. Count: {len(df_mtt)}")

    # Categorize and tag each ticket with the correct component using ML
    for _, row in df_mtt.iterrows():
        logging.info(f"Processing ticket {row['id']}: {row['summary']}")
        category = ml_categorize(row["summary"] + " " + str(row["description"]), vectorizer, clf)
        component = TEAM_COMPONENTS[category]
        assign_jira_component(jira_url, jira_user, jira_token, row["id"], component)

    logging.info("All 'MTT' tickets have been tagged with the correct team component (ML-based).")

if __name__ == "__main__":
    main()

