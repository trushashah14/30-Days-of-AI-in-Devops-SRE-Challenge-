# Day 12: AI-Powered Incident Impact Estimator – Step-by-Step Solution 📉

This guide explains how to estimate incident impact using ML predictions and LLM-generated summaries, and how to structure the workflow for reproducibility and clarity.

---

## Step 1: Introduction & Planning 📝
**Why:**  
Manual impact estimation is slow and inconsistent. Automating it improves speed and stakeholder communication.

**How:**  
Use ML to predict numeric impact, and LLM to generate readable summaries.

**What did I get:**  
A hybrid pipeline that combines structured predictions with natural language output.

---

## Step 2: Install Required Libraries 🧩
**Why:**  
You need pandas for data handling, scikit-learn for ML, requests for LLM API calls.

**How:**  
```sh
pip install pandas scikit-learn requests joblib --quiet
```

**What did I get:**  
All dependencies installed for training and prediction.

---

## Step 3: Prepare Historical Incident Data 📄
**Why:**  
ML needs labeled data to learn patterns.

**How:**  
Use `incidents.csv` with columns like traffic, severity, root_cause, actual_revenue_loss, actual_sessions_affected.

**What did I get:**  
A training dataset for regression models.

---

## Step 4: Train ML Models 🧠
**Why:**  
Predict sessions affected and revenue loss from incident metadata.

**How:**  
- Encode severity using OrdinalEncoder  
- Train RandomForestRegressor for each target  
- Save models using joblib

**What did I get:**  
Two trained regressors and an encoder saved to disk.

---

## Step 5: Prepare Synthetic Incidents for Prediction 🧪
**Why:**  
You need new incident metadata to test the pipeline.

**How:**  
Create `synthetic_incidents.csv` with fields like incident_id, traffic, severity, root_cause, etc.

**What did I get:**  
A clean input file for prediction.

---

## Step 6: Run Prediction Pipeline 🚀
**Why:**  
Generate structured predictions and summaries.

**How:**  
- Load models and encoder  
- Predict sessions and revenue  
- Call LLM to generate summary  
- Save results to `incident_estimates.csv`

**What did I get:**  
A complete output file with predictions and summaries.

---

## Step 7: View Results in Jupyter 📊
**Why:**  
Tabular view makes it easier to analyze and share.

**How:**  
```python
import pandas as pd
df = pd.read_csv("incident_estimates.csv")
df
```

**What did I get:**  
A scrollable table of incident impact estimates.

---

## Step 8: Review & Iterate 🔄
**Why:**  
Improve model accuracy and summary quality over time.

**How:**  
- Add more training data  
- Tune model hyperparameters  
- Refine LLM prompts

**What did I get:**  
A scalable, iterative workflow for impact estimation.

---

## What Did I Learn 🧩
- ML regression is effective for numeric impact prediction
- LLMs can generate readable summaries from structured data
- Combining both creates a powerful DevOps/SRE tool
- Tabular outputs make results easy to share and analyze

---