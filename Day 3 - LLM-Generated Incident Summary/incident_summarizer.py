import os
import json
import argparse
import requests
import time

def load_logs(file_path):
    """Load log data from a JSON file"""
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_incident_summary(logs, model="llama2"):
    """Generate an incident summary using Ollama local API"""
    
    # Create a formatted log string for the prompt
    log_text = "\n".join([f"[{log['timestamp']}] [{log['level']}] {log['message']}" for log in logs])
    
    # Create an improved system prompt that produces more concise, business-focused summaries
    system_prompt = """You are an expert incident response analyst tasked with creating concise, 
    business-impact focused incident summaries for a public status page.

    Follow these EXACT guidelines:
    1. Give the incident a clear, descriptive title focused on the business impact (not just technical details)
    2. Provide a brief, 3-5 sentence summary that explains:
       - When the incident occurred (with UTC times)
       - What service was affected
       - Root cause at a high level (database connectivity, etc.)
       - Customer impact
       - How it was resolved
    3. Include a CONDENSED timeline with only 5-7 key events (not every single log entry)
       - Focus on initial detection, escalation points, mitigation steps, and resolution
       - Use UTC times in the format "08:12 UTC"
       - Format each timeline item as "- **[TIME]**: [Event description]"
    4. List affected systems using business-friendly names (e.g., "Payment Processing API" not "api-server-03")
    5. End with a clear current status that:
       - Starts with "RESOLVED" or "ONGOING" in all caps
       - States whether systems are fully functional
       - Mentions any ongoing monitoring or improvements
    
    Your summary should be professional, customer-focused, and approximately 250-350 words total.
    
    Structure your response as:
    # [Incident Title - focus on service impact]
    
    ## Summary
    [Brief description of the incident and impact]
    
    ## Timeline
    - **[Time]**: Incident began
    - **[Time]**: [Key event]
    [Only include 5-7 most important events]
    
    ## Affected Systems
    - [Business-friendly system name]
    - [Business-friendly system name]
    
    ## Current Status
    [Status starting with RESOLVED or ONGOING, then 1-2 sentences about current state]
    """
    
    # Create the user prompt with the logs
    user_prompt = f"Analyze these logs and generate an incident summary following my guidelines EXACTLY:\n\n{log_text}"
    
    # Call local Ollama API
    try:
        print("Sending request to Ollama API...")
        response = requests.post('http://localhost:11434/api/generate',
                            json={
                                'model': model,
                                'prompt': user_prompt,
                                'system': system_prompt,
                                'stream': False
                            })
        
        # Check if response is successful
        if response.status_code != 200:
            print(f"Error: Ollama API returned status code {response.status_code}")
            print(f"Response content: {response.text}")
            return None
        
        # Parse the response
        try:
            response_json = response.json()
            
            # Debug: Print the response structure
            print(f"Response keys: {list(response_json.keys())}")
            
            # Check if 'response' key exists
            if 'response' in response_json:
                return response_json['response']
            else:
                print(f"Error: Response doesn't contain 'response' key. Available keys: {list(response_json.keys())}")
                print(f"Full response: {response_json}")
                return None
                
        except ValueError as e:
            print(f"Error parsing JSON response: {e}")
            print(f"Raw response: {response.text[:500]}...")
            return None
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Ollama API at http://localhost:11434")
        print("Make sure Ollama is installed, running, and the API is accessible")
        print("If using the desktop app, ensure it's open and running")
        return None
    except Exception as e:
        print(f"Error calling Ollama API: {str(e)}")
        print("Make sure Ollama is installed and running (https://ollama.ai)")
        return None

def save_summary(summary, output_file):
    """Save the generated summary to a file"""
    with open(output_file, 'w') as file:
        file.write(summary)
    print(f"Summary saved to {output_file}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Generate incident summaries from logs using Ollama')
    parser.add_argument('--input', '-i', required=True, help='Path to JSON log file')
    parser.add_argument('--output', '-o', default='incident_summary.md', help='Output file for the summary (default: incident_summary.md)')
    parser.add_argument('--model', '-m', default='llama2', help='Ollama model to use (default: llama2)')
    args = parser.parse_args()
    
    # Process the logs
    print("Loading logs...")
    logs = load_logs(args.input)
    print(f"Loaded {len(logs)} log entries")
    
    # Generate summary
    print(f"Generating incident summary using Ollama with model {args.model}...")
    print("(Make sure Ollama is running on your machine)")
    summary = generate_incident_summary(logs, args.model)
    
    if summary:
        # Save summary
        save_summary(summary, args.output)
        
        # Print summary
        print("\nGenerated Summary:")
        print("-" * 40)
        print(summary)
        print("-" * 40)
        print(f"\nSummary saved to {args.output}")
        print("Review the summary, make any necessary edits, and then publish to your status page.")
    else:
        print("Failed to generate summary.")

if __name__ == "__main__":
    main()
