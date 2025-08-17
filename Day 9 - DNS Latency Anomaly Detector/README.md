# Day 9: DNS Latency Anomaly Detector 🚦 – Aug 16, 2025

## Challenge Description 🎯
Detect DNS latency spikes using an autoencoder and alert via Slack. Visualize and interpret results to uncover DNS performance issues and improve reliability.

## Objective 🚀
- Simulate or collect DNS latency time-series data
- Train an autoencoder to model normal DNS latency patterns
- Detect statistically significant latency anomalies
- Visualize latency trends and detected anomalies
- Send Slack alerts for new anomalies
- Interpret each graph to extract actionable insights

## Code & Implementation 💻
- **README**: [`Day 9 - DNS Latency Anomaly Detector/README.md`](README.md)  
  Project overview, workflow, graph choices, and real-world use cases.
- **Step-by-Step Solution**: [`Day 9 - DNS Latency Anomaly Detector/Step-by-Step-Solution.md`](Step-by-Step-Solution.md)  
  Detailed explanation of each notebook/code step, including rationale and insights.
- **Notebook**: [`Day 9 - DNS Latency Anomaly Detector/dns_latency_anomaly_detector.ipynb`](dns_latency_anomaly_detector.ipynb)  
  Main workflow for DNS latency simulation, anomaly detection, visualization, and Slack alerting.

## Slack Setup 🔔
- Store your Slack webhook URL in a `.env` file as `SLACK_WEBHOOK_URL`.
- The code loads this value using `python-dotenv` for secure alerting.

## Why Each Graph Was Chosen 📊

- **Time Series Line Plot (Latency & Rolling Mean):**  
  Shows DNS latency trends and highlights periods of abnormal latency. Rolling mean helps visualize sustained changes.

- **Histogram (Latency Distribution):**  
  Reveals the distribution of DNS latency values and identifies outliers.

- **Boxplot (Latency Spread):**  
  Summarizes central tendency, spread, and extreme values in DNS latency.

- **Violin Plot (Latency Density):**  
  Combines boxplot and density to show the shape of latency distribution.

- **Anomaly Visualization Plot:**  
  Clearly marks detected anomalies with large red markers and annotations for easy identification.


## What Did I Learn 🧩
- Autoencoder-based anomaly detection can effectively identify abnormal DNS latency events.
- Visualizing latency and anomalies makes it easy to spot and interpret performance issues.
- Slack integration enables real-time alerting for operational awareness.

## How to Use in Real-World DevOps/SRE 🌍

### DNS Latency Monitoring & Alerting
**Use Case:**  
Enable proactive DNS troubleshooting by automatically detecting latency spikes and notifying the network operations team.

**Implementation:**  
- Continuously collect DNS latency metrics from edge locations or cloud DNS logs.
- Use an autoencoder to learn normal latency patterns and flag anomalies.
- Visualize latency spikes and trends for rapid diagnosis.
- Integrate Slack alerts to notify on-call engineers of critical events.
- Use visualizations to correlate anomalies with upstream network changes or provider incidents.

**Advantage:**  
- Reduces mean time to resolution (MTTR) for DNS-related outages.
- Provides historical context for recurring latency issues.
- Automates escalation and incident response for DNS performance degradation.

**Industry Example:**  
A global e-commerce company uses DNS latency anomaly detection to monitor checkout page performance. When a spike is detected, Slack alerts trigger automated traffic rerouting to backup DNS providers, minimizing customer impact and lost sales.

---

### Graph Selection for Interpretation
**Use Case:**  
Empower SREs and network engineers to quickly diagnose and resolve DNS latency anomalies using targeted visual analytics.

**Implementation:**  
- Time series plots reveal latency patterns during peak business hours and maintenance windows.
- Histograms and violin plots help distinguish between transient spikes and persistent latency shifts.
- Boxplots highlight outlier events that may be linked to DDoS attacks or misconfigurations.
- Anomaly plots focus attention on actionable incidents, enabling faster root cause analysis.

**Advantage:**  
- Facilitates post-incident reviews and continuous improvement of DNS infrastructure.
- Supports capacity planning and provider selection based on real latency data.
- Enables data-driven decisions for DNS failover and redundancy strategies.

**Industry Example:**  
A media streaming platform uses DNS latency visualizations to optimize CDN routing. After visualizing anomalies, the team identifies a regional ISP issue and works with the provider to resolve it, improving streaming quality for millions of users.

## References 📖
- [Matplotlib Documentation](https://matplotlib.org/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Scikit-learn Autoencoder Example](https://scikit-learn.org/)
- [python-dotenv Documentation](https://pypi.org/project/python-dotenv/)
- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [DNS Monitoring Best Practices](https://www.cloudflare.com/learning/dns/dns-monitoring/)

## Future Enhancements 🚀
- Integrate with CI/CD pipelines for automated DNS latency monitoring
- Add support for real probe data collection
- Use advanced ML models for improved anomaly detection
- Automate reporting and alerting based on visualization insights

---
