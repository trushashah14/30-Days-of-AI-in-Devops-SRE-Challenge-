# Database Connection Leak Runbook

**Last Updated:** 2023-10-18  
**Version:** 1.2  
**Environment:** PostgreSQL 13, Spring Boot, Kubernetes, HikariCP  
**Tags:** #database #connection-leak #postgresql #hikaricp #troubleshooting

## Table of Contents
- [Symptoms](#symptoms)
- [Detection](#detection)
- [Investigation](#investigation)
- [Remediation](#remediation)
- [Verification](#verification)
- [Prevention](#prevention)
- [Troubleshooting Decision Tree](#troubleshooting-decision-tree)

## Symptoms

Database connection leaks typically manifest as:

- Increasing latency in API responses
- Growing number of connection errors
- Application failure with "Too many connections" errors
- Degraded performance over time without traffic increase
- Database CPU usage disconnected from query volume
- Increasing memory usage on application pods

## Detection

### Prometheus Alert Queries

```
# Alert when connection count approaches the configured maximum
sum(hikaricp_connections_active) / sum(hikaricp_connections_max) > 0.8

# Alert on growing connection count without corresponding traffic increase
rate(hikaricp_connections_active[5m]) > 0.1 and rate(http_requests_total[5m]) < 0.05
```

### Dashboard Monitoring

Check Grafana dashboard "Database Connection Pool Status" for:
- Connection usage trend over time
- Connection acquisition time increasing
- Wait queue growing

### Direct Connection Count Verification

Connect to PostgreSQL and check current connections:

```sql
SELECT count(*) FROM pg_stat_activity;
```

Compare to maximum allowed connections:

```sql
SHOW max_connections;
```

## Investigation

### 1. Identify connection sources

Run on the PostgreSQL server:

```sql
SELECT 
    application_name,
    count(*) as connection_count,
    string_agg(distinct state, ', ') as states
FROM 
    pg_stat_activity 
WHERE 
    datname = 'your_database'
GROUP BY 
    application_name
ORDER BY 
    connection_count DESC;
```

### 2. Check connection states and age

```sql
SELECT 
    state, 
    count(*),
    max(now() - state_change) as max_duration,
    avg(now() - state_change) as avg_duration
FROM 
    pg_stat_activity
WHERE 
    datname = 'your_database'
GROUP BY 
    state;
```

### 3. Examine HikariCP metrics from application

Check pod logs for connection pool statistics:

```bash
kubectl logs -l app=your-application | grep HikariPool
```

Expected output pattern:
```
HikariPool-1 - Pool stats (total=20, active=18, idle=2, waiting=0)
```

### 4. Review application logs for connection handling

```bash
kubectl logs -l app=your-application | grep -E "Connection|DataSource" | tail -100
```

Look for patterns of connections being created but not closed.

## Remediation

### Option 1: Application Restart (Fastest, but temporary)

If immediate service restoration is required:

```bash
# Rolling restart of pods
kubectl rollout restart deployment/your-application-deployment

# Verify new pods are created before old ones terminate
kubectl get pods -l app=your-application -w
```

### Option 2: Terminate Idle Connections

Identify and terminate long-running idle connections:

```sql
SELECT pg_terminate_backend(pid) 
FROM pg_stat_activity
WHERE 
    datname = 'your_database' AND
    state = 'idle' AND
    now() - state_change > '30 minutes'::interval;
```

### Option 3: Fix Connection Leaks in Code

1. Review recent code changes that might affect connection handling
2. Check for missing `close()` statements in try-finally blocks
3. Verify correct usage of connection pool in application code:

```java
// Correct pattern
try (Connection conn = dataSource.getConnection()) {
    // use connection
} // auto-close
```

### Option 4: Adjust HikariCP Configuration

Update the application's connection pool settings:

```yaml
spring:
  datasource:
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      idle-timeout: 300000  # 5 minutes
      max-lifetime: 1800000  # 30 minutes
      connection-timeout: 30000  # 30 seconds
      leak-detection-threshold: 60000  # 1 minute
```

Apply configuration and restart affected services:

```bash
kubectl apply -f updated-config.yaml
kubectl rollout restart deployment/your-application-deployment
```

## Verification

### 1. Check connection count trend

```sql
SELECT count(*) FROM pg_stat_activity WHERE datname = 'your_database';
```

Run this query several times over 5-10 minutes to confirm connections are not increasing.

### 2. Verify connection pool metrics

```bash
kubectl exec -it $(kubectl get pod -l app=your-application -o jsonpath='{.items[0].metadata.name}') -- \
  curl -s localhost:8080/actuator/metrics/hikaricp.connections.active | jq
```

### 3. Confirm service health

```bash
# Check endpoint response times
curl -w "\nTime: %{time_total}s\n" https://your-service-endpoint/health

# Monitor for error rates
kubectl logs -l app=your-application --since=5m | grep ERROR | wc -l
```

## Prevention

### Connection Pool Configuration Best Practices

1. Set appropriate pool sizes:
   ```yaml
   maximum-pool-size: <2 * CPU cores>
   ```

2. Enable leak detection:
   ```yaml
   leak-detection-threshold: 60000  # 1 minute
   ```

3. Configure connection validation:
   ```yaml
   connection-test-query: "SELECT 1"
   validation-timeout: 5000  # 5 seconds
   ```

### Monitoring Setup

1. Add Prometheus metrics for connection pool:
   ```yaml
   management:
     metrics:
       export:
         prometheus:
           enabled: true
     endpoints:
       web:
         exposure:
           include: prometheus,health,info
   ```

2. Create alerts for:
   - Connection count approaching maximum
   - Connection acquisition time spikes
   - Connection usage growing without traffic increase

### Code Review Practices

1. Require code review focusing on resource cleanup
2. Add static code analysis for connection leak patterns
3. Implement integration tests that verify connection counts before/after operations

## Troubleshooting Decision Tree

```
Is the application experiencing "Too many connections" errors?
├── YES → Check current connection count
│   ├── Near max_connections → Immediate action needed
│   │   ├── Production critical system → Option 1: Restart application
│   │   └── Can tolerate investigation → Option 2: Terminate idle connections
│   └── Below 80% of max_connections → Different issue, check other database metrics
└── NO → Is connection count steadily increasing?
    ├── YES → Is it correlated with traffic?
    │   ├── YES → Scale up database or adjust pool configuration
    │   └── NO → Likely connection leak
    │       ├── Recent code deployment → Rollback and fix leak
    │       └── No recent changes → Option 3: Investigate application code
    └── NO → Monitor for other database performance issues
```

---

**Note:** Always test changes in lower environments before applying to production. Document any deviations from this runbook during actual incident response.
