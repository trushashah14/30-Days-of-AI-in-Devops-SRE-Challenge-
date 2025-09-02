# Day 24: Automated Test Scenario Generation – Step-by-Step Solution

---

## Step 1: Introduction & Planning

**Why:**  
Manual test authoring is slow and error-prone. AI can automate scenario generation, improving coverage and speeding up reviews.

**How:**  
- Outline the workflow: extract function schema, prompt LLM, parse/classify tests, render HTML, export PDF.

**What did I get?**  
A clear roadmap for automated test scenario generation.

---

## Step 2: Extract Function Schema

**Why:**  
Relevant tests require understanding the code structure.

**How:**  
- Parse the target Python file using AST.
- Extract function names, input arguments, types, and any rules from docstrings.

**What did I get?**  
A schema dictionary describing all functions and their inputs.

---

## Step 3: Generate Test Cases with LLM

**Why:**  
Automate scenario design, improving coverage and reducing manual effort.

**How:**  
- Construct a prompt using the extracted schema.
- Send the prompt to the LLM (Ollama API, Llama 3).
- Receive test cases as either a Python list or code block.

**What did I get?**  
Actionable unit and integration test cases.

---

## Step 4: Parse and Classify Test Cases

**Why:**  
Structure the LLM output for further processing and reporting.

**How:**  
- Use regex to extract individual test function blocks from the LLM output.
- Parse each block to get function name, description, input, and expected output.
- Classify each test as unit, edge, or integration based on its description.

**What did I get?**  
A list of structured test case dictionaries.

---

## Step 5: Render HTML Report

**Why:**  
Visualize the generated test scenarios for review and documentation.

**How:**  
- Render the structured test cases into an HTML table.
- Include function name, input, expected output, description, and test type.

**What did I get?**  
An HTML report summarizing all generated test scenarios.

---

## Step 6: Export to PDF

**Why:**  
Create a portable, shareable test report.

**How:**  
- Convert the HTML report to PDF using pdfkit.

**What did I get?**  
A PDF file containing all generated test scenarios.

---

## Step 7: Orchestration

**Why:**  
Automate the entire workflow from code to test report.

**How:**  
- Run `main.py <path_to_code_file>`.
- The script executes all steps: extraction, LLM call, parsing, classification, rendering, and export.

**What did I get?**  
A fully automated pipeline for AI-generated test scenario documentation.

---
