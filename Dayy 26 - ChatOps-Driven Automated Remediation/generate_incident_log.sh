#!/bin/bash
# Save as generate_incident_log.sh

> incident.log  # Clear previous log

kubectl get pods --all-namespaces --no-headers | while read -r ns pod rest; do
  status=$(echo $rest | awk '{print $3}')
  app=$(kubectl get pod $pod -n $ns -o jsonpath='{.metadata.labels.app}' 2>/dev/null)
  if [[ "$status" != "Running" && "$status" != "Completed" ]]; then
    # Extract first error/warning/backoff event from pod description
    event=$(kubectl describe pod $pod -n $ns | grep -E 'Error|Failed|CrashLoopBackOff|ImagePullBackOff|ErrImagePull|BackOff|Unhealthy|Warning' | head -n 1)
    if [[ "$event" != "" ]]; then
      echo "Pod $pod in namespace $ns (app=$app) has error: $event" >> incident.log
    else
      echo "Pod $pod in namespace $ns (app=$app) is unhealthy (status: $status)" >> incident.log
    fi
  fi
done

# Node issues
kubectl get nodes --no-headers | while read -r node status rest; do
  if [[ "$status" != "Ready" ]]; then
    echo "Node $node is not ready (status: $status)." >> incident.log
    kubectl describe node $node | grep -E 'Warning|NotReady|MemoryPressure|DiskPressure|NetworkUnavailable' | while read -r event; do
      echo "Node event: $event" >> incident.log
    done
    echo "---" >> incident.log
  fi
done

# Deployment issues
kubectl get deployments --all-namespaces --no-headers | while read -r ns deploy rest; do
  unavailable=$(kubectl get deployment $deploy -n $ns -o jsonpath='{.status.unavailableReplicas}' 2>/dev/null)
  if [[ "$unavailable" != "" && "$unavailable" != "0" ]]; then
    echo "Deployment $deploy in namespace $ns has $unavailable unavailable replicas." >> incident.log
    echo "---" >> incident.log
  fi
done

# Service issues (example: check for endpoints)
kubectl get svc --all-namespaces --no-headers | while read -r ns svc rest; do
  endpoints=$(kubectl get endpoints $svc -n $ns -o jsonpath='{.subsets}' 2>/dev/null)
  if [[ "$endpoints" == "" ]]; then
    echo "Service $svc in namespace $ns has no endpoints." >> incident.log
    echo "---" >> incident.log
  fi
done