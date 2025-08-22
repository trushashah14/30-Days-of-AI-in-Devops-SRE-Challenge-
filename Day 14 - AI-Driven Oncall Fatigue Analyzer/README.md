# Day 14: SRE Oncall Fatigue Analyzer 🧠 – Aug 21, 2025

## Challenge Description 🎯  
This project was created to help SRE/DevOps teams measure and visualize on-call fatigue using real incident data. By quantifying fatigue and generating rotation suggestions, teams can proactively prevent burnout, improve fairness, and make better decisions about on-call schedules.

## Objective 🚀  
- Compute daily fatigue scores based on alert volume and sleep disruption  
- Aggregate monthly fatigue metrics per engineer  
- Flag high-fatigue patterns using configurable thresholds  
- Generate tiered rotation suggestions (off-call, monitor, fallback)  
- Output clean CSVs for notebook visualization and team dashboards  

## Code & Implementation 💻  
- **Fatigue Scorer**: [`fatigue_model.py`](./fatigue_model.py)  
  Computes daily fatigue scores using: `score = total_alerts + 2 × night_alerts`  
- **Rotation & Summary Logic**: [`suggest_rotation_tweaks.py`](./suggest_rotation_tweaks.py)  
  Aggregates monthly metrics and generates tiered rotation suggestions  
- **Analysis Runner**: [`run_analysis.py`](./run_analysis.py)  
  End-to-end pipeline for generating all outputs  
- **Notebook Visualizer**: [`visualise_output.ipynb`](./visualise_output.ipynb)  
  Renders fatigue summaries and rotation plans with Markdown and styling  
- **Sample Data**:  
  - [`data/mock_incidents.csv`](./data/mock_incidents.csv)  
  - [`data/fatigue_scores.csv`](./data/fatigue_scores.csv)  
  - [`data/fatigue_summary.csv`](./data/fatigue_summary.csv)  
  - [`data/rotation_plan.csv`](./data/rotation_plan.csv)  
- **Documentation**:  
  - [`README.md`](./README.md)  
  - [`Step-by-Step-Solution.md`](./Step-by-Step-Solution.md)  

## Workflow 🔄  
1. Generate or load incident data and compute daily fatigue scores  
2. Aggregate monthly metrics per engineer  
3. Apply tiered logic to generate rotation suggestions  
4. Visualize results in notebook or export to dashboards  

## Why Each Step Was Chosen 📊  
- **Weighted scoring**: Night alerts disrupt sleep, so they’re weighted ×2  
- **Tiered logic**: Enables strategic planning, not just reactive alerts  
- **CSV outputs**: Modular, reproducible, and easy to visualize  

## Interpretation of Results 🧠  
- 🔴 Rotate off-call: High fatigue, needs rest  
- 🟠 Monitor closely: Moderate fatigue, borderline  
- 🟢 Eligible for fallback or lead: Stable fatigue profile  

## How to Use in Real-World SRE 🌍  

### Monthly Rotation Planning  
**Use Case:**  
Generate fatigue summaries and rotation plans for SRE teams  

**Implementation:**  
- Run the analyzer post-incident cycle  
- Share summaries with team leads  
- Use fallback tier to assign backup leads  

**Advantage:**  
- Makes SRE health visible and actionable  
- Improves fairness and transparency in rotations  

**Industry Example:**  
An SRE team uses this tool to review monthly fatigue. Engineers with high scores are rotated off-call, while low-fatigue engineers are assigned as fallback leads. This improves team morale and reduces burnout.

## Future Enhancements 🚀  
- Integrate with PagerDuty or Opsgenie APIs  
- Add visualization of fatigue trends over time  
- Export summaries to Markdown or HTML  
- Include fallback pairing logic based on fatigue tiers

<<<<<<< HEAD
## Where Was AI Used? 🤖

- **AI Used:**  
  ML logic (Python, pandas) was used to compute fatigue scores based on incident volume and sleep disruption.  
  Tiered recommendations for rotation planning were generated using rule-based AI logic.  
  LLM (Llama2 via Ollama) was used to generate human-readable summaries and explanations in notebooks and documentation.

**AI Technologies Used:**
- Scikit-learn (ML models: regressors, clustering, anomaly detection)
- Llama2 (LLM, via Ollama for summarization and documentation)
- Python (for orchestration and data processing)
=======
---
>>>>>>> d946b232ba0e4b59854631cf7e398a24ef82a2ac
