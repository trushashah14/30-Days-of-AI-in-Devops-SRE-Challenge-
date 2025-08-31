# Day 24: Automated Test Scenario Generation – Step-by-Step Solution

---

## Step 1: Extract Function Schema

**Why:**  
We need to understand the structure of the code to generate relevant tests.

**How:**  
- Parse the target Python file using AST.
- Extract function names, input arguments, types, and any rules from docstrings.

**Result:**  
A schema dictionary describing all functions and their inputs.

---

## Step 2: Generate Test Cases with LLM

**Why:**  
Automate the creation of test scenarios for each function.

**How:**  
- Construct a prompt using the extracted schema.
- Send the prompt to the LLM (Ollama API).
- Receive test cases as either a Python list or code block.

**Result:**  
Raw test case code or strings from the LLM.

---

## Step 3: Parse and Classify Test Cases

**Why:**  
Structure the LLM output for further processing and reporting.

**How:**  
- Use regex to extract individual test function blocks from the LLM output.
- Parse each block to get function name, description, input, and expected output.
- Classify each test as unit, edge, or integration based on its description.

**Result:**  
A list of structured test case dictionaries.

---

## Step 4: Render HTML Report

**Why:**  
Visualize the generated test scenarios for review and documentation.

**How:**  
- Render the structured test cases into an HTML table.
- Include function name, input, expected output, description, and test type.

**Result:**  
An HTML report summarizing all generated test scenarios.

---

## Step 5: Export to PDF

**Why:**  
Create a portable, shareable test report.

**How:**  
- Convert the HTML report to PDF using pdfkit.

**Result:**  
A PDF file containing all generated test scenarios.

---

## Step 6: Orchestration

**Why:**  
Automate the entire workflow from code to test report.

**How:**  
- Run `main.py <path_to_code_file>`.
- The script executes all steps: extraction, LLM call, parsing, classification, rendering, and export.

**Result:**  
A fully automated pipeline for AI-generated test scenario documentation.

---
