# Day 12: AI-Powered Incident Impact Estimator 📉 – Aug 19, 2025

## Challenge Description 🎯
Estimate business impact (e.g., revenue loss, user sessions affected) from incident metadata using LLMs.

## Objective 🚀
- Ingest incident metadata (timestamps, affected services, traffic data)
- Use an LLM to estimate business impact based on historical patterns and service criticality

## Code & Implementation 💻
- **Impact Estimator Script**: [`impact_estimator.py`](./impact_estimator.py)  
  Main logic for ingesting incident data, prompting LLM, and estimating impact.
- **Step-by-Step Solution**: [`Step-by-Step-Solution.md`](./Step-by-Step-Solution.md)  
  Detailed guide for setup, workflow, and interpretation.
- **Sample Incident Data**: [`incidents.csv`](./incidents.csv)  
  Example incidents with timestamps, affected services, and traffic data.


## Workflow 🔄
1. **Prepare Incident Data:**  
   Use `incidents.csv` or API to ingest incident metadata.
2. **Run Impact Estimator Script:**  
   Start `impact_estimator.py` to prompt LLM and estimate impact.
3. **Review Estimates:**  
   Compare LLM estimates with postmortem analysis.
4. **Test in Notebook:**  
   Use `impact_estimator_demo.ipynb` for interactive testing and validation.

## Example Inputs & Outputs 💬
- Inputs: Incident start/end, affected services, traffic/users, historical impact data
- Outputs: Estimated revenue loss, sessions affected

## References 📖
- [OpenAI API Docs](https://platform.openai.com/docs/)
- [Ollama Documentation](https://ollama.com/)
- [Incident Postmortem Best Practices](https://www.atlassian.com/incident-management/postmortem)
- [Business Impact Analysis](https://www.ready.gov/business-impact-analysis)

## Future Enhancements 🚀
- Integrate with live incident management systems
- Use advanced LLMs for more accurate estimation
- Add visualization and reporting features
- Automate feedback loop for model improvement

---
