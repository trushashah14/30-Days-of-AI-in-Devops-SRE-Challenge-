import sys
import json
import pdfkit
import requests
import re
import ast
import logging

logging.basicConfig(level=logging.INFO)

# --- Function Schema Extraction ---
def extract_functions_from_file(file_path):
    logging.info("Extracting function schema from: %s", file_path)
    with open(file_path, "r") as f:
        tree = ast.parse(f.read())

    schema = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            inputs = {}
            for arg in node.args.args:
                arg_name = arg.arg
                arg_type = "unknown"
                if arg.annotation:
                    if isinstance(arg.annotation, ast.Name):
                        arg_type = arg.annotation.id
                    elif isinstance(arg.annotation, ast.Subscript):
                        arg_type = "enum" if arg.annotation.value.id == "Literal" else "unknown"
                inputs[arg_name] = {"type": arg_type}

            docstring = ast.get_docstring(node)
            rules = []
            if docstring and "Rules:" in docstring:
                rules = [line.strip("- ").strip() for line in docstring.splitlines() if line.startswith("-")]

            schema[node.name] = {"inputs": inputs}
            if rules:
                schema[node.name]["rules"] = rules
    return schema

# --- LLM Call ---
def call_llm(prompt):
    logging.info("Calling LLM...")
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False}
        )
        raw = response.json()["response"]
    except Exception as e:
        logging.error("LLM request failed: %s", e)
        return []

    cleaned = re.sub(r"```[\w]*|```", "", raw).strip()
    match = re.search(r"(\[.*\])", cleaned, re.DOTALL)
    if match:
        try:
            return ast.literal_eval(match.group(1))
        except:
            pass

    test_funcs = re.findall(
        r"(def\s+test_[\w_]+\s*\(.*?\):\s*(?:.*?\n)+?)(?=def\s+test_|class\s|\Z)",
        cleaned,
        re.DOTALL
    )
    return [func.strip() for func in test_funcs]

# --- Test Classification ---
def classify_test(description):
    desc = description.lower()
    if "multiple" in desc or "combined" in desc or "interaction" in desc:
        return "integration"
    elif "invalid" in desc or "negative" in desc or "edge" in desc:
        return "edge"
    return "unit"

# --- Test Case Parsing ---
def parse_test_case_string(code_str):
    lines = code_str.strip().split("\n")
    name, description, input_data, expected = "", "", "", ""
    for line in lines:
        if not name:
            match = re.match(r'def\s+([\w_]+)\s*\(', line)
            if match:
                name = match.group(1)
                description = f"Test function {name}"
        if not input_data:
            match = re.match(r'(\w+)\s*=\s*\{.*\}', line)
            if match:
                input_data = line.strip()
        match = re.search(r'assertEqual\((.+?),\s*(.+?)\)', line)
        if match:
            input_data = match.group(1).strip()
            expected = match.group(2).strip().strip("')\"")
    return {
        "function": name,
        "description": description or lines[0],
        "input": input_data,
        "expected": expected
    }

# --- HTML Renderer ---
def render_to_html(test_cases):
    html = "<html><head><style>table{border-collapse:collapse;}td,th{border:1px solid #ccc;padding:8px;}</style></head><body>"
    html += "<h2>🧪 AI-Generated Test Scenarios</h2><table><tr><th>Function</th><th>Input</th><th>Expected</th><th>Description</th><th>Type</th></tr>"
    for case in test_cases:
        html += f"<tr><td>{case['function']}</td><td>{json.dumps(case['input'])}</td><td>{case['expected']}</td><td>{case['description']}</td><td>{case['type']}</td></tr>"
    html += "</table></body></html>"
    return html

# --- PDF Export ---
def export_pdf(html, filename="test_report.pdf"):
    pdfkit.from_string(html, filename)

# --- Main Orchestration ---
def generate_tests_for_file(file_path):
    schema = extract_functions_from_file(file_path)
    prompt = f"Generate Python test cases for this schema:\n{schema}\nReturn a Python list of strings. Each string should contain a complete test function definition."
    raw_test_cases = call_llm(prompt)

    if not raw_test_cases:
        print("⚠️ No test cases generated. Check your LLM prompt or schema.")
        return

    code_blob = "\n".join(raw_test_cases) if isinstance(raw_test_cases, list) else str(raw_test_cases)
    test_func_blocks = re.findall(r'def\s+test_[\w_]+\s*\(.*?\):[\s\S]*?(?=def\s+test_|class\s|\Z)', code_blob)

    test_cases = []
    for block in test_func_blocks:
        parsed = parse_test_case_string(block)
        if parsed["function"]:
            parsed["type"] = classify_test(parsed["description"])
            test_cases.append(parsed)

    if not test_cases:
        print("⚠️ No valid test cases parsed from LLM output.")
        return

    html = render_to_html(test_cases)
    export_pdf(html)
    print("✅ Test report generated and exported to PDF.")

# --- Entry Point ---
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_code_file>")
    else:
        generate_tests_for_file(sys.argv[1])