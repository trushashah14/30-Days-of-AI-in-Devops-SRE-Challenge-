# Day 13: Auto-Updating Documentation – Step-by-Step Solution 🛠️

This guide explains how to detect infrastructure changes and generate human-readable changelog entries using LLaMA 2 via Ollama.

---

## Step 1: Introduction & Planning 📝
**Why:**  
Manual changelog writing is slow and inconsistent. Automating it improves clarity and saves time.

**How:**  
Use Python to detect diffs and LLM to summarize them.

**What did I get:**  
A reproducible pipeline that auto-generates changelog entries from Helm or IaC changes.

---

## Step 2: Install Required Tools 🧩
**Why:**  
You need Python libraries and Ollama to run LLaMA 2 locally.

**How:**  
```sh
pip install requests --quiet
ollama pull llama2
```

**What did I get:**  
All dependencies installed and model ready to run.

---

## Step 3: Prepare Sample Files 📄
**Why:**  
You need old and new versions of Helm or Terraform files to test the workflow.

**How:**  
Use `helm_old.yaml` and `helm_new.yaml`, or `iac_old.tf` and `iac_new.tf`.

**What did I get:**  
Test files to simulate infrastructure changes.

---

## Step 4: Detect Diffs with Python 🔍
**Why:**  
You need to extract meaningful changes between file versions.

**How:**  
Use `difflib.unified_diff()` in `diff_detector.py`.

**What did I get:**  
A clean diff string ready for LLM summarization.

---

## Step 5: Summarize Diff with LLaMA 2 🤖
**Why:**  
Raw diffs are hard to read — LLMs can translate them into plain English.

**How:**  
Use `summarise_diff.py` to send the diff to Ollama and get a summary.

**What did I get:**  
Bullet-point summary of infrastructure changes.

---

## Step 6: Append to Changelog 📘
**Why:**  
You want to store summaries in a versioned, readable format.

**How:**  
Use `update_changelog.py` to write the summary to `CHANGELOG.md`.

**What did I get:**  
Auto-updated changelog with timestamped entries.

---

## Step 7: Run the Full Pipeline 🚀
**Why:**  
Test the workflow end-to-end.

**How:**  
```sh
python update_changelog.py --old helm_old.yaml --new helm_new.yaml --type helm
```

**What did I get:**  
A complete changelog entry generated and saved.

---

## What Did I Learn 🧩
- LLMs can automate documentation with clarity and consistency
- Python’s diff tools are powerful for infra change detection
- Combining AI with DevOps workflows creates high-impact tools

---