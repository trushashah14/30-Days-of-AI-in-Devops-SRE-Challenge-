# Day 10: ChatOps Bot for Status Queries – Step-by-Step Solution 🤖

This guide walks you through building a Slack ChatOps bot that answers operational status queries (like “What’s current error rate?”) using your monitoring API and an LLM (Ollama) for clear, human-friendly responses.

---

## Step 1: Introduction & Planning 📝
**Why:**  
Enable real-time, conversational status checks in Slack for SRE/DevOps teams.

**How:**  
Outline the workflow: connect Slack bot, fetch metrics from monitoring API, summarize with LLM, and reply in Slack.

**What did I get:**  
A clear roadmap for ChatOps status automation.

---

## Step 2: Install Required Libraries 🧩
**Why:**  
You need Slack SDK, python-dotenv, requests for API calls, and Ollama for LLM integration.

**How:**  
```sh
pip install slack-sdk python-dotenv requests
```

**What did I get:**  
All necessary Python packages installed.

---

## Step 2.5: Create a Mock Monitoring API 🛠️
**Why:**  
You need a testable endpoint for your bot to fetch metrics.

**How:**  
Create a simple Flask API (`mock_monitoring_api.py`) with endpoints like `/error_rate`, `/latency`, `/health`:
```python
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/error_rate')
def error_rate():
    return jsonify(error_rate=0.7)

@app.route('/latency')
def latency():
    return jsonify(latency=120)

@app.route('/health')
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(port=5000)
```
Run this file before starting your bot.

**What did I get:**  
A local API for your bot to query metrics.

---

## Step 3: Configure Environment & Tokens 🔑
**Why:**  
Slack bot and app tokens, monitoring API URL, and Ollama API URL are required for secure integration.

**How:**  
Add these to your `.env` file:
```
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
SLACK_APP_TOKEN=xapp-your-app-token
MONITORING_API_URL=http://localhost:5000
OLLAMA_API_URL=http://localhost:11434/api/chat
```

**What did I get:**  
Environment variables set for authentication and API access.

---
## Step 3.1: Local Testing with Notebook (`chatops_bot_demo.ipynb`) 🧪
**Why:**  
Test your bot logic and LLM integration locally before deploying to Slack.

**How:**  
- Use the provided notebook (`chatops_bot_demo.ipynb`) to simulate status queries and LLM summarization.
- The notebook sends sample questions to your monitoring API and gets summarized answers from Ollama.
- This helps debug and verify your workflow without needing Slack.

**What did I get:**  
A quick way to test and validate the bot's logic and LLM output locally.

---

## Step 4: Create & Configure Slack App ⚙️
**Why:**  
You need a Slack app with the right permissions and event subscriptions.

**How:**  
- Create a new Slack app at [Slack API: Your Apps](https://api.slack.com/apps).
- Enable Socket Mode.
- Add an App-Level Token (`xapp-...`) with `connections:write` scope.
- Add a Bot Token (`xoxb-...`) with scopes:
  - `chat:write`
  - `channels:history`
  - `app_mentions:read`
  - `im:history` (for DM support)
- Enable Event Subscriptions and subscribe to `message.channels`.
- Install the app to your workspace.
- Invite the bot to your channel using `/invite @your-bot-name`.

**What did I get:**  
A Slack app ready to receive and respond to channel messages.

---

## Step 5: Start Monitoring API & Ollama 🟢
**Why:**  
The bot needs a running monitoring API and LLM backend.

**How:**  
- Run your Flask monitoring API (`mock_monitoring_api.py`) on port 5000.
- Start Ollama with `ollama serve` and pull the required model (`ollama pull llama2` or `llama3`).

**What did I get:**  
Monitoring and LLM services running locally.

---

## Step 6: Run the Bot Script 🚀
**Why:**  
Start the bot so it can listen for Slack messages and respond to operational queries in real time.

**How:**  
- Create the main Python bot script (`chatops_bot.py`) with the following features:
  - Loads environment variables from `.env` for Slack tokens, monitoring API, and Ollama API.
  - Connects to Slack using Socket Mode (`slack_sdk.socket_mode`).
  - Listens for messages in channels where the bot is invited.
  - Matches queries like "What's current error rate?", "What's current latency?", and "Is the API healthy?".
  - Fetches metrics from your Flask monitoring API endpoints (`/error_rate`, `/latency`, `/health`).
  - Sends the raw metric to Ollama LLM for summarization and clarity.
  - Immediately posts "Bot is working on your answer..." in the channel for user feedback.
  - Replies with the summarized answer in a thread under the working message.
  - Ignores duplicate questions and bot/self messages.
  - Prints debug logs for every step, including received messages, API responses, and LLM output.

- To run the bot:
  ```sh
  python chatops_bot.py
  ```
  - The bot will connect to Slack via Socket Mode and display debug logs in your terminal.
  - You should see logs for every message received and every answer sent.

**What did I get:**  
A fully functional Python ChatOps bot script that connects to Slack, listens for status queries, fetches metrics, summarizes with LLM, and responds in real time with user feedback and deduplication.

---

## Step 7: Interact in Slack 💬
**Why:**  
Test the bot’s ability to answer status queries.

**How:**  
- Send `What's current error rate?` in the channel.
- The bot will immediately reply with "Bot is working on your answer..." and then post the summarized answer in a thread.

**What did I get:**  
Conversational, real-time status answers in Slack.
- ![Slack Output](Slack_output.png)  <!-- Screenshot of bot response in Slack -->

---

## Step 7.1: Supported Questions & Extending Bot Logic 💡
**Why:**  
Make your bot more useful by supporting more queries.

**How:**  
With your current `mock_monitoring_api.py`, you can ask:
- `"What's current error rate?"` (calls `/error_rate`)
- `"What's current latency?"` (calls `/latency`)
- `"Is the API healthy?"` (calls `/health`)

You can extend your bot to recognize these questions and call the corresponding endpoint.  
For example, add logic to your bot to match:
- `"Show me the latency"` or `"How fast is the API?"` → `/latency`
- `"Is everything healthy?"` or `"API health status"` → `/health`

**What did I get:**  
A flexible ChatOps bot that can answer a variety of operational questions based on your monitoring API endpoints.

---



## Step 8: Bot Features & Logic 🧠

- Responds to "What's current error rate?" in any channel it's invited to.
- Shows a "Bot is working on your answer..." message immediately so users know the bot is processing.
- Replies with the summarized answer in a thread under the working message.
- Ignores duplicate messages (does not answer the same question twice).
- Ignores bot/self messages and only responds to plain user messages.
- Debug print statements show every step and message received.

---

## Step 9: Troubleshooting & Debugging 🛠️

**If the bot does not respond:**
- Check your terminal for debug logs.
- Make sure the bot is invited to the channel.
- Ensure all tokens and URLs are correct.
- Reinstall the app after changing permissions or event subscriptions.
- Confirm event subscriptions (`message.channels`) are enabled.
- Make sure monitoring API and Ollama are running.

**Debugging tips:**
- Watch for `Received message:` logs in your terminal.
- Check for Slack errors or API issues in the logs.
- Use print statements to trace the bot’s logic.

---

## What Did I Learn 🧩
- Slack Socket Mode is required for modern bots; both bot and app tokens are needed.
- Event subscriptions and permissions must be set up for the bot to receive messages.
- Ollama can be used as a local LLM to summarize and clarify monitoring metrics.
- Real-time feedback ("Bot is working...") improves user experience.
- Deduplication logic prevents repeated answers for the same question.

---

