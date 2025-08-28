# Day 18: Natural-Language Dashboard Queries 🚀 – Aug 25, 2025

## Challenge Description 🎯
Enable SRE/DevOps teams to query Grafana dashboards using natural language (e.g., “Show me last week’s error rate”) and automatically generate the correct PromQL query using Llama 3 via Ollama.

## Objective 🚀
- Translate user requests into PromQL using LLM
- Query Grafana and visualize results
- Make dashboards accessible to all team members

## Code & Implementation 💻
- **Python Script**: [`NLP_Dashboard_queries.py`](./NLP_Dashboard_queries.py)  
  CLI workflow for full automation, including panel creation and visualization.
- **Step-by-Step Solution**: [`Step-by-Step-Solution.md`](./Step-by-Step-Solution.md)  
  Detailed guide for setup, workflow, and interpretation.
- **Sample Data & Config**:  
  - `.env` file for secrets/config
  - `docker-compose.yml` and `prometheus.yml` for monitoring stack setup

## Workflow 🔄
1. **Prepare Environment:**  
   Install Python dependencies, start Ollama, and pull the Llama 3 model.
2. **Configure Secrets:**  
   Store Grafana API key, URL, and Prometheus UID in `.env`.
3. **Run Script:**  
   Format prompt, send to Llama 3 via Ollama, generate PromQL, query Grafana, and display results.

## Why Each Step Was Chosen 📊
- **LLM Extraction:**  
  Automates PromQL generation, reducing manual effort and errors.
- **Prompt Engineering:**  
  Ensures the LLM understands the query and outputs valid PromQL.
- **Visualization:**  
  Makes dashboard data accessible and actionable.
- **Panel Automation:**  
  Adds results directly to Grafana dashboards for team visibility.

## Interpretation of Results 🧠
- **Generated PromQL:**  
  Shows how natural language is mapped to PromQL.
- **Grafana Output:**  
  Time series data visualized for easy analysis.
- **Panel Creation:**  
  New panels are added to dashboards automatically.

## What Did I Learn 🧩
- LLMs can bridge the gap between natural language and technical queries.
- Prompt clarity is key for reliable PromQL generation.
- Local LLMs (Ollama) are practical for secure, fast inference.
- Full automation is possible from query to dashboard visualization.

## How to Use in Real-World DevOps/SRE 🌍

### Conversational Dashboard Queries
**Use Case:**  
Empower engineers and stakeholders to ask questions in plain English and get instant dashboard insights.

**Implementation:**  
- Integrate the notebook or backend into Grafana as a plugin or API.
- Use LLM to translate queries and automate dashboard updates.

**Industry Examples:**  
- **Incident Review:**  
  Quickly visualize error rates, latency, or resource usage by asking natural language questions.
- **Executive Reporting:**  
  Non-technical users can generate custom dashboard views without learning PromQL.
- **Continuous Improvement:**  
  Teams can explore metrics and trends conversationally to drive reliability.

## Where Was AI Used? 🤖

- **AI Used:**  
  Llama 3 (LLM) for natural language to PromQL translation.

**AI Technologies Used:**  
- Ollama (local LLM runner)
- Python (prompt formatting, API calls, data handling, visualization)

## References 📖
- [Grafana Plugin Development](https://grafana.com/docs/grafana/latest/developers/plugins/)
- [PromQL Documentation](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- [Ollama Documentation](https://ollama.com/docs)

## Future Enhancements 🚀
- Add support for more query types and dashboards
- Improve prompt engineering for complex queries
- Integrate as a Grafana plugin for direct UI access
- Enhance visualization and panel automation
