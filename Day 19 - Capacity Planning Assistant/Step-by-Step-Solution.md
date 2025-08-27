# 📋 Step-by-step Solution – Day 19: Capacity Planning Assistant

---

## 📝 Step 1: Introduction & Planning

### 🎯 Overview
Manual capacity planning is slow and error-prone. This workflow uses Llama 3 (via Ollama) and time-series forecasting to automate resource projections and generate actionable recommendations for DevOps/SRE teams.

### ❓ Key Questions and Answers

**1. Why automate capacity planning?**
- Ensures infrastructure can handle future workloads
- Avoids outages and over-provisioning
- Provides data-driven recommendations for scaling

**2. Why use Llama 3 and Ollama?**
- Llama 3 is a state-of-the-art open-source LLM
- Ollama enables fast, local inference
- Python integration allows flexible forecasting and document generation

---

## ⚙️ Step 2: Environment Setup

### 💻 Implementation

**How to set up your environment:**
- Install Python packages:
  ```bash
  pip install pandas numpy matplotlib scikit-learn statsmodels requests python-dotenv
  ```
- Install and start Ollama:
  - Download from [ollama.com](https://ollama.com/)
  - Start server:
    ```bash
    ollama serve
    ```
- Pull the Llama 3 model:
  ```bash
  ollama pull llama3
  ```

**What did I get?**
- Local LLM inference capability
- Python environment ready for forecasting and API calls

---

## 📄 Step 3: Data Preparation

### 🎯 Overview
Resource metrics are the input for forecasting. Place them in a file named `resource_metrics.csv`.

**Why this format?**
- CSV is easy to parse and structure for time-series analysis
- Supports multiple resource types (CPU, memory, disk, network)
- Notebook will auto-generate a sample file if missing

**What did I get?**
- Structured input data for the workflow

---

## 📈 Step 4: Forecasting Resource Needs

### 💻 Implementation

**How is forecasting performed?**
- Load historical metrics into pandas DataFrame
- Use Holt-Winters (Exponential Smoothing) to project usage for the next quarter (90 days)
- Generate forecast tables for each resource

**Why this approach?**
- Holt-Winters is robust for time-series forecasting
- Produces actionable projections for planning

**What did I get?**
- Forecast tables for CPU, memory, disk, and network usage

---

## 📊 Step 5: Visualize Forecasts

### 💻 Implementation

**How are forecasts visualized?**
- Use matplotlib to plot CPU, memory, disk, and network forecasts
- Visualizations help stakeholders understand projected trends

**What did I get?**
- Clear time-series plots for each resource

---

## 🧠 Step 6: Draft Capacity Planning Document with LLM

### 💻 Implementation

**How is the prompt constructed?**
- Format forecast results as markdown tables
- Create a detailed prompt for Llama 3:
- Send the prompt to Ollama with a high `num_predict` value (e.g., 1024) to ensure complete output
- Stream and concatenate the response for full document generation

**Why this approach?**
- Clear instructions improve LLM output completeness
- Streaming avoids truncation and JSON errors

**What did I get?**
- A complete, actionable capacity planning document

---

## 💾 Step 7: Saving Results

### 💻 Implementation

**How are results saved?**
- Save the generated markdown document as `capacity_plan.md`
- Review LLM recommendations and tables
- Share with stakeholders for approval and implementation

**What did I get?**
- Ready-to-use capacity planning document

---