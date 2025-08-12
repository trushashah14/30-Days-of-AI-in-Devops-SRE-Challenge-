# Runbook: Disk Space Exhaustion On Production Servers

**Generated:** 2025-08-11 18:44:30
**Model:** llama2
**Provider:** ollama

Runbook: Diagnosing and Resolving Disk Space Exhaustion Issues in Production Servers

1. Symptoms Indicating Disk Space Issues:
Disk space exhaustion can lead to a variety of issues, including service outages, database crashes, and data corruption. Some common symptoms to look out for include:
* Error messages related to disk space usage (e.g., "No space left on device")
* Degraded system performance (e.g., slow response times, sluggish behavior)
* Increased network latency or packet loss due to disk I/O contention
2. Diagnostic Commands:
To identify disk space consumption, perform the following diagnostic commands:
* `df -h`: Displays total disk usage, used space, and available space for each mounted file system. Expected output: A list of file systems with their respective usage metrics (e.g., 50G free, 200M used).
* `du -sh`: Calculates the disk usage for each directory and subdirectory in the file system hierarchy. Expected output: A list of directories with their corresponding usage metrics (e.g., /home/user/Documents: 10G used, 500M free).
* `lsof -ti`: Displays open files and their associated processes. Expected output: A list of processes and their respective file handles, along with information about the opened files (e.g., File name: /path/to/file.txt, Process ID: 1234).
3. Remediation Procedures:
To resolve disk space exhaustion issues, follow these step-by-step remediation procedures:
* Log Cleanup: Remove unnecessary logs and files to free up disk space. Use commands like `find /path/to/log/directory -type f -delete` or `rm -rf /path/to/unnecessary/files`. Expected output: A list of removed log files or unnecessary files.
* Volume Expansion: Increase the size of the running out of disk space by creating a new volume and migrating the affected data. Use commands like `sudo lvm create -n new_volume -L 100G` (where `new_volume` is the desired name for the new volume, and `100G` is the desired size increase). Expected output: A successful message indicating that a new volume has been created.
4. Verification Steps:
After remediation, perform these verification steps to confirm resolution:
* `df -h`: Check the updated disk usage metrics for each mounted file system. Expected output: A list of file systems with improved usage metrics (e.g., 50G free, 100M used).
* `du -sh`: Verify reduced disk usage for directories that were prone to exhaustion. Expected output: A list of directories with updated usage metrics (e.g., /home/user/Documents: 5G used, 400M free).
5. Preventative Measures:
To avoid future occurrences of disk space exhaustion, implement the following preventative measures:
* Monitoring: Set up monitoring tools to track disk usage and alert when thresholds are met (e.g., `threshold=90%, commodity=df -h /`). Expected output: A notification upon reaching a specified threshold (e.g., "Disk usage for /home/user/Documents exceeds 90%").
* Log Rotation: Automate log rotation to remove older logs and free up disk space. Use commands like `sudo logrotate -f -d /path/to/log/rotation/configuration`. Expected output: A successful message indicating that logs have been rotated.
* Quotas: Set up file system quotas to limit the amount of disk usage for individual users or groups. Use commands like `sudo quota -a -d /path/to/quota/configuration`. Expected output: A list of created quotas with their corresponding limits (e.g., User "user" has 10G of disk space available).
6. Emergency Procedures:
For critical space shortages, follow these emergency procedures:
* AWS EBS Volume Management: If your environment consists of AWS resources, use the `aws ec2 create-snapshot` command to create a snapshot of the affected volume, followed by `aws ec2 launch-instances --volume-id <Snapshot ID>` to launch new instances with the affected volume attached. Expected output: A list of newly launched instances with the affected volume attached.
* Spin Up Additional Volumes: If you have multiple volumes or file systems experiencing space issues, use the `sudo lvm extend` command to add additional disk space to existing volumes. Expected output: A successful message indicating that additional disk space has been added.
7. Additional Considerations:

* Avoid using the `rm -rf` command without proper confirmation, as it can permanently delete files and directories. Use the `-i` option to prompt for confirmation before deleting (e.g., `sudo rm -i -f /path/to/unnecessary/file`).
* Be cautious when working with sensitive data or critical systems. Verify file ownership and permissions before modifying any files or directories.
* Monitor system resource usage to identify potential disk space issues before they become critical. Use tools like `top`, `htop`, or `sysdig` to monitor resource usage in real-time.

By following this runbook, you can effectively diagnose and resolve disk space exhaustion issues in your production servers, ensuring optimal system performance and data integrity.