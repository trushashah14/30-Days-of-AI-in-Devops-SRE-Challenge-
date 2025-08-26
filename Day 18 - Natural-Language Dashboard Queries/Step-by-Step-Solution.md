# 📋 Step-by-step Solution – Day 18: Natural-Language Dashboard Queries

---

## 📝 Step 1: Introduction & Planning

**Why:**  
PromQL is powerful but not intuitive for all users. Enabling natural language queries in Grafana makes dashboards more accessible and actionable for SRE/DevOps teams.

**How:**  
Use Llama 3 via Ollama to translate user requests into PromQL, then query Grafana and display results.

**What did I get:**  
A notebook workflow for conversational dashboard queries using local LLM inference.

---

## ⚙️ Step 2: Environment Setup

**How:**  
- Install Python packages:
  ```bash
  pip install pandas requests python-dotenv
  ```
- Install and start Ollama:
  - Download from [ollama.com](https://ollama.com/)
  - Start server:
    ```bash
    ollama serve
    ```
- Pull the Llama 3 model:
  ```bash
  ollama pull llama3
  ```
- Set up `.env` file with:
  ```
  GRAFANA_API_KEY=your_grafana_api_key
  GRAFANA_URL=http://localhost:3000
  PROMETHEUS_UID=your_prometheus_uid
  ```

**What did I get?**  
A secure, configurable environment for LLM-powered dashboard queries.

---

## 📄 Step 3: Data Preparation

**How:**  
- Ensure Prometheus is collecting metrics (e.g., `errors_total`).
- Grafana is connected to Prometheus.
- Store API keys and config in `.env` for security.

**What did I get?**  
Live metrics available for querying and a secure config setup.

---

## 🧠 Step 4: Prompt Engineering

**How:**  
- Format prompts for Llama 3 to translate natural language to PromQL.
- Example prompt in notebook:
  ```
  You are a PromQL expert. Convert the following natural-language query into a valid PromQL expression:
  Query: "Show me last week's error rate"
  PromQL:
  ```

**What did I get?**  
Effective prompts for accurate query generation.

---

## 🤖 Step 5: LLM Integration (Ollama Llama 3)

**How:**  
- Use Python to send the prompt to Ollama's Llama 3 model via REST API.
- Stream and collect the model's response.
- Extract PromQL from the LLM output.

**What did I get?**  
Automated PromQL generation from natural language queries.

---

## 🛠️ Step 6: Query Grafana with PromQL

**How:**  
- Send the generated PromQL to Grafana using API credentials from `.env`.
- Parse the Grafana response and extract time series data.

**What did I get?**  
Automated dashboard querying and data retrieval.

---

## 💾 Step 7: Display Results

**How:**  
- Parse and display results in a pandas DataFrame for easy analysis.
- Visualize time series data directly in the notebook.

**What did I get?**  
Clear, actionable dashboard results from natural language queries.

---