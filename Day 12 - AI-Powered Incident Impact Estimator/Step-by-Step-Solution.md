# Day 12: AI-Powered Incident Impact Estimator – Step-by-Step Solution 📉

This guide explains how to estimate business impact from incident metadata using LLMs and compare with postmortem analysis.

---

## Step 1: Introduction & Planning 📝
**Why:**  
Estimating business impact helps prioritize incident response and improve postmortem accuracy.

**How:**  
Feed incident metadata and traffic data into an LLM, prompt it to estimate impact, and compare with actual postmortem results.

**What did I get:**  
A clear workflow for AI-powered impact estimation.

---

## Step 2: Install Required Libraries 🧩
**Why:**  
You need pandas for data handling, requests for LLM API, and optionally python-dotenv for secrets.

**How:**  
```sh
pip install pandas requests python-dotenv --quiet
```

**What did I get:**  
All necessary Python libraries installed.

---

## Step 3: Prepare Incident Metadata 📄
**Why:**  
Incident data is needed for estimation.

**How:**  
- Create `incidents.csv` with columns: `incident_id,start_time,end_time,affected_services,traffic,actual_revenue_loss,actual_sessions_affected`
- Add historical incidents for context.

**What did I get:**  
A dataset of incidents and their business impact.

---

## Step 4: Prompt LLM for Impact Estimation 🤖
**Why:**  
LLMs can use historical patterns and service criticality to estimate impact.

**How:**  
- For each incident, send metadata and traffic data to the LLM via API.
- Use a prompt like:  
  `"Given the following incident details and historical impact, estimate the revenue loss and sessions affected."`
- Parse and save the LLM's estimate.

**What did I get:**  
AI-generated impact estimates for each incident.

---

## Step 5: Compare Estimates with Postmortem Analysis 📊
**Why:**  
Validate LLM accuracy and usefulness.

**How:**  
- Compare LLM estimates with actual postmortem values in the dataset.
- Calculate error metrics (absolute error, percentage error).

**What did I get:**  
A comparison of AI estimates vs. real-world impact.

---

## Step 6: Review & Iterate 🔄
**Why:**  
Improve prompts and data for better estimation.

**How:**  
- Refine prompts, add more historical data, and tune LLM parameters.
- Gather feedback from incident managers.

**What did I get:**  
An iterative process for improving impact estimation.

--

## What Did I Learn 🧩
- LLMs can provide useful impact estimates from incident metadata.
- Comparing AI estimates with postmortem analysis helps validate and improve the workflow.
- Data quality and prompt engineering are key to accurate estimation.

---
