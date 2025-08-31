# Day 24: Automated Test Scenario Generation 🚀 – Sept 1, 2025

## Challenge Description 🎯
Enable SRE/DevOps teams to automatically generate Python test scenarios for code changes using LLMs (Ollama + Llama 3). The workflow parses code, prompts the LLM, and produces a structured test report in HTML and PDF.

## Objective 🚀
- Extract function schemas from Python code
- Generate actionable test cases using LLM
- Classify, visualize, and export test scenarios
- Automate the entire workflow for rapid feedback

## Code & Implementation 💻
- **Main Script:** [`main.py`](./main.py)  
  Orchestrates extraction, LLM call, parsing, classification, rendering, and PDF export.
- **Step-by-Step Solution:** [`Step-by-Step-Solution.md`](./Step-by-Step-Solution.md)  
  Detailed guide for workflow, logic, and troubleshooting.
- **Supporting Modules:**  
  - [`code_parser.py`](./code_parser.py): Extracts function schemas
  - [`llm_driver.py`](./llm_driver.py): Handles LLM API calls and output parsing
  - [`classifier.py`](./classifier.py): Classifies test types
  - [`renderer.py`](./renderer.py): Renders HTML and exports PDF

## Workflow 🔄
1. **Extract Function Schema:**  
   Parse the target Python file using AST to get function names, arguments, types, and rules.
2. **Generate Test Cases with LLM:**  
   Send the schema to Ollama (Llama 3) and receive test cases as code or strings.
3. **Parse & Classify Test Cases:**  
   Extract test functions, parse metadata, and classify as unit, edge, or integration.
4. **Render HTML Report:**  
   Visualize all test cases in a structured HTML table.
5. **Export to PDF:**  
   Convert the HTML report to PDF for sharing and documentation.

## Why Each Step Was Chosen 📊
- **Schema Extraction:**  
  Ensures tests are relevant to the actual code structure.
- **LLM Generation:**  
  Automates scenario design, improving coverage and reducing manual effort.
- **Classification:**  
  Helps prioritize and organize test types for review.
- **Visualization & Export:**  
  Makes results accessible and actionable for teams.

## Usage

```bash
python main.py <path_to_code_file>
```
- Generates a PDF report named `test_report.pdf` in the current directory.
- All steps are logged for debugging and traceability.

## Requirements

- Python 3.8+
- `pdfkit`, `requests`
- Ollama server running with Llama 3 model
- wkhtmltopdf installed for PDF export

## Interpretation of Results 🧠
- **Generated Test Cases:**  
  Shows how code structure is mapped to actionable test scenarios.
- **HTML/PDF Output:**  
  Human-readable report for review and documentation.
- **Classification:**  
  Highlights unit, edge, and integration tests for coverage analysis.

## What Did I Learn 🧩
- LLMs can automate test scenario generation from code structure.
- Prompt clarity and schema extraction are key for reliable results.
- Full automation is possible from code to test documentation.

## How to Use in Real-World DevOps/SRE 🌍

### Automated Test Scenario Generation
**Use Case:**  
Empower engineers to quickly generate and review test coverage for new code changes.

**Implementation:**  
- Integrate the workflow into CI/CD pipelines for instant feedback.
- Use the PDF report for code reviews and compliance documentation.

**Industry Examples:**  
- **Pull Request Review:**  
  Instantly generate and visualize test scenarios for changed code.
- **Release Validation:**  
  Ensure all new features and bug fixes are covered by tests.
- **Continuous Improvement:**  
  Use AI-generated scenarios to drive better coverage and reliability.

## Where Was AI Used? 🤖

- **AI Used:**  
  Llama 3 (LLM) for test scenario generation.

**AI Technologies Used:**  
- Ollama (local LLM runner)
- Python (schema extraction, prompt formatting, API calls, reporting)

## References 📖
- [Ollama Documentation](https://ollama.com/docs)
- [wkhtmltopdf](https://wkhtmltopdf.org/)
- [Python AST Module](https://docs.python.org/3/library/ast.html)

## Future Enhancements 🚀
- Add support for more languages and test frameworks
- Improve prompt engineering for complex code
- Integrate with CI/CD for automated test validation
- Enhance visualization and reporting features
