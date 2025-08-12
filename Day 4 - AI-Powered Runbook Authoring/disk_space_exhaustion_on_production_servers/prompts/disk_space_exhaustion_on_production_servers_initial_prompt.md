# Initial Prompt for disk space exhaustion on production servers

```
You are an experienced Linux systems administrator and DevOps engineer with deep knowledge of database systems.

I need you to create a comprehensive runbook for diagnosing and resolving disk space exhaustion issues on production servers. Disk space exhaustion can lead to service outages, database crashes, and data corruption.

Our environment consists of:
- Generic production environment

The runbook should include:
1. Clear symptoms that indicate disk space issues (error messages, degraded performance)
2. Diagnostic commands to identify space consumption (df, du, lsof)
3. Step-by-step remediation procedures (log cleanup, volume expansion)
4. Verification steps to confirm resolution (disk usage metrics)
5. Preventative measures to avoid future occurrences (monitoring, log rotation, quotas)

For each step, include specific Linux commands, expected outputs, and potential pitfalls. Include emergency procedures for critical space shortages and guidance on AWS EBS volume management.

```
