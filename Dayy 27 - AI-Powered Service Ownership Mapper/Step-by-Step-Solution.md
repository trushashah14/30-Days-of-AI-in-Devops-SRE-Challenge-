# 📋 Step-by-step Solution – Day 27: AI-Powered Service Ownership Mapper

---

## 📝 Step 1: Introduction & Planning

### 🎯 Overview
Manual service ownership mapping is slow and error-prone. This workflow uses ML clustering and LLMs to automate ownership inference and generate stakeholder-friendly service catalog entries for microservices.

### 🗺️ Planning
- **Goal:** Automate service ownership mapping and documentation for all microservices.
- **Inputs:** Contributor, alert, and ticket data from multiple sources.
- **Process:** 
  - Normalize and merge data.
  - Infer ownership and contributor relationships using ML clustering.
  - Generate human-friendly catalog entries using LLM.
- **Outputs:** 
  - Service catalog entries with ownership, recent contributors, and cluster context.
- **Benefits:** 
  - Scales to hundreds of services.
  - Reveals hidden ownership and cross-team dependencies.
  - Standardizes documentation for audits and onboarding.

---

## ⚙️ Step 2: Environment Setup

### 💻 Implementation

**How to set up your environment:**
- Install Python packages:
  ```bash
  pip install pandas scikit-learn requests numpy
  ```
- Prepare sample data files:
  - `commits.csv`, `alerts.csv`, `tickets.csv`

**What did I get?**
- Python environment ready for clustering and LLM integration
- Sample and/or real data for analysis

---

## 📄 Step 3: Data Preparation

### 🎯 Overview
Contributor, alert, and ticket data are the input for ownership inference and clustering. Place them in CSV files.

**How to get real data:**
- **Commits:**  
  Use `git log --pretty=format:'%an,%s,%ad' --date=iso` and map commit messages/services.
- **Alerts:**  
  Export alert acknowledgments from monitoring tools (Prometheus, PagerDuty) as CSV.
- **Tickets:**  
  Export ticket assignments from ticketing systems (Jira, ServiceNow) as CSV.

- Ensure each CSV has columns:  
  - `service`, `author` (or `responder`/`assignee`), `timestamp`

- Place these files in the project folder for notebook analysis.

**Why this format?**
- CSV is easy to parse and structure for ML analysis
- Supports multiple contributor types

**What did I get?**
- Structured input data for the workflow

---

## 🤖 Step 4: ML Clustering for Ownership Inference

### 💻 Implementation

- Normalize contributor and service names using pandas.
- Create a binary matrix of services × contributors.
- Use Spectral Clustering (with cosine similarity) to group services by contributor overlap.
- Infer primary owners and recent contributors for each service using weighted scoring logic.

**Why this approach?**
- Clustering reveals organizational patterns and cross-team dependencies.
- Ownership inference is automated from behavioral data, not manually assigned.

**What did I get?**
- Cluster assignments for each service
- Ownership and contributor mapping

---

## 🧠 Step 5: LLM Service Catalog Generation

### 💻 Implementation

- For each service, format a prompt summarizing ownership, recent contributors, and cluster group.
- Send prompt to LLM (Ollama, OpenAI, etc.) to generate a stakeholder-friendly catalog entry:
  ```
  Service: <service>
  Main owner: <owner>
  Recent contributors: <names>
  Cluster group: <cluster>
  Summary: <LLM-generated paragraph>
  ```
- Display catalog entries in Markdown for easy review.

**Why this approach?**
- LLM transforms structured metadata into natural language documentation.
- Saves manual effort and standardizes catalog format.

**What did I get?**
- Human-friendly, context-aware service catalog entries for all services

---

## Example Usage

- Run the notebook to process data and generate catalog entries.
- Review and share the output with teams.

---
