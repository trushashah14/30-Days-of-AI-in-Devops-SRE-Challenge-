import re
from typing import List, Dict

def check_service_health(response_time: float, error_rate: float) -> str:
    """
    Rules:
    - If response_time > 500ms or error_rate > 0.05, service is unhealthy
    - If both are within limits, service is healthy
    - Negative values are invalid and should raise an alert
    """
    if response_time < 0 or error_rate < 0:
        return "alert: invalid metrics"
    if response_time > 500 or error_rate > 0.05:
        return "unhealthy"
    return "healthy"

def parse_logs(log_lines: List[str]) -> Dict[str, int]:
    """
    Rules:
    - Count number of ERROR, WARN, and INFO entries
    - Ignore empty lines or malformed entries
    - Case-insensitive matching
    """
    counts = {"ERROR": 0, "WARN": 0, "INFO": 0}
    for line in log_lines:
        if not line.strip():
            continue
        match = re.search(r"(ERROR|WARN|INFO)", line, re.IGNORECASE)
        if match:
            level = match.group(1).upper()
            counts[level] += 1
    return counts

def deployment_summary(response_time: float, error_rate: float, logs: List[str]) -> Dict[str, str]:
    """
    Rules:
    - Combines health check and log parsing
    - Returns overall status and log breakdown
    - If logs contain more than 5 ERRORs, override status to 'critical'
    """
    status = check_service_health(response_time, error_rate)
    log_summary = parse_logs(logs)
    if log_summary["ERROR"] > 5:
        status = "critical"
    return {
        "status": status,
        "logs": f"{log_summary['ERROR']} errors, {log_summary['WARN']} warnings, {log_summary['INFO']} info"
    }