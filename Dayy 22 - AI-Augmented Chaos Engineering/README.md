# Day 22: AI-Augmented Chaos Engineering ⚡ – Aug 28, 2025

## Challenge Description 🎯
Use AI to design chaos experiments that target weak spots in your system. Feed system topology and incident data into an LLM, generate chaos scenarios, and run experiments with LitmusChaos or Gremlin.

## Objective 🚀
- Dynamically load real-world system topology and incident data
- Use LLM to propose chaos experiments (kill DB node, throttle API, etc.)
- Run experiments with LitmusChaos (Kubernetes-native) or Gremlin (hybrid)
- Visualize and analyze experiment results

## Code & Implementation 💻
- **Notebook**: [`chaos_engineering_ai.ipynb`](./chaos_engineering_ai.ipynb)  
  Main workflow for data loading, LLM prompt construction, chaos scenario generation, YAML orchestration, and results visualization.
- **Step-by-Step Solution**: [`Step-by-Step-Solution.md`](./Step-by-Step-Solution.md)  
  Detailed explanation of each notebook step, including rationale and insights.
- **Sample Data**:  
  - `system_topology.json` / `system_topology.yaml` – system architecture
  - `past_incidents.json` / `past_incidents.yaml` – incident history
- **Output**:  
  - `chaos_experiments.md` – LLM-generated chaos scenarios
  - `chaos_experiments.csv` – parsed experiment table
  - `chaos_verdicts.csv` – experiment results

## Workflow 🔄

1. **Load Data:**  
   Dynamically load system topology and incident data from JSON/YAML files.
2. **Prompt LLM:**  
   Construct a prompt for the LLM to generate chaos experiment scenarios.
3. **Generate & Parse Scenarios:**  
   Save LLM output, parse markdown table, and clean up results.
4. **Visualize:**  
   Bar/Count plots of actions by target service.
5. **Run Experiments:**  
   Generate and apply LitmusChaos YAMLs via kubectl, or use Gremlin for hybrid environments.
6. **Analyze Results:**  
   Collect chaos verdicts and visualize experiment outcomes.

## Why Each Step Was Chosen 📊
- **Dynamic Data Loading:**  
  Enables real-world, non-hardcoded input for chaos engineering.
- **LLM Prompting:**  
  Automates scenario design, targeting system weaknesses.
- **YAML Orchestration:**  
  Bridges AI output with actual chaos tools.
- **Visualization:**  
  Makes experiment coverage and outcomes clear.

## Interpretation of Results 🧠
- **chaos_experiments.md/csv:**  
  Shows proposed experiments, targets, actions, and expected outcomes.
- **chaos_verdicts.csv:**  
  Summarizes experiment status and verdicts for review.

## What Did I Learn 🧩
- LLMs can automate chaos scenario design, but output must be parsed and validated.
- Dynamic data loading is essential for real-world applicability.
- Visualization clarifies experiment coverage and risk areas.
- Integration with chaos tools (LitmusChaos/Gremlin) enables practical testing.

## How to Use in Real-World DevOps/SRE 🌍

### Automated Chaos Experiment Design
**Use Case:**  
Rapidly generate and execute chaos experiments based on live system data.

**Implementation:**  
- Feed topology and incident data into notebook
- Generate YAMLs and run experiments with LitmusChaos or Gremlin
- Visualize and analyze results for reliability improvements

**Industry Examples:**  
- SaaS teams testing database failover
- Platform teams validating API resilience

## Where Was AI Used? 🤖

- **AI Used:**  
  Local LLM (Ollama, e.g. Llama3) was used to generate chaos scenarios from structured system and incident data.

**AI Technologies Used:**  
- Llama3 (LLM, via Ollama)
- Python (prompt orchestration, YAML generation, visualization)
- LitmusChaos (Kubernetes-native chaos tool)
- Gremlin (hybrid chaos tool)

## References 📖
- [LitmusChaos Documentation](https://docs.litmuschaos.io/)
- [Gremlin Documentation](https://www.gremlin.com/docs/)
- [Ollama Documentation](https://ollama.com/docs)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## Future Enhancements 🚀
- Add support for more chaos actions (network, disk, CPU, etc.)
- Integrate with CI/CD pipelines for automated reliability testing
- Correlate chaos results with system metrics (Grafana/Prometheus)
- Extend to multi-cluster and multi-cloud environments
