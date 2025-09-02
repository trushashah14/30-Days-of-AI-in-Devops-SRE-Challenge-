import os
import openai  # Or use ollama or Azure OpenAI
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.rtm_v2 import RTMClient
import subprocess

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID", "general")

openai.api_key = OPENAI_API_KEY
slack_client = WebClient(token=SLACK_BOT_TOKEN)

def run_remediation(action):
    # Example: restart pods (replace with actual command/script)
    if action == "restart pods":
        try:
            result = subprocess.run(
                ["echo", "kubectl rollout restart deployment/my-app"],
                capture_output=True, text=True
            )
            return result.stdout.strip()
        except Exception as e:
            return f"Error running remediation: {e}"
    return "Unknown remediation action."

def llm_confirmation_log(action, remediation_output):
    prompt = (
        f"You are a DevOps assistant. Summarize the following remediation action in a human-friendly log for Slack:\n"
        f"Action: {action}\n"
        f"Output: {remediation_output}\n"
        f"Include what was done, why, and confirmation that it succeeded or failed."
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response.choices[0].message.content.strip()

@RTMClient.run_on(event="message")
def handle_message(**payload):
    data = payload["data"]
    web_client = payload["web_client"]
    text = data.get("text", "")
    channel_id = data.get("channel", "")
    if text.startswith("/remediate"):
        action = text.replace("/remediate", "").strip()
        remediation_output = run_remediation(action)
        confirmation = llm_confirmation_log(action, remediation_output)
        try:
            web_client.chat_postMessage(channel=channel_id, text=confirmation)
        except SlackApiError as e:
            print(f"Slack error: {e.response['error']}")

if __name__ == "__main__":
    rtm_client = RTMClient(token=SLACK_BOT_TOKEN)
    print("ChatOps bot running...")
    rtm_client.start()
