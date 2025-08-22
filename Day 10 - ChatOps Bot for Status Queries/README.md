# Day 10: ChatOps Bot for Status Queries 🤖 – Aug 17, 2025

## Challenge Description 🎯
Build a Slack ChatOps bot that answers operational status queries like “What’s current error rate?” by integrating with your monitoring API and summarizing responses using an LLM (Ollama). Visualize, interpret, and automate status checks for DevOps/SRE teams.

## Objective 🚀
- Create a Slack ChatOps bot for real-time status queries
- Integrate with a monitoring API (e.g., Prometheus, custom Flask API)
- Use Ollama (local LLM) to clarify and summarize raw metrics
- Respond in Slack channels with actionable, human-friendly answers
- Provide instant feedback ("Bot is working...") and avoid duplicate answers

## Code & Implementation 💻
- **Bot Script**: [`chatops_bot.py`](./chatops_bot.py)  
  Main bot logic for Slack integration, monitoring API queries, LLM summarization, and duplicate handling.
- **Step-by-Step Solution**: [`Step-by-Step-Solution.md`](./Step-by-Step-Solution.md)  
  Detailed guide for setup, configuration, and workflow.
- **Notebook**: [`chatops_bot_demo.ipynb`](./chatops_bot_demo.ipynb)  
  Example workflow, test queries, and bot interaction demo.
- **Mock Monitoring API**: [`mock_monitoring_api.py`](./mock_monitoring_api.py)  
  Simple Flask API to simulate error rate and latency metrics.

## Workflow 🔄
1. **Configure Environment:**  
   Set up `.env` with Slack bot token, app token, monitoring API URL, and Ollama API URL.
2. **Start Monitoring API & Ollama:**  
   Run Flask API and Ollama server with the required model.
3. **Run Bot Script:**  
   Start `chatops_bot.py` to listen for status queries in Slack.
4. **Ask Status Questions:**  
   Send queries like “What’s current error rate?” in a channel.
5. **Bot Feedback:**  
   Bot posts "Bot is working on your answer..." immediately, then replies in a thread with the summarized answer.
6. **Duplicate Handling:**  
   Bot ignores repeated questions and only answers once per unique query.

## Why Each Feature Was Chosen 📊

- **Instant Feedback Message:**  
  Lets users know the bot is processing their request, improving UX during LLM/API delays.

- **Threaded Replies:**  
  Keeps the channel clean and organizes bot answers under the working message.

- **Duplicate Detection:**  
  Prevents spam and repeated answers for the same question.

- **Debug Logging:**  
  Prints every step and received message for easy troubleshooting.

## Interpretation of Bot Responses 🧠

- **Human-Friendly Summaries:**  
  Ollama transforms raw metrics into clear, actionable insights for non-experts.

- **Real-Time Status Checks:**  
  SREs and engineers can query system health instantly in Slack.

- **Threaded Answers:**  
  Responses are easy to find and follow, even during busy incident channels.

## What Did I Learn 🧩
- Slack Socket Mode is required for modern bots; both bot and app tokens are needed.
- Event subscriptions and permissions must be set up for the bot to receive messages.
- Ollama can be used as a local LLM to summarize and clarify monitoring metrics.
- Real-time feedback ("Bot is working...") improves user experience.
- Deduplication logic prevents repeated answers for the same question.

## How to Use in Real-World DevOps/SRE 🌍

### ChatOps Status Automation
**Use Case:**  
Empower on-call engineers to instantly check production error rates, latency, or health metrics in Slack during a live incident or deployment.

**Implementation:**  
- Integrate Slack bot with your monitoring API and Ollama LLM.
- Bot listens for status queries and replies with clear, actionable summaries.
- Uses threaded replies to keep conversations organized.

**Advantage:**  
- Reduces time spent searching dashboards or waiting for manual updates.
- Enables rapid, data-driven decision making during outages or releases.

**Industry Example:**  
A global e-commerce company uses the bot during Black Friday sales. When a spike in error rate is detected, engineers query the bot in Slack and receive a concise summary, allowing them to quickly pinpoint and resolve checkout issues before customers are impacted.

---

### Bot Features for Team Collaboration
**Use Case:**  
Streamline cross-team communication by providing a single source of truth for system status in Slack, especially during high-pressure launches or incident bridges.

**Implementation:**  
- Bot posts "Bot is working..." for immediate feedback, then replies in a thread with the full answer.
- Deduplication logic ensures only one answer per unique query, preventing noise.
- Threaded responses keep status updates grouped and easy to follow.

**Advantage:**  
- Prevents repeated questions and answers, reducing channel clutter.
- Ensures everyone sees the same, up-to-date information.

**Industry Example:**  
A healthcare SaaS provider uses the bot during a major platform upgrade. Multiple teams ask about API health and error rates in a shared Slack channel; the bot answers each query once, in a thread, so all teams stay aligned and focused on the upgrade without confusion or duplicate information.

## Where Was AI Used? 🤖

- **AI Used:**  
  Local LLM (Ollama, e.g. Llama2) was used to summarize and clarify raw monitoring metrics for Slack bot responses.  
  The bot uses LLM to transform API data into human-friendly answers.

**AI Technologies Used:**  
- Llama2 (LLM, via Ollama)
- Python (Slack bot orchestration, API integration)

## References 📖
- [Slack Socket Mode](https://api.slack.com/apis/connections/socket)
- [Slack Bots with Python](https://slack.dev/python-slack-sdk/)
- [Ollama Documentation](https://ollama.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [ChatOps Best Practices](https://www.atlassian.com/incident-management/chatops)

## Future Enhancements 🚀
- Add support for Teams and Discord
- Enable multi-metric queries and dashboards
- Integrate with incident management and alerting
- Add authentication and role-based access
- Use RAG or custom LLMs for deeper context


