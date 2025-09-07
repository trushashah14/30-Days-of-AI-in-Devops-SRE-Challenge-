# Day 30: AI-Powered “Resilience Replay” Generator 🎥🛠️ – Sept 6, 2025

## Challenge Description 🎯
Reconstruct how your system should have behaved during an incident — like a flight recorder for infrastructure — using ML simulation and LLM-powered narrative replay.

## Objective 🚀
- Feed in incident metadata: timestamps, affected services, expected SLAs, and historical baselines
- Use ML models to simulate expected system behavior under normal conditions
- Compare actual vs. simulated behavior to pinpoint deviation zones
- Use an LLM to narrate the replay, highlighting what should have happened vs. what actually occurred

## Code & Implementation 💻
- **Notebook**: `resilience_replay.ipynb`  
  Main workflow for data loading, ML simulation, deviation analysis, and LLM replay narration.
- **Step-by-Step Solution**: `Step-by-Step-Solution.md`  
  Detailed guide for setup, workflow, and interpretation.
- **Sample Data**:  
  - `incident_metadata.csv` – incident timestamps, affected services, expected SLAs
  - `historical_baseline.csv` – historical normal system metrics
  - `actual_metrics.csv` – actual metrics during the incident
- **Output**:  
  - Replay narrative comparing actual vs. simulated behavior, deviation zones, and actionable insights

## Workflow 🔄
1. **Prepare Data:**  
   Collect incident metadata, historical baselines, and actual incident metrics.
2. **ML Simulation:**  
   Use time-series or regression models to simulate expected system behavior under normal conditions.
3. **Deviation Analysis:**  
   Compare actual vs. simulated metrics to identify deviation zones and root causes.
4. **LLM Replay Narration:**  
   Use LLM (Ollama, OpenAI, etc.) to generate a narrative replay, highlighting key deviations and what should have happened.
5. **Report:**  
   Output replay narrative and deviation analysis for review and postmortems.

## Why Each Step Was Chosen 📊
- **ML Simulation:**  
  Provides objective, data-driven baseline for expected system behavior.
- **Deviation Analysis:**  
  Pinpoints exactly where and when the system diverged from normal.
- **LLM Replay:**  
  Transforms technical findings into actionable, stakeholder-friendly incident narratives.

## Usage

Open and run `resilience_replay.ipynb` in Jupyter.

## Requirements

- Python 3.8+
- `pandas`, `scikit-learn`, `requests` (for LLM API)

## Interpretation of Results 🧠
- **Replay Narrative:**  
  “At 14:03, Service B should have autoscaled to 6 pods. Instead, it stalled at 2, causing cascading latency in Service C.”
- **Deviation Zones:**  
  Pinpointed times and metrics where actual behavior diverged from expected.

## How to Use in Real-World DevOps/SRE 🌍

### Incident Replay & Postmortem Analysis
**Use Case:**  
Reconstruct incidents for root cause analysis, training, and reliability improvement.

**Implementation:**  
- Integrate notebook into postmortem workflows
- Use replay narratives for team learning and stakeholder communication

**Industry Examples:**  
- Autoscaling failures
- Cascading latency or outages
- SLA breaches and recovery analysis

## Where Was AI Used? 🤖

- **AI Usage:**  
  ML simulation for baseline generation, deviation analysis, LLM for replay narrative generation.

**AI Technologies Utilized:**  
- Python (scikit-learn for simulation, pandas for data prep)
- Ollama/OpenAI (LLM for replay narration)

## References 📖
- [Incident Replay Best Practices](https://sre.google/sre-book/postmortem-culture/)
- [Ollama Documentation](https://ollama.com/docs)
- [ML for Time-Series Simulation](https://www.statsmodels.org/stable/tsa.html)

## Future Enhancements 🚀
- Integrate with real-time monitoring and alerting
- Automate replay generation for all incidents
- Add visualization of deviation zones


