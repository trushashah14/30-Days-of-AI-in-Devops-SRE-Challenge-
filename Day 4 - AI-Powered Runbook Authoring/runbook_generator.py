#!/usr/bin/env python3
"""
Runbook Generator - AI-Powered Runbook Authoring Tool

This script uses LLMs to generate, refine, and save technical runbooks for common failure modes.
Supports Ollama as LLM provider.
"""

import argparse
import json
import os
import sys
import requests
import time
from datetime import datetime
import re

# Default prompt templates
INITIAL_PROMPT_TEMPLATE = """
You are an experienced DevOps engineer with deep knowledge of {system_type} systems. 
I need you to create a comprehensive runbook for diagnosing and resolving {failure_mode} in a production environment.

Our environment consists of:
{environment_details}

The runbook should include:
1. Clear symptoms that indicate the issue
2. Diagnostic commands to confirm the issue
3. Step-by-step remediation procedures
4. Verification steps to confirm resolution
5. Preventative measures to avoid future occurrences

For each step, include specific commands, expected outputs, and potential pitfalls.
"""

REFINEMENT_PROMPT_TEMPLATE = """
Your previous runbook on {failure_mode} was helpful, but we need more specific details for our environment.
Please enhance the runbook with:

{refinement_requests}

Also, add a troubleshooting decision tree to help engineers navigate different root causes of the issue.
"""

class RunbookGenerator:
    def __init__(self, args):
        self.args = args
        self.model = args.model
        self.provider = "ollama"  # Fixed to ollama only
        self.output_dir = args.output_dir
        self.failure_mode = args.failure_mode
        self.environment_file = args.environment_file
        self.runbook_content = ""
        self.input_runbook = args.input_runbook
        
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)
        
    def load_environment(self):
        """Load environment details from JSON file, checking for failure-mode specific file first"""
        # Try to load a failure-mode specific environment file first
        safe_name = self.failure_mode.lower().replace(' ', '_')
        
        # Check in the environments directory first
        specific_env_file = f"environments/environment_{safe_name}.json"
        
        # If not found, try the legacy location
        if not os.path.exists(specific_env_file):
            specific_env_file = f"environment_{safe_name}.json"
        
        if os.path.exists(specific_env_file):
            try:
                with open(specific_env_file, 'r') as f:
                    print(f"Using failure-mode specific environment: {specific_env_file}")
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Invalid JSON in environment file {specific_env_file}.")
        
        # Try default environment in environments directory
        default_env = "environments/environment.json"
        if os.path.exists(default_env):
            try:
                with open(default_env, 'r') as f:
                    print(f"Using default environment from environments directory: {default_env}")
                    return json.load(f)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error reading environment file {default_env}: {e}")
        
        # Fall back to the original default environment file
        try:
            with open(self.environment_file, 'r') as f:
                print(f"Using original default environment: {self.environment_file}")
                return json.load(f)
        except FileNotFoundError:
            print(f"Environment file {self.environment_file} not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Invalid JSON in environment file {self.environment_file}.")
            return {}
    
    def load_prompt_template(self, template_type="initial"):
        """Load a custom prompt template for the specific failure mode if available"""
        # Convert failure mode to safe filename format
        safe_name = self.failure_mode.lower().replace(' ', '_')
        
        # Get the base name without "on_production_servers" suffix
        base_name = safe_name
        if "on_production_servers" in base_name:
            base_name = base_name.replace("_on_production_servers", "")
        
        # Log what we're looking for
        print(f"Looking for {template_type} template for failure mode: '{self.failure_mode}'")
        print(f"  Using safe name: '{safe_name}'")
        print(f"  Using base name: '{base_name}'")
        
        # Potential template locations and naming patterns to try
        template_patterns = [
            # First try the exact filename matches
            f"prompt_templates/{safe_name}_{template_type}.txt",
            
            # Then try with the base name (without _on_production_servers)
            f"prompt_templates/{base_name}_{template_type}.txt",
            
            # Try full paths within directories
            f"{safe_name}/prompts/{safe_name}_{template_type}_prompt.md",
            f"{base_name}/prompts/{base_name}_{template_type}_prompt.md",
            
            # Try various directory and file patterns
            f"{safe_name}/initial_prompt.md",
            f"{base_name}/initial_prompt.md",
            f"prompt_templates/{template_type}_{safe_name}.txt",
            f"prompt_templates/{template_type}_{base_name}.txt"
        ]
        
        # Try each potential location
        for pattern in template_patterns:
            print(f"Checking for template at: {pattern}")
            if os.path.exists(pattern):
                try:
                    with open(pattern, 'r') as f:
                        content = f.read()
                        print(f"Found template at: {pattern}")
                        
                        # If it's a markdown file, extract content between triple backticks
                        if pattern.endswith('.md'):
                            match = re.search(r'```(.*?)```', content, re.DOTALL)
                            if match:
                                content = match.group(1).strip()
                                print("Extracted template content from markdown")
                        
                        return content
                except Exception as e:
                    print(f"Error reading template {pattern}: {e}")
        
        print(f"No custom template found for {self.failure_mode}, using default template")
        # Use default templates as fallback
        if template_type == "initial":
            return INITIAL_PROMPT_TEMPLATE
        else:
            return REFINEMENT_PROMPT_TEMPLATE
    
    def generate_initial_prompt(self):
        """Generate the initial prompt for runbook creation"""
        env = self.load_environment()
        system_type = env.get('system_type', 'database')
        
        # Format environment details as bullet points
        env_details = "\n".join([f"- {k}: {v}" for k, v in env.get('details', {}).items()])
        if not env_details:
            env_details = "- Generic production environment"
        
        # Get the template
        template = self.load_prompt_template("initial")
        print(f"Using template: {template[:100]}...")  # Log first 100 chars of template
        
        # Format the template with our variables
        formatted_prompt = template.format(
            system_type=system_type,
            failure_mode=self.failure_mode,
            environment_details=env_details
        )
        
        return formatted_prompt
    
    def generate_refinement_prompt(self, refinement_requests):
        """Generate a prompt for refining the runbook"""
        template = self.load_prompt_template("refinement")
        
        return template.format(
            failure_mode=self.failure_mode,
            refinement_requests="\n".join([f"{i+1}. {r}" for i, r in enumerate(refinement_requests)])
        )
    
    def call_ollama(self, prompt):
        """Call Ollama API to generate content"""
        try:
            headers = {"Content-Type": "application/json"}
            data = {
                "model": self.model,
                "prompt": prompt,
                "system": "You are an expert DevOps engineer creating detailed technical runbooks.",
                "stream": False
            }
            
            response = requests.post("http://localhost:11434/api/generate", 
                                    headers=headers, 
                                    json=data)
            
            if response.status_code == 200:
                return response.json().get('response', '')
            else:
                print(f"Error from Ollama API: {response.text}")
                sys.exit(1)
                
        except requests.exceptions.ConnectionError:
            print("Failed to connect to Ollama API. Is Ollama running at http://localhost:11434?")
            sys.exit(1)
        except Exception as e:
            print(f"Error calling Ollama API: {e}")
            sys.exit(1)
    
    def generate_content(self, prompt):
        """Generate content using Ollama"""
        print(f"Generating content using Ollama...")
        start_time = time.time()
        
        content = self.call_ollama(prompt)
        
        elapsed_time = time.time() - start_time
        print(f"Content generated in {elapsed_time:.2f} seconds.")
        
        return content
    
    def save_runbook(self, content, filename=None):
        """Save the runbook content to a markdown file"""
        if filename is None:
            # Generate filename based on failure mode
            safe_name = self.failure_mode.lower().replace(' ', '_')
            filename = f"{safe_name}_runbook.md"
        
        output_path = os.path.join(self.output_dir, filename)
        
        with open(output_path, 'w') as f:
            # Add metadata header
            f.write(f"# Runbook: {self.failure_mode.title()}\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Model:** {self.model}\n")
            f.write(f"**Provider:** {self.provider}\n\n")
            f.write(content)
        
        print(f"Runbook saved to {output_path}")
        return output_path
    
    def save_prompt(self, prompt, stage="initial"):
        """Save the prompt used for documentation"""
        prompt_dir = os.path.join(self.output_dir, "prompts")
        os.makedirs(prompt_dir, exist_ok=True)
        
        safe_name = self.failure_mode.lower().replace(' ', '_')
        filename = f"{safe_name}_{stage}_prompt.md"
        output_path = os.path.join(prompt_dir, filename)
        
        with open(output_path, 'w') as f:
            f.write(f"# {stage.title()} Prompt for {self.failure_mode}\n\n")
            f.write("```\n")
            f.write(prompt)
            f.write("\n```\n")
        
        print(f"Prompt saved to {output_path}")
    
    def run_initial_generation(self):
        """Run the initial runbook generation"""
        prompt = self.generate_initial_prompt()
        self.save_prompt(prompt, "initial")
        
        content = self.generate_content(prompt)
        self.runbook_content = content
        
        return self.save_runbook(content, "initial_runbook.md")
    
    def run_refinement(self, refinement_requests):
        """Run refinement on the existing runbook"""
        if not self.runbook_content:
            print("No runbook content to refine. Run initial generation first.")
            return
        
        prompt = self.generate_refinement_prompt(refinement_requests)
        prompt += "\n\nCurrent runbook content:\n\n" + self.runbook_content
        self.save_prompt(prompt, "refinement")
        
        content = self.generate_content(prompt)
        self.runbook_content = content
        
        return self.save_runbook(content)
    
    def load_runbook_from_file(self, filepath):
        """Load runbook content from an existing file"""
        try:
            with open(filepath, 'r') as f:
                content = f.read()
                
            # Extract actual runbook content (skip metadata header)
            match = re.search(r'\*\*Provider:\*\*.*?\n\n(.*)', content, re.DOTALL)
            if match:
                self.runbook_content = match.group(1)
            else:
                self.runbook_content = content
            
            # Try to extract failure mode from title if not provided
            if not self.failure_mode or self.failure_mode == "unknown":
                title_match = re.search(r'# Runbook: (.*?)\n', content)
                if title_match:
                    self.failure_mode = title_match.group(1).lower()
                    print(f"Extracted failure mode from runbook: {self.failure_mode}")
            
            print(f"Loaded runbook from {filepath}")
            return True  # Success
            
        except FileNotFoundError:
            print(f"Error: Runbook file {filepath} not found.")
            return False  # Failure
        except Exception as e:
            print(f"Error loading runbook file {filepath}: {e}")
            return False  # Failure
    
    def interactive_refinement(self):
        """Run an interactive refinement session"""
        print("\nEntering interactive refinement mode.")
        print("Enter refinement requests one per line. Enter an empty line when done.")
        
        refinement_requests = []
        while True:
            request = input("> ")
            if not request:
                break
            refinement_requests.append(request)
        
        if refinement_requests:
            return self.run_refinement(refinement_requests)
        else:
            print("No refinement requests provided.")
            return None

def main():
    parser = argparse.ArgumentParser(description="AI-Powered Runbook Generator")
    parser.add_argument("--failure-mode", required=False, default="unknown", 
                        help="The failure mode to create a runbook for (e.g., 'database connection leak')")
    parser.add_argument("--model", default="llama2", help="Ollama model to use (e.g., 'llama2')")
    parser.add_argument("--environment-file", default="environments/environment.json", 
                        help="JSON file with environment details")
    parser.add_argument("--output-dir", default=".", help="Directory to save generated runbooks")
    parser.add_argument("--interactive", action="store_true", help="Enable interactive refinement mode")
    parser.add_argument("--input-runbook", help="Path to existing runbook file to refine (skips initial generation)")
    
    args = parser.parse_args()
    
    generator = RunbookGenerator(args)
    
    # Check if we're refining an existing runbook or generating a new one
    if args.input_runbook:
        if not generator.load_runbook_from_file(args.input_runbook):
            print("Failed to load the runbook file.")
            sys.exit(1)
        
        # If failure mode wasn't extracted from the runbook, require it
        if generator.failure_mode == "unknown":
            print("Error: Could not determine failure mode from runbook. Please provide it with --failure-mode.")
            sys.exit(1)
            
        # Always enter interactive mode when refining existing runbook
        generator.interactive_refinement()
    else:
        # Require failure mode for new runbook generation
        if args.failure_mode == "unknown":
            print("Error: --failure-mode is required when generating a new runbook.")
            sys.exit(1)
            
        # Generate initial runbook
        initial_runbook_path = generator.run_initial_generation()
        
        # Optionally enter interactive refinement mode
        if args.interactive:
            generator.interactive_refinement()
    
    print("\nRunbook generation complete!")
    
if __name__ == "__main__":
    main()
        