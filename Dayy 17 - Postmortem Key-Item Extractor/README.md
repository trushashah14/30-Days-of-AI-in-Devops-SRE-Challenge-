# Day 17: Postmortem Key-Item Extractor 🛠️ – Aug 24, 2025

## Challenge Description 🎯
Automatically extract root causes, action items, and owners from incident reports using Llama 3 via Ollama.

## Objective 🚀
- Analyze incident write-ups with Llama 3
- Extract key postmortem items into structured JSON
- Save and visualize results for SRE/DevOps teams

## Code & Implementation 💻
- **Notebook**: [`extractor.ipynb`](./extractor.ipynb)  
  Main workflow for prompt formatting, LLM inference, extraction, and reporting.
- **Step-by-Step Solution**: [`STEP-BY-STEP.md`](./STEP-BY-STEP.md)  
  Detailed guide for setup, workflow, and interpretation.
- **Sample Data**:  
  - `raw_data.json` – incident report(s) for extraction
- **Output**:  
  - Extracted postmortem items in CSV and JSON

## Workflow 🔄
1. **Prepare Environment:**  
   Install Python dependencies, start Ollama, and pull the Llama 3 model.
2. **Prepare Data:**  
   Place incident report(s) in `raw_data.json`.
3. **Run Notebook:**  
   Format prompt, send to Llama 3, extract and display key items.
4. **Save Results:**  
   Output CSV and JSON files for further analysis.

## Why Each Step Was Chosen 📊
- **LLM Extraction:**  
  Automates manual postmortem analysis, saving time and improving consistency.
- **Prompt Engineering:**  
  Ensures the LLM understands the extraction task and outputs structured results.
- **Visualization & Saving:**  
  Makes extracted insights actionable for SRE/DevOps teams.

## Interpretation of Results 🧠
- **Extracted JSON:**  
  Shows root cause, action items, and owners in a machine-readable format.
- **DataFrame & CSV:**  
  Enables further analysis, reporting, and integration with other tools.

## What Did I Learn 🧩
- LLMs can automate tedious postmortem analysis.
- Prompt clarity is critical for reliable extraction.
- Local LLMs (Ollama) are practical for DevOps workflows.
- Output formats (JSON/CSV) make results easy to use downstream.

## How to Use in Real-World DevOps/SRE 🌍

### Automated Postmortem Extraction
**Use Case:**  
Speed up incident review and reporting by automatically extracting key items from write-ups.

**Implementation:**  
- Integrate the extractor into incident management workflows.
- Use extracted action items to drive follow-up and accountability.
- Aggregate root causes for trend analysis and reliability improvements.

**Industry Examples:**  
- **Cloud Outage Review:**  
  After a major outage, the SRE team runs the extractor on incident reports to quickly summarize causes and owners for executive review.
- **Compliance Audits:**  
  Automated extraction ensures all required postmortem fields are present for regulatory reporting.
- **Continuous Improvement:**  
  Action items are tracked and visualized to monitor progress on reliability initiatives.

## Where Was AI Used? 🤖

- **AI Used:**  
  Llama 3 (LLM) for natural language understanding and structured extraction.

**AI Technologies Used:**  
- Ollama (local LLM runner)
- Python (prompt formatting, API calls, data handling)

## References 📖
- [Ollama Documentation](https://ollama.com/docs)
- [Llama 3 Model Card](https://ollama.com/library/llama3)

## Future Enhancements 🚀
- Batch processing for multiple incidents
- Schema validation for extracted JSON
- Integration with ticketing and reporting tools
