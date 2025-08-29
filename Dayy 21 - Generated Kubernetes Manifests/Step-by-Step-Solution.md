# Day 21: Generated Kubernetes Manifests – Step-by-Step Solution

---

## Step 1: Introduction & Planning

**Why:**  
Manual YAML authoring for Kubernetes is error-prone and slow. Automating manifest generation with LLMs saves time and reduces mistakes.

**How:**  
A markdown cell outlines the workflow: define service, prompt LLM, extract YAML, validate, and save.

**What did I get:**  
A clear roadmap for automated manifest generation.

---

## Step 2: Install Required Libraries

**Why:**  
Requests is needed for API calls to Ollama. PyYAML is used for YAML parsing and validation.

**How:**  
- Use `!pip install requests --quiet` to install requests.
- Use `pip install pyyaml` if not already installed.

**What did I get:**  
All necessary tools installed locally.

---

## Step 3: Import Libraries

**Why:**  
To use requests for API calls, yaml for parsing/validation, and standard Python utilities.

**How:**  
- Import `requests` for HTTP API calls.
- Import `yaml` for YAML parsing and validation.

**What did I get:**  
Access to functions for LLM orchestration and YAML validation.

---

## Step 4: Define Service Requirements

**Why:**  
Captures all necessary fields for manifest generation (name, image, replicas, ports, env).

**How:**  
- Create a Python dictionary with service details.
- Print the description for confirmation.

**What did I get:**  
A structured service definition for prompt construction.

---

## Step 5: Prepare Prompt for LLM

**Why:**  
Clear, detailed prompts improve LLM output quality and completeness.

**How:**  
- Format a prompt string describing the service and requesting only YAML output.
- Specify separation of resources with '---'.

**What did I get:**  
A ready-to-send prompt for manifest generation.

---

## Step 6: Call Ollama API for YAML Output

**Why:**  
Automates manifest generation using LLM, reducing manual effort.

**How:**  
- Send the prompt to Ollama API.
- Receive the response and extract the YAML output.

**What did I get:**  
LLM-generated YAML for Deployment and Service.

---

## Step 7: Extract and Save Only YAML Code

**Why:**  
LLMs may include explanations or markdown; only YAML should be saved and validated.

**How:**  
- Use a function to extract only YAML blocks (ignore code fences, explanations, and backticks).
- Write the cleaned YAML to `deployment_and_service.yaml`.

**What did I get:**  
A file containing only valid YAML code.

---

## Step 8: Validate YAML Syntax

**Why:**  
Ensures the generated YAML is syntactically correct before applying to Kubernetes.

**How:**  
- Use PyYAML to parse all YAML documents in the file.
- Print the number of resources and any errors.

**What did I get:**  
Validation output confirming readiness for deployment.

---
