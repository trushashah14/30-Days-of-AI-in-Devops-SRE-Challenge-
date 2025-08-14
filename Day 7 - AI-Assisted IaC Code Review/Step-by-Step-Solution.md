# Day 7: AI-Assisted IaC Code Review – Step-by-Step Solution 🤖

This document explains each step of the notebook, why it is needed, how it was implemented, and what insights were gained. It also discusses the difference between static analysis and LLM review, and how to interpret the results.

---

## Step 1: Introduction & Planning 📝
**Why:**  
Clarifies the goal: to review Terraform IaC files using tfsec (static analysis) and Ollama LLM, comparing the strengths of each approach.

**How:**  
A markdown cell outlines the workflow: find Terraform files, run tfsec, review with LLM, compare outputs.

**What did I get:**  
A clear roadmap for automated IaC code review.

---

## Step 2: Install Required Libraries 🧩
**Why:**  
Requests is needed for LLM API calls; tfsec must be available for static analysis.

**How:**  
`!pip install requests --quiet` (tfsec installed separately)

**What did I get:**  
All necessary tools installed locally.

---

## Step 3: Import Libraries 📚
**Why:**  
To use requests for API calls and subprocess for running tfsec.

**How:**  
Standard Python imports.

**What did I get:**  
Access to functions for static analysis and LLM review.

---

## Step 4: Find Terraform Files 🕒
**Why:**  
To locate all `.tf` files for analysis.

**How:**  
Walk the workspace and collect paths to `.tf` files.

**What did I get:**  
A list of Terraform files to review.

---

## Step 5: Run Static Analysis with tfsec 🛡️
**Why:**  
tfsec scans Terraform files for security issues and misconfigurations.

**How:**  
Run tfsec on each file's directory, save output to markdown files in `Iac analysis` folder.

**What did I get:**  
A summary of security findings for each file.

---

## Step 6: LLM Review of Terraform Files (Ollama) 🤖
**Why:**  
LLM provides context-aware, human-friendly feedback and can catch issues missed by static tools.

**How:**  
Send each file and its tfsec output to Ollama API, save feedback to markdown files in `Iac analysis` folder.

**What did I get:**  
Detailed, actionable review for each file.

---

## Step 7: Compare Outputs & Draw Conclusions 📊
**Why:**  
To understand the strengths and limitations of static analysis vs. LLM review.

**How:**  
Print and compare tfsec and LLM outputs for each file, summarize differences.

**What did I get:**  
Insight into which tool provides more useful feedback and why.

---

## Step 8: Temporary Limitation for Testing ⚡
**Why:**  
Running LLM on all files can be slow; for testing, only `vpc.tf` is analyzed.

**How:**  
Filter the list of files to just `vpc.tf` in a temporary code cell.

**What did I get:**  
Faster iteration during development; can be removed later.

---

