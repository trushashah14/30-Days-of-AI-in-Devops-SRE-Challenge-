# Day 14: SRE Fatigue Analyzer – Step-by-Step Solution 🧠

This guide walks through how to compute fatigue scores and generate rotation plans using incident data and the provided Python scripts.

---

## Step 1: Introduction & Planning 📝  
**Why:**  
On-call fatigue affects SRE performance and morale. Quantifying it enables proactive planning.

**How:**  
Use weighted scoring and tiered logic to generate actionable summaries.

**What did I get:**  
A reproducible pipeline that outputs fatigue metrics and rotation suggestions.

---

## Step 2: Prepare Incident Data 📄  
**Why:**  
You need realistic incident data to compute fatigue.

**How:**  
- Use `mock_api.pagerduty_mock.generate_mock_incidents()` to generate mock incidents for a list of engineers.
- Save as `data/mock_incidents.csv`.

**What did I get:**  
Mock data for reproducible scoring and demo use.

---

## Step 3: Compute Daily Fatigue Scores 🔢  
**Why:**  
You need to quantify fatigue per engineer per day.

**How:**  
- Run `fatigue_model.py` (function: `compute_fatigue_scores`) to compute:
  ```
  fatigue_score = total_alerts + 2 × night_alerts
  ```
- Night alerts are those between 10 PM and 6 AM.
- Save as `data/fatigue_scores.csv`.

**What did I get:**  
`fatigue_scores.csv` with daily scores per engineer.

---

## Step 4: Summarize Monthly Metrics 📊  
**Why:**  
You need to aggregate fatigue trends over time.

**How:**  
- Use `summarize_fatigue()` from `suggest_rotation_tweaks.py` to compute:
  - Total days on-call
  - Average and max fatigue
  - Days above threshold (default threshold: 4)
- Save as `data/fatigue_summary.csv`.

**What did I get:**  
`fatigue_summary.csv` with monthly metrics.

---

## Step 5: Generate Rotation Plan 📋  
**Why:**  
You want actionable suggestions for the next month.

**How:**  
- Use `generate_monthly_rotation_plan()` from `suggest_rotation_tweaks.py` with tiered logic:
  - 🔴 Rotate off-call (max fatigue ≥ 7 or ≥ 3 days above threshold)
  - 🟠 Monitor closely (max fatigue ≥ threshold or ≥ 1 day above threshold)
  - 🟢 Eligible for fallback or lead (otherwise)
- Save as `data/rotation_plan.csv`.

**What did I get:**  
`rotation_plan.csv` with suggested actions and reasons.

---

## Step 6: Visualize in Notebook 📘  
**Why:**  
You want to present results clearly to stakeholders.

**How:**  
- Use `visualise_output.ipynb` to render Markdown explanations and styled tables.
- Display full rotation suggestions table (no truncation).
- Plot fatigue metrics by engineer.

**What did I get:**  
Readable summaries and rotation plans in notebook format.

---

## Step 7: Extend or Integrate 🚀  
**Why:**  
Make the tool more powerful and production-ready.

**How:**  
- Add fallback pairing logic
- Export to HTML or Markdown
- Integrate with incident APIs
- Visualize fatigue trends over time

**What did I get:**  
A strategic, demo-ready fatigue analyzer for SRE teams.

---