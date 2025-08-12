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

## Code & Implementation 💻
- [runbook_generator.py](./runbook_generator.py) - Main Python script for runbook generation
- [Step-by-Step-Solution.md](./Step-by-Step-Solution.md) - Detailed implementation process
- [environments/](./environments/) - Environment configuration files
- [prompt_templates/](./prompt_templates/) - Prompt templates for different failure modes


### Failure Mode Specific Files 🔧
- [environment_database_connection_leak.json](./environments/environment_database_connection_leak.json): Custom environment details for database connection leaks
- [environment_high_memory_usage_kubernetes.json](./environments/environment_high_memory_usage_kubernetes.json): Custom environment for Kubernetes memory issues
- [environment_disk_space_exhaustion.json](./environments/environment_disk_space_exhaustion.json): Custom environment for disk space problems
- [environment_api_gateway_5xx_errors.json](./environments/environment_api_gateway_5xx_errors.json): Custom environment for API gateway issues
- [environment_rabbitmq_queue_backlog.json](./environments/environment_rabbitmq_queue_backlog.json): Custom environment for message queue backlog
- [environment_load_balancer_health_check_failures.json](./environments/environment_load_balancer_health_check_failures.json): Custom environment for load balancer issues

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



## What Did I Learn 🧠
- **Prompt Engineering for Technical Documentation**: Crafting effective prompts for generating structured, technical runbooks requires understanding both LLM capabilities and domain-specific requirements
- **Template-Based Generation**: Creating reusable templates significantly improves consistency and quality across different runbooks
- **Environment-Specific Customization**: Tailoring content to specific technical environments yields more accurate and useful documentation
- **Human-in-the-Loop Refinement**: Combining AI generation with human expertise creates superior documentation compared to either approach alone
- **Model Selection Impact**: Different LLMs have varying strengths for technical writing tasks, with some excelling at technical accuracy while others at organization and clarity
- **Failure Mode Specificity**: Each system failure type requires unique diagnostic approaches, commands, and remediation steps that can be captured in specialized templates
- **Documentation Structure Matters**: Well-organized runbooks with clear sections for symptoms, diagnosis, remediation, and verification are more effective during incidents

## References 📖

### External Resources
- [Ollama GitHub Repository](https://github.com/ollama/ollama)
- [Ollama API Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md)
- [Site Reliability Engineering Book - Google](https://sre.google/sre-book/)
- [Runbook Best Practices - Microsoft](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/manage/hybrid/server/best-practices/runbook-maintenance)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

### Related Tools
- [Ollama](https://ollama.ai/) - Local LLM running tool
- [Markdown Guide](https://www.markdownguide.org/) - For runbook formatting
- [Mermaid Diagrams](https://mermaid.js.org/) - For diagram creation in runbooks

## Future Enhancements 🚀
- Expand the template library to cover additional failure scenarios
- Integrate the generated runbooks into an incident management system
- Create a feedback loop to improve prompts based on real incident usage
- Add support for diagram generation to enhance runbook clarity