# Day 22: AI-Augmented Chaos Engineering – Step-by-Step Solution

---

## Step 1: Introduction & Planning

**Why:**  
Manual chaos experiment design is slow and may miss system weak spots. AI can automate scenario generation based on real system data.

**How:**  
A markdown cell outlines the workflow: load data, prompt LLM, generate scenarios, run experiments, visualize results.

**What did I get:**  
A clear roadmap for AI-driven chaos engineering.

---

## Step 2: Install Required Libraries

**Why:**  
Requests for API calls, pandas for data handling, seaborn/matplotlib for visualization, yaml for YAML orchestration.

**How:**  
- `!pip install requests pandas matplotlib seaborn pyyaml --quiet`

**What did I get:**  
All necessary tools installed locally.

---

## Step 3: Dynamic Data Loading

**Why:**  
Real-world chaos engineering requires dynamic, non-hardcoded input.

**How:**  
- Load system topology and incident data from JSON/YAML files.
- Prompt user for file paths, fallback to example data if missing.

**What did I get:**  
Flexible, realistic input for scenario generation.

---

## Step 4: LLM Prompt Construction & Scenario Generation

**Why:**  
LLMs can propose chaos experiments tailored to system weaknesses.

**How:**  
- Construct a prompt with system topology and incident data.
- Call Ollama API to generate markdown table of chaos scenarios.

**What did I get:**  
AI-generated chaos experiments with targets, actions, and expected outcomes.

---

## Step 5: Parse & Clean LLM Output

**Why:**  
LLM output may include markdown artifacts or empty rows.

**How:**  
- Parse markdown table, remove header/empty/`---` rows.
- Replace missing/None values in 'Expected Outcome' for clarity.

**What did I get:**  
Cleaned DataFrame of chaos experiments for analysis.

---

## Step 6: Visualize Chaos Actions by Target

**Why:**  
Visualization highlights coverage and risk areas.

**How:**  
- Use seaborn/matplotlib to plot actions by target service.
- Style plots for clarity (rotation, color, integer ticks).

**What did I get:**  
Clear bar chart of experiment coverage.

---

## Step 7: Generate & Apply Chaos YAMLs

**Why:**  
Bridge AI output with actual chaos tools for execution.

**How:**  
- Generate LitmusChaos YAMLs for each experiment.
- Apply YAMLs via kubectl subprocess calls.

**What did I get:**  
Automated chaos experiment execution.

---

## Step 8: Collect & Analyze Chaos Verdicts

**Why:**  
Review experiment outcomes for reliability insights.

**How:**  
- Query chaosresult resources via kubectl.
- Parse and visualize verdicts/status.

**What did I get:**  
Tabular and visual summary of experiment results.

---

