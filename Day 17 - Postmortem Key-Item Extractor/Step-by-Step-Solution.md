# 📋 Step-by-step Solution – Day 17: Postmortem Key-Item Extractor

---

## 📝 Step 1: Introduction & Planning

### 🎯 Overview
Manual extraction of postmortem key items from incident reports is slow and inconsistent. This workflow uses Llama 3 (via Ollama) to automate extraction of root causes, action items, and owners, making postmortem analysis faster and more reliable for DevOps/SRE teams.

### ❓ Key Questions and Answers

**1. Why automate postmortem extraction?**
- Saves time and reduces human error
- Ensures consistent structure for reporting and analysis
- Enables faster incident review and follow-up

**2. Why use Llama 3 and Ollama?**
- Llama 3 is a state-of-the-art open-source LLM
- Ollama allows easy local inference without cloud dependencies
- Python integration enables flexible workflows

---

## ⚙️ Step 2: Environment Setup

### 💻 Implementation

**How to set up your environment:**
- Install Python packages:
  ```bash
  pip install pandas requests
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
- Python environment ready for data handling and API calls

---

## 📄 Step 3: Data Preparation

### 🎯 Overview
Incident reports are the input for extraction. Place them in a file named `raw_data.json`.

**Why this format?**
- JSON is easy to parse and structure for LLM prompts
- Supports single or multiple incident reports

**What did I get?**
- Structured input data for the workflow

---

## 🧠 Step 4: Prompt Engineering

### 💻 Implementation

**How is the prompt constructed?**
- The notebook formats each incident report into a prompt that asks Llama 3 to extract:
  - Root Cause
  - Action Items
  - Responsible Owners
- The prompt requests a JSON output for easy parsing

**Why this approach?**
- Clear instructions improve LLM extraction accuracy
- Structured output simplifies downstream processing

---

## 🤖 Step 5: LLM Inference with Ollama

### 💻 Implementation

**How does the notebook interact with Ollama?**
- Checks if Ollama is running locally
- Sends the formatted prompt to Llama 3 via Ollama's REST API
- Streams and collects the model's response

**Why stream the response?**
- Handles large outputs efficiently
- Avoids timeouts and incomplete results

**What did I get?**
- Raw LLM output containing extracted key items

---

## 🛠️ Step 6: Output Extraction & Validation

### 💻 Implementation

**How is the output processed?**
- The notebook parses the LLM output to extract the JSON block
- Validates the extracted JSON for expected keys
- Displays the result and loads it into a pandas DataFrame

**Why this step?**
- Ensures reliable extraction for further analysis
- Provides immediate feedback on extraction quality

**What did I get?**
- Machine-readable postmortem key items
- Tabular view for easy inspection

---

## 💾 Step 7: Saving Results

### 💻 Implementation

**How are results saved?**
- Extracted key items are saved to:
  - `llama3_extracted_postmortem.csv` (tabular format)
  - `llama3_extracted_postmortem.json` (structured format)

**Why save in both formats?**
- CSV is ideal for spreadsheets and reporting
- JSON is ideal for automation and integration

**What did I get?**
- Ready-to-use files for further analysis or integration

---

## 🏆 Step 8: Troubleshooting & Best Practices

### ❓ Common Issues & Solutions

- **Ollama not running:**  
  Start Ollama with `ollama serve`
- **Model not found:**  
  Run `ollama pull llama3` and check with `ollama list`
- **Timeouts or slow output:**  
  - Use a smaller model (`llama3:8b`)
  - Reduce prompt/context size
  - Lower `num_predict` in the notebook
- **404 errors:**  
  Ensure the model name in the notebook matches the name shown by `ollama list`
- **No JSON found:**  
  Refine the prompt for clearer instructions


