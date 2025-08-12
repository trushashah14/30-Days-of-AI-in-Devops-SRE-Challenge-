 [Incorrect Summary]

## SUMMARY
A high memory usage was detected on the API Server. The root cause is unknown. However, this incident has impacted the Database Server by causing it to timeout after a long period of time and return an internal server error. This led to multiple failed customer payment attempts being reported. A failover operation was initiated to switch to a database replica, which successfully established a connection with the replacement server. The issue was resolved when the primary server was restarted, and all systems were operating normally by the end of the day.

## TIMELINE
- [2021-10-17T08:12:34Z] 
  - API Server received a warning due to high memory usage.
- [2021-10-17T08:15:45Z] 
  - Database Query took 4582ms, exceeding the threshold for query GET_USER_TRANSACTIONS.
- [2021-10-17T08:17:22Z] 
  - Connection timeout occurred after 30000ms to the primary server.
- [2021-10-17T08:17:25Z] 
  - Failed to process a payment transaction due to a database connection failure.
- [2021-10-17T08:17:28Z] 
  - Posting an API request for /api/v1/payments returned 500 Internal Server Error.
- [2021-10-17T08:18:05Z] 
  - Multiple failed customer payment attempts reported by frontend services.
- [2021-10-17T08:19:45Z] 
  - Failover initiated to switch to a database replica due to the connection issues with the primary server.
- [2021-10-17T08:20:12Z] 
  - A successful connection was established with the replacement server, allowing payment processing to resume.
- [2021-10-17T08:25:30Z] 
  - The Database Server's primary server started responding again after being restarted.
- [2021-10-17T08:27:45Z] 
  - The database connection was reverted back to the original primary server.
[2021-10-17T08:30:00Z] 
  - All systems were operating normally, and 100% of payment processing capacity was restored.
