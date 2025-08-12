# Runbook: High Memory Usage On Kubernetes Nodes

**Generated:** 2025-08-11 20:03:28
**Model:** llama2
**Provider:** ollama

Runbook for Diagnosing and Resolving High Memory Usage Issues on Kubernetes Nodes in a Production Environment

Introduction:
High memory usage on Kubernetes nodes can lead to pod evictions, service disruptions, and performance issues. This runbook outlines the steps to diagnose and resolve high memory usage issues in a production environment. The runbook is tailored for experienced Kubernetes administrators and DevOps engineers with deep knowledge of database systems.

Step 1: Symptoms Indicating High Memory Usage
---------------------------------------------

Symptoms that indicate high memory usage on Kubernetes nodes include:

* Pods being evicted due to memory constraints
* Node's memory utilization exceeding the available capacity
* OOMKilled events in pod logs
* Increased container overhead due to excessive memory usage

Step 2: Diagnostic Commands and Metrics
---------------------------------------

Use the following diagnostic commands and metrics to identify problematic pods and processes:

### kubectl Commands:

1. List all running pods on the node: `kubectl get pods -n <namespace>`
2. Check the CPU and memory usage of each pod: `kubectl describe pod <pod-name>`
3. Get the list of processes running on the node: `kubectl get nodes -o jsonpath='{.items[0].status.containerStatuses}'`

### Metrics Queries:

1. Node's memory utilization: `kubectl get node <node-name> -o jsonpath='{.status.memory.available}'`
2. Pods' memory usage: `kubectl get pod <pod-name> -o jsonpath='{.spec.containers[0].memoryLimit}'`
3. Node's CPU utilization: `kubectl get node <node-name> -o jsonpath='{.status.cpu.utilization}'`

Step 3: Remediation Procedures
------------------------------

Remediate high memory usage by following these steps:

### Pod Rescheduling:

1. Check if the pods are running on the node with high memory usage: `kubectl get pods -n <namespace> -o jsonpath='{.items[].status.host'`
2. Reschedule problematic pods to other nodes: `kubectl rollout undo <deployment-name>`
3. Monitor the rescheduling process using the `kubectl get` command: `kubectl get pods -n <namespace> -o jsonpath='{.items[].status.host'`

### Node Draining:

1. Check if the node has a high memory usage: `kubectl get nodes -o jsonpath='{.items[0].status.memory.available}'`
2. Drain the node of pods: `kubectl drain <node-name>`
3. Monitor the draining process using the `kubectl get` command: `kubectl get nodes -o jsonpath='{.items[].status.containerStatuses.State}`

### Pod Scaling:

1. Check if the pods are running on the node with high memory usage: `kubectl get pods -n <namespace> -o jsonpath='{.items[].status.host'`
2. Scale down problematic pods by adjusting their `memoryLimit` value: `kubectl patch pod <pod-name> -n <namespace> -p '{"metadata":{"labels":{},"resourceVersion":0}}' -l ' scale=down'`
3. Monitor the scaling process using the `kubectl get` command: `kubectl get pods -n <namespace> -o jsonpath='{.items[].status.host'`

Step 4: Verification Steps
-------------------------

Verify that the high memory usage issue has been resolved by checking the following metrics:

### Node Memory Utilization:

1. Check the node's memory utilization after remediation: `kubectl get node <node-name> -o jsonpath='{.status.memory.available}'`
2. Verify that the memory usage is within the acceptable range: `kubectl get nodes -o jsonpath='{.items[0].status.memory.available}')`

### Pod Memory Usage:

1. Check the pods' memory usage after remediation: `kubectl get pod <pod-name> -o jsonpath='{.spec.containers[0].memoryLimit}'`
2. Verify that the pods' memory usage is within the acceptable range: `kubectl get pods -n <namespace> -o jsonpath='{.items[].status.memoryUsage}')`

Step 5: Preventative Measures
-----------------------------

Prevent future high memory usage issues by implementing the following preventative measures:

### Resource Limits:

1. Set resource limits for pods to avoid excessive memory usage: `kubectl create clusterrolebinding <binding-name> --clusterrole=<clusterrole-name> --resource=memory`
2. Apply the binding to the problematic pods: `kubectl patch pod <pod-name> -n <namespace> -p '{"metadata":{"labels":{},"resourceVersion":0}}' -l 'binding=<binding-name>'}`

### Monitoring:

1. Set up monitoring tools to detect high memory usage issues early on: `kubectl create clustermonitor <monitor-name> --clusterrole=<clusterrole-name> --resource=memory`
2. Configure alerts for high memory usage: `kubectl get clustermonitor <monitor-name> -o jsonpath='{.items[0].status.alerters[] | .metadata.name'`

Conclusion:
High memory usage on Kubernetes nodes can lead to pod evictions, service disruptions, and performance issues. This runbook provides a comprehensive approach to diagnosing and resolving high memory usage issues in a production environment. By following the steps outlined in this runbook, experienced Kubernetes administrators and DevOps engineers can quickly identify and resolve memory-related issues, ensuring optimal system performance.