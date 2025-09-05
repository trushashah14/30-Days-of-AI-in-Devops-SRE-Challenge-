# Day 27: AI-Powered Service Ownership Mapper 🧠🔍 – Sept 3, 2025

## Challenge Description 🎯
Automatically infer service ownership across teams using commit history, alert response patterns, and ticket assignments. Use ML clustering and LLMs to generate a service catalog entry for each microservice.

## Objective 🚀
- Analyze commit metadata, alert acknowledgments, and ticket assignments
- Use ML clustering to infer likely owners or responsible teams for each service
- Use LLM to generate human-friendly service catalog entries

## Code & Implementation 💻
- **Notebook**: `service_ownership_mapper.ipynb`  
  Main workflow for data loading, ML clustering, ownership inference, and LLM catalog generation.
- **Step-by-Step Solution**: `Step-by-Step-Solution.md`  
  Detailed guide for setup, workflow, and interpretation.
- **Sample Data**:  
  - `commits.csv` – Git commit metadata (author, service, timestamp)
  - `alerts.csv` – Alert acknowledgments (service, responder, timestamp)
  - `tickets.csv` – Ticket assignments (service, assignee, timestamp)

### How to Get Real Data

- **Commits:**  
  Export commit history using `git log --pretty=format:'%an,%s,%ad' --date=iso` and map commit messages/services.
- **Alerts:**  
  Export alert acknowledgments from your monitoring tool (e.g., Prometheus Alertmanager, PagerDuty) as CSV.
- **Tickets:**  
  Export ticket assignments from your ticketing system (e.g., Jira, ServiceNow) as CSV.

- Clean and map data so each row contains:  
  - Service name  
  - Contributor/Responder/Assignee  
  - Timestamp

- Place these files in the project folder for notebook analysis.

## Example Sample Data

See `commits.csv`, `alerts.csv`, and `tickets.csv` in this folder for format.

## Output 📤
  - Service catalog entries summarizing ownership and recent changes

## Workflow 🔄
1. **Prepare Data:**  
   Collect commit, alert, and ticket data for all services.
2. **ML Clustering:**  
   Cluster contributors/responders/assignees by service to infer ownership.
3. **LLM Catalog Generation:**  
   Use LLM (Ollama, OpenAI, etc.) to generate catalog entries for each service.
4. **Report:**  
   Output catalog entries for review and sharing.

## Why Each Step Was Chosen 📊
- **ML Clustering:**  
  Finds patterns in contributor and responder data to infer ownership.
- **LLM Catalog:**  
  Generates clear, actionable documentation for teams.

## Usage

Open and run `service_ownership_mapper.ipynb` in Jupyter.

## Requirements

- Python 3.8+
- `pandas`, `scikit-learn`, `requests` (for LLM API)

## Interpretation of Results 🧠
- **Catalog Entry:**  
  “Service X is primarily maintained by Team Y, with recent changes by Z.”

## How to Use in Real-World DevOps/SRE 🌍

### Automated Service Ownership Mapping
**Use Case:**  
Quickly identify responsible teams for incident response, audits, and onboarding.

**Implementation:**  
- Integrate notebook into regular reviews
- Use catalog for incident routing and compliance

**Industry Examples:**  
- Ownership mapping for microservices
- Audit and compliance documentation

## Where Was AI Used? 🤖

- **AI Usage:**  
  - Data fusion and normalization: Contributor, alert, and ticket data are merged and standardized using pandas.
  - Ownership inference: Weighted scoring logic automatically determines the most likely maintainer and recent contributors from behavioral data.
  - ML clustering: Spectral Clustering (with cosine similarity) groups services by contributor overlap, revealing organizational patterns and cross-team dependencies.
  - LLM-driven documentation: Ollama Llama 3 generates stakeholder-friendly, context-aware service catalog entries from structured metadata, including cluster group context and service relationships.

**AI Technologies Utilized:**  
- Python (pandas for data fusion and normalization, scikit-learn for clustering and inference)
- Ollama/OpenAI (LLM for catalog entry generation via API calls in the notebook)

## References 📖
- [Scikit-learn Clustering](https://scikit-learn.org/stable/modules/clustering.html)
- [Ollama Documentation](https://ollama.com/docs)
- [Service Ownership Best Practices](https://sre.google/sre-book/service-ownership/)

## Future Enhancements 🚀
- Integrate with CI/CD and monitoring tools
- Add visualization of ownership graphs
- Automate catalog updates

## How Does the AI Pipeline Work? 🤖

It’s not just “feeding data to an LLM.”  
This solution is a multi-stage AI pipeline that automates and enriches service documentation using both ML and LLMs:

### 🔹 Stage 1: Data Fusion

- Pulls contributor data from commits, alerts, and tickets.
- Normalizes and merges it across sources — something humans rarely do consistently.

### 🔹 Stage 2: Ownership Inference

- Uses weighted scoring logic to infer the most likely maintainer.
- This is not manually provided — it’s derived from behavioral data.
- Recent contributors are also inferred, not hardcoded.

### 🔹 Stage 3: Clustering

- Uses Spectral Clustering + cosine similarity to group services by contributor overlap.
- Reveals organizational patterns (e.g., which services are maintained by the same team) — not something you’d get from raw data.

### 🔹 Stage 4: LLM-Driven Narrative Generation

- The LLM takes structured metadata and generates stakeholder-friendly summaries.
- Transforms raw data into natural language documentation — something that would take hours manually.
- Can optionally infer relationships, describe service roles, and contextualize clusters.

---

### 🧾 So Why Not Just Write It Yourself?

Because this pipeline:

- Scales across hundreds of services.
- Adapts to changing contributor behavior.
- Standardizes documentation format.
- Reduces cognitive load for SREs and PMs.
- Surfaces hidden patterns (e.g., shadow ownership, cross-team dependencies).
