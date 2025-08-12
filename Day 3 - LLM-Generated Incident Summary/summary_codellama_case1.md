
# High Memory Usage and Database Connectivity Issues

## Summary

On October 15th, 2023 at approximately 8:12 UTC, a high memory usage alert was triggered on the api-server-03 server. The alert was followed by several other alerts related to database connectivity issues and failed payments. These events resulted in a service disruption for our customers, with some being unable to complete transactions due to connection timeout errors. Fortunately, we were able to quickly resolve the issue by failing over to a database replica and re-establishing connections to the primary server. All systems are now operating normally, and payment processing is at 100% capacity.

## Timeline

- **08:12 UTC**: High memory usage alert triggered on api-server-03
- **08:15 UTC**: Database query took 4582ms, exceeding threshold on query GET_USER_TRANSACTIONS
- **08:17 UTC**: Connection timeout after 30000ms to database primary server
- **08:17 UTC**: Failed to process payment transaction: Database connection failure
- **08:17 UTC**: API request failed: POST /api/v1/payments returned 500 Internal Server Error
- **08:17 UTC**: Multiple failed customer payment attempts reported by frontend services
- **08:18 UTC**: Failover initiated: Switching to database replica
- **08:19 UTC**: Database connection established to replica server
- **08:20 UTC**: Payment processing resumed with limited capacity
- **08:25 UTC**: Database primary server responding again after restart
- **08:27 UTC**: Reverting to database primary server
- **08:30 UTC**: All systems operating normally, payment processing at 100% capacity

## Affected Systems

- Payment Processing API

## Current Status
RESOLVED - All systems operating normally, payment processing at 100% capacity.