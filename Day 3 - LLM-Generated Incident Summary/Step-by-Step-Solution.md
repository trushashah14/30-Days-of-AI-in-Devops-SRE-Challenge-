# Day 3: LLM-Generated Incident Summary - Step-by-Step Solution

## 1. Understanding the Task 🧠

### Why?
- Manual incident summary creation is time-consuming
- Consistency in format and tone is challenging across different team members
- Extracting key information from raw logs requires careful analysis
- Faster incident communication improves user trust

### How?
By using a Large Language Model (LLM) to:
- Process raw logs and alerts
- Identify patterns and key events
- Generate concise, professional summaries
- Maintain consistent structure and tone

## 2. Selecting the Right Tools 🛠️

### Why choose Ollama?
- Free and open-source LLM solution
- Runs locally without sending data to external services
- No API costs or usage limits
- Privacy-preserving for sensitive log data
- Available as a desktop application for easy use

### How?
- Downloaded the Ollama desktop application from ollama.ai
- Used the Llama 2 model for its balance of quality and performance
- Leveraged Ollama's API for programmatic interaction

## 3. Designing the Data Structure 📊

### Why?
- LLMs need structured input to generate meaningful summaries
- Consistent log format improves analysis quality
- Essential fields: timestamp, level, message

### How?
Created a simple JSON structure:
```json
[
  {
    "timestamp": "2023-10-15T08:12:34Z",
    "level": "WARN",
    "message": "High memory usage detected: 87%"
  }
]
```

## 4. Crafting the Prompt Engineering 📝

### Why?
- The quality of the LLM output depends heavily on the prompt
- Need to specify format, style, and content requirements
- Must extract key information from logs: timeline, impact, status

### How?
Designed a two-part prompt:
1. **System prompt**: Defines the role, guidelines, and output format
   - Specified clear sections: Title, Summary, Timeline, Affected Systems, Status
   - Set tone as professional and factual
   - Established word count limits for conciseness
   
2. **User prompt**: Contains the actual log data
   - Formatted logs for readability
   - Instructed the model to analyze and summarize

### What did I get?
A prompt that guides the LLM to produce consistently structured incident summaries with:
- Clear incident titles
- Concise impact descriptions
- Chronological timelines with key events
- Lists of affected systems
- Current status and next steps

## 5. Building the Python Script 🐍

### Why?
- Need a tool to process logs and interact with Ollama
- Should be easy to use from the command line
- Must handle various input/output scenarios

### How?
Created `incident_summarizer.py` with these components:
1. **Log Loading**: Reads JSON log data from files
2. **Ollama API Integration**: Communicates with the local Ollama service
3. **Prompt Construction**: Formats logs and creates effective prompts
4. **Summary Generation**: Processes LLM responses
5. **Output Handling**: Saves summaries to markdown files

Key implementation details:
```python
# Format logs for the prompt
log_text = "\n".join([f"[{log['timestamp']}] [{log['level']}] {log['message']}" for log in logs])

# Call Ollama API
response = requests.post('http://localhost:11434/api/generate',
                    json={
                        'model': model,
                        'prompt': user_prompt,
                        'system': system_prompt,
                        'stream': False
                    })
```

## 6. Testing with Sample Data 🧪

### Why?
- Need realistic test data to verify tool functionality
- Should cover common incident patterns
- Must include progression from detection to resolution

### How?
1. Created `example_logs.json` with a sample incident scenario
2. Included various log levels (INFO, WARN, ERROR)
3. Structured a narrative showing:
   - Initial warnings (high memory usage)
   - Escalation to errors (database connection failures)
   - Impact (payment processing disruption)
   - Resolution steps (failover to replica)
   - Recovery confirmation

### What did I get?
A realistic test dataset that demonstrates:
- How warnings can precede critical errors
- The progression of an incident over time
- Various affected components
- Resolution steps and verification

## 7. Running and Troubleshooting 🔍

### Why?
- Local LLM tools require proper setup and configuration
- Connection issues are common with local API services
- Need to verify that summaries meet quality standards

### How?
1. Installed the Ollama desktop application
2. Started the application and downloaded the Llama 2 model
3. Ran the script with sample data:
   ```
   python incident_summarizer.py --input example_logs.json
   ```
4. Troubleshot connection issues:
   - Verified Ollama was running
   - Checked API availability at http://localhost:11434
   - Added error handling for common failure modes
   - Improved debugging output

### What did I get?
A reliable tool that:
- Properly connects to Ollama's API
- Handles errors gracefully with helpful messages
- Successfully generates incident summaries from logs

## 8. Sample Output Analysis 📑

### Why?
- Need to evaluate summary quality
- Should verify that key information is captured
- Must ensure professional and clear communication

### How?
Generated a summary from example logs and analyzed:
- Structure and formatting
- Accuracy of timeline
- Clarity of impact description
- Appropriate tone

### What did I get?
A professional incident summary like:

```markdown
# Database Connectivity Incident Affecting Payment Processing

## Summary
On October 15, 2023, our payment processing system experienced an outage due to database connectivity issues. Starting at 08:12 UTC, we observed high memory usage on our API servers followed by database query timeouts, culminating in a complete connection failure to our primary database server. This resulted in payment transaction failures for customers. The incident was resolved at 08:30 UTC through failover to a replica database server and subsequent restoration of the primary server.

## Timeline
- **08:12 UTC**: Initial warning of high memory usage detected on api-server-03
- **08:15 UTC**: Database queries began exceeding response time thresholds
- **08:17 UTC**: Database connection timeout occurred, causing payment failures
- **08:18 UTC**: Initiated failover to database replica server
- **08:20 UTC**: Payment processing resumed with limited capacity
- **08:30 UTC**: Full service restored after primary server recovery

## Affected Systems
- Payment Processing API
- Database Services
- Customer Payment Interface

## Current Status
RESOLVED. All systems are now operating normally with payment processing at 100% capacity. We have identified the root cause as memory pressure on the database server and are implementing monitoring improvements to detect similar issues earlier.
```

## Results and Benefits

This solution provides:
1. Rapid creation of professional incident summaries
2. Consistent formatting and tone across all status updates
3. Time savings for operations teams during incidents
4. Better communication with users and stakeholders
5. Complete privacy and no ongoing costs
6. A balance between automation and human oversight

By leveraging local LLM technology for the initial draft while maintaining human review, we ensure both efficiency and accuracy in our incident communications.
