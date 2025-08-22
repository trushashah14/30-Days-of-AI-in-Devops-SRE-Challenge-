# Day 13: Auto-Updating Documentation 🛠️ – Aug 20, 2025

## Challenge Description 🎯
Automatically detect changes in infrastructure files (Helm charts or Terraform IaC) and generate human-readable changelog entries using an LLM.

## Objective 🚀
- Compare old vs new versions of Helm or IaC files
- Extract meaningful diffs using Python
- Use LLaMA 2 via Ollama to summarize changes in plain English
- Append summaries to a structured `CHANGELOG.md`
- Make documentation auto-updating and stakeholder-friendly

## Code & Implementation 💻
- **Diff Detector**: [`diff_detector.py`](./diff_detector.py)  
  Extracts unified diffs between old and new files.
- **LLM Summarizer**: [`summarise_diff.py`](./summarise_diff.py)  
  Sends diffs to LLaMA 2 via Ollama and returns bullet-point summaries.
- **Changelog Updater**: [`update_changelog.py`](./update_changelog.py)  
  Orchestrates the pipeline and appends summaries to `CHANGELOG.md`.
- **Examples**:  
  - [`helm_old.yaml`](./helm_old.yaml) / [`helm_new.yaml`](./helm_new.yaml)  
  - [`iac_old.tf`](./iac_old.tf) / [`iac_new.tf`](./iac_new.tf)  
  Sample files for testing Helm and Terraform diffs.
- **Documentation**:  
  - [`README.md`](./README.md)  
  - [`Step-by-Step-Solution.md`](./Step-by-Step-Solution.md)  
  Full guide and rationale for the workflow.

## Workflow 🔄
1. Prepare old and new versions of your infra files
2. Run `update_changelog.py` with file paths and type
3. LLM summarizes the diff and appends it to `CHANGELOG.md`
4. View changelog in Markdown or render in dashboard

## Why Each Step Was Chosen 📊
- **Diffing**:  
  Captures meaningful changes without parsing entire files.
- **LLM Summarization**:  
  Converts raw diffs into readable, stakeholder-friendly language.
- **Markdown Output**:  
  Easy to version, share, and integrate into docs or dashboards.

## Interpretation of Results 🧠
- **Readable summaries**:  
  Bullet points that explain what changed and why it matters.
- **Auto-updated changelog**:  
  No manual editing required — just run the script.
- **Supports multiple formats**:  
  Works for both Helm and Terraform files.

## What Did I Learn 🧩
- LLMs can automate documentation in a meaningful way
- Structured prompts yield consistent, professional summaries
- Combining diff logic with AI creates powerful DevOps tooling

## How to Use in Real-World DevOps/SRE 🌍

### Auto-Documenting Infra Changes
**Use Case:**  
Generate changelogs for Helm or Terraform updates during CI/CD.

**Implementation:**  
- Run the script post-merge or pre-deploy
- Append summary to release notes or dashboards
- Share with stakeholders or include in postmortems

**Advantage:**  
- Saves time and improves clarity
- Ensures infra changes are documented consistently

**Industry Example:**  
An SRE team uses this tool to auto-document Helm chart updates. When replicas or image tags change, the LLM generates a summary like:  
“Updated replica count from 2 to 4. Changed image tag from v1.2.0 to v1.3.0.”  
This gets appended to the changelog and shared with product teams.

## Where Was AI Used? 🤖

- **AI Used:**  
  LLM (Llama2 via Ollama) was used to automatically summarize infrastructure diffs (Helm/Terraform) into human-readable changelog entries.  
  Python orchestrates the workflow and sends diffs to the LLM for documentation generation.

**AI Technologies Used:**  
- Llama2 (LLM, via Ollama for summarization)
- Python (diff extraction, orchestration)

## References 📖
- [Ollama](https://ollama.com/)
- [LLaMA 2](https://ai.meta.com/llama/)
- [Python difflib](https://docs.python.org/3/library/difflib.html)
- [Markdown Guide](https://www.markdownguide.org/)
- [Terraform Docs](https://developer.hashicorp.com/terraform/docs)
- [Helm Docs](https://helm.sh/docs/)

## Future Enhancements 🚀
- Add support for JSON or Kubernetes manifests
- Use structured output (e.g., JSON changelog entries)
- Integrate with Git hooks or CI pipelines
- Add risk scoring or impact estimation to summaries

