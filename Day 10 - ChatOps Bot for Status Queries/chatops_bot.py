import os
import requests
import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.rtm_v2 import RTMClient
from slack_sdk.socket_mode import SocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
MONITORING_API_URL = os.getenv("MONITORING_API_URL")
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/chat")

client = WebClient(token=SLACK_BOT_TOKEN)

def get_error_rate():
    print("get_error_rate called")  # Debug
    try:
        resp = requests.get(f"{MONITORING_API_URL}/error_rate")
        print(f"Monitoring API response status: {resp.status_code}")  # Debug
        resp.raise_for_status()
        data = resp.json()
        print(f"Monitoring API response data: {data}")  # Debug
        return f"Current error rate is {data.get('error_rate', 'N/A')}%"
    except Exception as e:
        print(f"Error in get_error_rate: {e}")  # Debug
        return f"Could not fetch error rate: {e}"

def clarify_with_llm(question, raw_answer):
    print(f"clarify_with_llm called with question: {question}, raw_answer: {raw_answer}")  # Debug
    prompt = f"User asked: '{question}'. Monitoring API replied: '{raw_answer}'. Please summarize and clarify for a non-expert."
    payload = {
        "model": "llama2",
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        resp = requests.post(OLLAMA_API_URL, json=payload)
        print(f"Ollama API response status: {resp.status_code}")  # Debug
        resp.raise_for_status()
        lines = resp.text.splitlines()
        print(f"Ollama raw response lines: {lines}")  # Debug
        contents = []
        for line in lines:
            try:
                result = json.loads(line)
                print(f"Parsed Ollama line: {result}")  # Debug
                if "message" in result and "content" in result["message"]:
                    contents.append(result["message"]["content"])
            except Exception as e:
                print(f"Error parsing Ollama line: {e}")  # Debug
                continue
        answer = "".join(contents)
        print(f"Final LLM answer: {answer}")  # Debug
        return answer if answer else "No valid response from Ollama."
    except Exception as e:
        print(f"Error in clarify_with_llm: {e}")  # Debug
        return f"Ollama LLM error: {e}"

# Track processed message timestamps and channel+text to avoid duplicate responses
processed_messages = set()

# Fix: Use Socket Mode for Slack bots (recommended for modern Slack apps)
def handle_socket_mode_event(client, req):
    print(f"handle_socket_mode_event called with req.type: {req.type}")  # Debug
    if req.type == "events_api":
        event = req.payload["event"]
        print(f"Received message: {event.get('text')}, subtype: {event.get('subtype')}, bot_id: {event.get('bot_id')}")  # Debug
        ts = event.get("ts")
        channel_id = event.get("channel")
        text = event.get("text", "")
        # Use a tuple of (channel_id, text) to avoid duplicate answers for same question in channel
        msg_key = (channel_id, text.strip().lower())
        # Only respond to user messages (not bot/self messages) and avoid duplicates
        if (
            event.get("type") == "message"
            and "error rate" in text.lower()
            and not event.get("bot_id")
            and event.get("subtype") is None
            and msg_key not in processed_messages
        ):
            print("Message matched bot logic, preparing response...")  # Debug
            processed_messages.add(msg_key)
            # Notify user that bot is working
            working_msg = client.web_client.chat_postMessage(channel=channel_id, text="Bot is working on your answer...")["ts"]
            raw_answer = get_error_rate()
            answer = clarify_with_llm(text, raw_answer)
            try:
                print(f"Sending message to channel {channel_id}: {answer}")  # Debug
                client.web_client.chat_postMessage(channel=channel_id, text=answer, thread_ts=working_msg)
            except SlackApiError as e:
                print(f"Slack error: {e.response['error']}")
        else:
            print("Message did not match bot logic or was sent by a bot/self or already processed.")  # Debug
        client.ack(req)

if __name__ == "__main__":
    print("Starting ChatOps bot main...")  # Debug
    if not SLACK_APP_TOKEN or not SLACK_BOT_TOKEN:
        print("Missing SLACK_APP_TOKEN or SLACK_BOT_TOKEN in .env")
        exit(1)
    socket_client = SocketModeClient(
        app_token=SLACK_APP_TOKEN,
        web_client=WebClient(token=SLACK_BOT_TOKEN)
    )
    socket_client.socket_mode_request_listeners.append(handle_socket_mode_event)
    print("ChatOps bot is running (Socket Mode)...")
    socket_client.connect()
    import time
    while True:
        time.sleep(1)
