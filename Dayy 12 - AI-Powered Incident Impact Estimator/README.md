# Day 12: AI-Powered Incident Impact Estimator 📉 – Aug 19, 2025

## Challenge Description 🎯
Estimate the business impact of incidents using a hybrid ML + LLM workflow. Predict affected sessions and revenue loss using a trained ML model, and generate stakeholder-ready summaries using an LLM.

## Objective 🚀
- Train ML models to predict `sessions_affected` and `revenue_loss_usd`
- Use incident metadata (traffic, severity, root cause, etc.) as input
- Generate business impact summaries using LLM prompts
- Output structured predictions and readable summaries to CSV
- View results in tabular format for analysis and reporting

## Code & Implementation 💻
- **ML Training Script**: [`train_model.py`](./train_model.py)  
  Trains regressors for session and revenue prediction using historical incident data.
- **Prediction Pipeline**: [`impact_estimator.py`](./impact_estimator.py)  
  Loads new incidents, runs ML predictions, and generates summaries via LLM.
- **LLM Summary Generator**: [`generate_summary.py`](./generate_summary.py)  
  Wraps LLM API call to produce concise business impact summaries.
- **Training Data**: [`incidents.csv`](./incidents.csv)  
  Historical labeled incidents used for ML training.
- **Synthetic Input**: [`synthetic_incidents.csv`](./synthetic_incidents.csv)  
  New incident metadata for prediction and summary generation.
- **Output**: [`incident_estimates.csv`](./incident_estimates.csv)  
  Final predictions and summaries saved in tabular format.
- **Step-by-Step Solution**: [`Step-by-Step-Solution.md`](./Step-by-Step-Solution.md)  
  Detailed workflow and rationale for each step.

## Workflow 🔄
1. **Prepare Historical Data**  
   Use `incidents.csv` to train ML models on past incident impact.
2. **Train ML Models**  
   Run `train_model.py` to train and save session/revenue regressors.
3. **Load New Incidents**  
   Add new incidents to `synthetic_incidents.csv`.
4. **Run Prediction Pipeline**  
   Execute `impact_estimator.py` to generate predictions and summaries.
5. **Review Output**  
   View `incident_estimates.csv` in Jupyter or Excel for analysis.

## Why Each Step Was Chosen 📊
- **ML Regression**:  
  Provides structured, reproducible numeric predictions.
- **LLM Summary**:  
  Converts raw predictions into stakeholder-friendly language.
- **CSV Output**:  
  Enables easy review, filtering, and dashboard integration.

## Interpretation of Results 🧠
- **Predicted Sessions & Revenue**:  
  Quantifies business impact for each incident.
- **Summary**:  
  Communicates impact clearly to non-technical stakeholders.

## What Did I Learn 🧩
- ML and LLMs can complement each other for structured + narrative outputs.
- Encoding incident metadata enables accurate impact estimation.
- Prompt engineering is key to generating useful summaries.

## How to Use in Real-World DevOps/SRE 🌍

### Incident Impact Estimation for Stakeholders
**Use Case:**  
Estimate and communicate the business impact of incidents in real time.

**Implementation:**  
- Train ML models on historical incident data.
- Use structured metadata to predict impact.
- Generate summaries for execs and product teams using LLM.

**Advantage:**  
- Combines precision with clarity.
- Enables faster postmortems and stakeholder updates.

**Industry Example:**  
An SRE team uses this tool to estimate the impact of checkout failures. ML predicts $10K revenue loss and 8K affected sessions. The LLM generates a summary for the incident report, saving hours of manual analysis.

## Where Was AI Used? 🤖

- **AI Used:**  
  ML regressors (scikit-learn) were trained to predict sessions affected and revenue loss for incidents.  
  LLM (Llama2 via Ollama) was used to generate human-readable business impact summaries from ML predictions and incident metadata.

**AI Technologies Used:**  
- Scikit-learn (ML regression models)  
- Llama2 (LLM, via Ollama for summarization)  
- Python (for orchestration and data processing)


## References 📖
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Requests Documentation](https://docs.python-requests.org/en/master/)
- [Ollama LLM API](https://ollama.com/)
- [Jupyter Notebook](https://jupyter.org/)

## Future Enhancements 🚀
- Add confidence intervals to ML predictions
- Use LLM to generate remediation suggestions
- Build a Streamlit dashboard for real-time impact visibility

