# Initial Prompt for API gateway 5xx errors

```
You are an experienced API architect and DevOps engineer with deep knowledge of api systems.

I need you to create a comprehensive runbook for diagnosing and resolving 5xx error responses from API Gateways in a production environment. These errors indicate server-side issues and often lead to degraded user experience and service unavailability.

Our environment consists of:
- API Gateway: Amazon API Gateway
- Backend Services: Lambda, ECS, EC2
- Authentication: JWT, OAuth2
- Rate Limiting: Enabled at 1000 req/min
- Caching: Enabled with 5 min TTL
- Logging: CloudWatch Logs
- Monitoring: CloudWatch Metrics, X-Ray
- CDN: CloudFront

The runbook should include:
1. Clear symptoms that indicate API Gateway 5xx errors (error patterns, client impact)
2. Diagnostic commands to identify the root cause (log analysis, metrics queries)
3. Step-by-step remediation procedures for different error types (502, 503, 504)
4. Verification steps to confirm resolution (API test requests, error rate metrics)
5. Preventative measures to avoid future occurrences (circuit breakers, rate limiting)

For each step, include specific AWS CLI commands, CloudWatch queries, and API Gateway configurations. Provide guidance on differentiating between various 5xx errors and their likely causes.

```
