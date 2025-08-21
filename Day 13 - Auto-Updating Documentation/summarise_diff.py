import requests

OLLAMA_HOST = "http://localhost:11434"
MODEL_NAME = "llama2"  # Or any model you've pulled via Ollama CLI

def generate_summary(diff_text, max_retries=3):
    if not diff_text.strip():
        return "No changes detected."

    prompt = f"""
You are a DevOps assistant. Summarize the following infrastructure diff in plain English for a changelog.
Use concise bullet points. Avoid unnecessary jargon. Highlight meaningful changes.

Diff:
{diff_text}
"""

    for attempt in range(max_retries):
        try:
            response = requests.post(
                f"{OLLAMA_HOST}/api/generate",
                json={
                    "model": MODEL_NAME,
                    "prompt": prompt,
                    "stream": False
                }
            )
            response.raise_for_status()
            return response.json()["response"].strip()
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")

    return "⚠️ Failed to generate summary after multiple attempts."