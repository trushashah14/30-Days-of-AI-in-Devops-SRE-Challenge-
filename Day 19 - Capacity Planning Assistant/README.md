# Day 19: Capacity Planning Assistant 📈 – Aug 26, 2025

## Challenge Description 🎯
Automate capacity planning for DevOps/SRE teams by forecasting resource needs and generating a comprehensive planning document using Llama 3 via Ollama.

## Objective 🚀
- Forecast CPU, memory, disk, and network usage for the next quarter
- Visualize resource trends and growth
- Use LLM to draft a capacity planning document with recommendations

## Code & Implementation 💻
- **Notebook**: [`capacity_planning.ipynb`](./capacity_planning.ipynb)  
  Main workflow for data loading, forecasting, visualization, LLM prompt formatting, and document generation.
- **Step-by-Step Solution**: [`Step-by-Step-Solution.md`](./Step-by-Step-Solution.md)  
  Detailed guide for setup, workflow, and interpretation.
- **Sample Data**:  
  - `resource_metrics.csv` – historical resource metrics (auto-generated if missing)
- **Output**:  
  - Forecast tables and plots  
  - Markdown capacity planning document (`capacity_plan.md`)

## Workflow 🔄
1. **Prepare Environment:**  
   Install Python dependencies, start Ollama, and pull the Llama 3 model.
2. **Prepare Data:**  
   Place historical metrics in `resource_metrics.csv` (or let the notebook generate a sample).
3. **Run Notebook:**  
   Forecast resource usage, visualize trends, format markdown tables, and send prompt to Llama 3.
4. **Generate Document:**  
   LLM drafts a detailed capacity planning document with recommendations and action items.
5. **Save Results:**  
   Output markdown document for review and stakeholder sharing.

## Why Each Step Was Chosen 📊
- **Forecasting:**  
  Provides data-driven projections for resource needs.
- **Visualization:**  
  Makes trends and risks clear for decision makers.
- **LLM Document Generation:**  
  Automates the creation of actionable, stakeholder-ready planning documents.

## Interpretation of Results 🧠
- **Forecast Tables & Plots:**  
  Show expected resource usage growth and potential bottlenecks.
- **Capacity Plan Document:**  
  Summarizes findings, recommendations, and next steps for scaling.

## What Did I Learn 🧩
- Time-series models are effective for resource forecasting.
- LLMs can automate documentation and recommendations.
- Streaming LLM output and prompt engineering are key for complete results.

## How to Use in Real-World DevOps/SRE 🌍

### Automated Capacity Planning
**Use Case:**  
Proactively plan infrastructure scaling and resource allocation for upcoming quarters.

**Implementation:**  
- Integrate notebook into regular planning cycles.
- Use LLM-generated documents for executive and engineering reviews.
- Visualize forecasts to guide hardware/cloud purchases.

**Industry Examples:**  
- **Cloud Migration:**  
  Forecast future needs before migrating workloads to cloud.
- **Quarterly Reviews:**  
  Present capacity plans to leadership for budget and scaling decisions.
- **Incident Prevention:**  
  Identify resource risks before they impact reliability.

## Where Was AI Used? 🤖

- **AI Used:**  
  Llama 3 (LLM) for natural language document generation.

**AI Technologies Used:**  
- Ollama (local LLM runner)
- Python (forecasting, visualization, API calls)

## References 📖
- [Statsmodels Forecasting](https://www.statsmodels.org/stable/tsa.html)
- [Ollama Documentation](https://ollama.com/docs)
- [Capacity Planning Best Practices](https://sre.google/sre-book/capacity-planning/)

## Future Enhancements 🚀
- Automate data collection from Prometheus/Grafana
- Add more advanced forecasting models
- Integrate with dashboards and alerting
- Refine LLM prompts for more detailed recommendations
