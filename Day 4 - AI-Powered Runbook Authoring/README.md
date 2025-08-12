# Day 4: AI-Powered Runbook Authoring 📚 - Aug 11, 2025

## Challenge Description 🎯
This challenge focuses on using AI to create effective runbooks for common system failures:

* Take multiple known failure modes (DB connection leak plus 5 additional scenarios)
* Ask an LLM to propose step-by-step remediation for each scenario
* Validate steps, refine prompts, and save comprehensive runbooks

## Objective 🚀
Create comprehensive, validated runbooks for multiple common failure modes by leveraging LLM capabilities while ensuring technical accuracy. The failure modes addressed include:

1. Database connection leaks in PostgreSQL environments
2. High memory usage on Kubernetes nodes 
3. Disk space exhaustion on production servers
4. API gateway 5xx errors
5. RabbitMQ message queue backlog

Each runbook provides detailed detection, remediation, and verification steps specific to the failure scenario.

## Files in this Directory 📁
- `Step-by-Step-Solution.md`: Detailed walkthrough of the process
- `runbook_generator.py`: Python script to automate runbook generation with Ollama
- `environment.json`: Default environment configuration for runbook generation
- `prompt_examples.md`: Example prompts used with the LLM

### Failure Mode Specific Files 🔧
- `environment_database_connection_leak.json`: Custom environment details for database connection leaks
- `environment_high_memory_usage_kubernetes.json`: Custom environment for Kubernetes memory issues
- `environment_disk_space_exhaustion.json`: Custom environment for disk space problems
- `environment_api_gateway_5xx_errors.json`: Custom environment for API gateway issues
- `environment_rabbitmq_queue_backlog.json`: Custom environment for message queue backlog
- `environment_load_balancer_health_check_failures.json`: Custom environment for load balancer issues

### Custom Prompt Templates 💬
- `prompt_templates/`: Directory containing specialized prompts for each failure mode
  - Initial prompts (`*_initial.txt`): Used for generating the first version of a runbook
  - Refinement prompts (`*_refinement.txt`): Used for improving existing runbooks

### Generated Runbooks 📋
Each failure mode has its own dedicated directory with the following structure:
- `<failure_mode>/initial_runbook.md`: The generated runbook for each failure mode
- `<failure_mode>/prompts/`: Folder containing refinement prompts used for that specific failure mode

For example:
- `database_connection_leak/initial_runbook.md`
- `high_memory_usage_kubernetes/initial_runbook.md`
- `disk_space_exhaustion/initial_runbook.md`
- `api_gateway_5xx_errors/initial_runbook.md`
- `rabbitmq_queue_backlog/initial_runbook.md`
- `load_balancer_health_check_failures/initial_runbook.md`

## Example Failure Modes 🔍

The script can generate runbooks for various common failure modes, not just database connection leaks. Here are some additional examples:

### 1. High CPU/Memory Usage 🧠

```bash
python runbook_generator.py --failure-mode "high memory usage on Kubernetes nodes" --interactive
```

This will create a runbook covering:
- Memory usage monitoring techniques
- Pod memory limit configuration
- Memory leak investigation
- OOMKilled event remediation
- Horizontal/vertical scaling options

### 2. Disk Space Exhaustion 💾

```bash
python runbook_generator.py --failure-mode "disk space exhaustion on production servers"
```

This will generate a runbook addressing:
- Disk usage monitoring
- Log rotation and cleanup
- Identifying large files and directories
- Emergency space reclamation
- Disk expansion procedures

### 3. API Gateway Failures 🌐

```bash
python runbook_generator.py --failure-mode "API gateway 5xx errors"
```

This creates procedures for:
- API gateway traffic investigation
- Backend service health validation
- Rate limiting configuration
- Circuit breaker implementation
- Fallback strategies

### 4. Message Queue Backlog 📨

```bash
python runbook_generator.py --failure-mode "RabbitMQ message queue backlog"
```

This produces a runbook with:
- Queue monitoring procedures
- Consumer scaling options
- Message TTL configuration
- Dead letter queue management
- Queue purging safeguards

### 5. Load Balancer Failure ⚖️

```bash
python runbook_generator.py --failure-mode "load balancer health check failures"
```

This creates instructions for:
- Health check configuration validation
- Backend service investigation
- Connection draining procedures
- Failover mechanisms
- DNS failover implementation

## Post-Generation Workflow 🔄

After generating the initial runbook (`initial_runbook.md`), follow these steps:

1. **Review the initial runbook**:
   - Examine the generated content for technical accuracy
   - Identify any missing information or incorrect assumptions
   - Note areas that need improvement or more specific details

2. **Refine the runbook** using one of these methods:
   - **Interactive mode**: Re-run the script with the `--interactive` flag to iteratively improve the content:
     ```bash
     python runbook_generator.py --failure-mode "database connection leak" --interactive
     ```
   - **Manual editing**: Make direct edits to the markdown file
   - **Refined prompt**: Create a new prompt in `prompt_examples.md` that addresses specific improvements

3. **Validate the runbook**:
   - Set up a test environment that simulates the failure condition
   - Follow the runbook procedures exactly as written
   - Document any unclear or incorrect steps
   - Have a team member unfamiliar with the issue try to follow the runbook

4. **Finalize and publish**:
   - Remove any inaccurate or environment-specific information
   - Ensure all commands and procedures are properly formatted
   - Add relevant screenshots or diagrams if helpful
   - Move the final version to your team's knowledge base or documentation system

5. **Iterate and improve**:
   - Schedule regular reviews of the runbook
   - Update after each incident where the runbook is used
   - Add any discovered edge cases or alternative solutions

## Results and Benefits ✅
- Faster runbook creation (reduced from days to hours)
- Standardized format and instructions across different failure modes
- Comprehensive coverage of detection, investigation, and remediation steps
- Knowledge democratization through shareable templates and processes
- Enhanced technical accuracy through specialized prompts and environments
- Consistent verification steps that are often overlooked in manual creation

## Next Steps 🔮
- Expand the template library to cover additional failure scenarios
- Integrate the generated runbooks into an incident management system
- Create a feedback loop to improve prompts based on real incident usage
- Add support for diagram generation to enhance runbook clarity

