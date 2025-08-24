# Day 17: Postmortem Key-Item Extractor – Step-by-Step Solution 🛠️

This guide explains how to extract postmortem key items from incident reports using Llama 3 and Ollama.

---

## Step 1: Prepare Environment ⚙️

**Why:**  
You need the right tools and data.

**How:**  
- Install Python packages:
  ```
  pip install pandas requests
  ```
- Install and start Ollama:
  - Download from [ollama.com](https://ollama.com/)
  - Start server:
    ```
    ollama serve
    ```
- Pull the Llama 3 model:
  ```
  ollama pull llama3
  ```

**What did I get:**  
A working local LLM setup.

---

## Step 2: Prepare Data 📄

**Why:**  
Incident reports are the input for extraction.

**How:**  
- Place your incident report(s) in a file named `raw_data.json` in this folder.

**What did I get:**  
Structured input data for the workflow.

---

## Step 3: Run the Notebook 🚀

**Why:**  
Automate extraction and reporting.

**How:**  
- Open `extractor.ipynb` in Jupyter or VS Code.
- Run all cells.

**What did I get:**  
Extracted key items displayed and saved.

---

## Step 4: Review Results 📊

**Why:**  
Validate and use the extracted insights.

**How:**  
- Extracted key items will be displayed in the notebook.
- Results are saved to:
  - `llama3_extracted_postmortem.csv`
  - `llama3_extracted_postmortem.json`

**What did I get:**  
Ready-to-use structured postmortem data.

