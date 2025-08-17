# Day 9: DNS Latency Anomaly Detector – Step-by-Step Solution 🚦

This document explains how to build a DNS latency anomaly detector using an autoencoder and send alerts to Slack when latency spikes are detected.

---

## Step 1: Introduction & Planning 📝
**Why:**  
Detecting DNS latency anomalies helps prevent outages and performance issues.

**How:**  
Outline the workflow: collect DNS latency data, train an autoencoder, detect anomalies, and send Slack alerts.

**What did I get:**  
A clear roadmap for DNS latency anomaly detection.

---

## Step 2: Install Required Libraries 🧩
**Why:**  
pandas, numpy, scikit-learn, matplotlib for data processing and ML; requests for Slack alerts.

**How:**  
```sh
pip install pandas numpy scikit-learn matplotlib requests --quiet
```

**What did I get:**  
All necessary tools installed locally.

---

## Step 3: Collect DNS Query Latency Data 🕒
**Why:**  
Need time-series data of DNS query latencies for anomaly detection.

**How:**  
- Simulate or collect DNS latency data (timestamp, latency_ms).
- Save as CSV for analysis.

**What did I get:**  
A time-series dataset of DNS latencies.

---

## Step 4: Load and Visualize DNS Latency Data 📊
**Why:**  
Visualize data to understand normal patterns and spot obvious spikes.

**How:**  
- Load CSV into pandas.
- Plot latency over time.

**What did I get:**  
Baseline understanding of DNS latency behavior.

---

## Step 5: Train Autoencoder for Anomaly Detection 🤖
**Why:**  
Autoencoders learn normal patterns and flag deviations as anomalies.

**How:**  
- Normalize latency values.
- Train a simple autoencoder (scikit-learn MLPRegressor or Keras).
- Compute reconstruction error for each point.

**What did I get:**  
A model that can detect irregular latency spikes.

---

## Step 6: Detect Latency Anomalies 🚨
**Why:**  
Identify timestamps where latency drifts beyond normal.

**How:**  
- Set anomaly threshold (e.g., mean + 3*std of reconstruction error).
- Flag points above threshold as anomalies.

**What did I get:**  
List of anomaly timestamps and values.

---
## Step 7: Visualize Anomalies on Latency Plot 📈
**Why:**  
Show anomalies on the time-series plot for easy interpretation.

**How:**  
- Overlay anomaly points on latency plot (red dots).

**What did I get:**  
Clear visualization of when and where anomalies occurred.

---

## Step 8: Alert via Slack When Anomaly Detected 💬
**Why:**  
Immediate notification helps SREs respond quickly.

**How:**  
- Use Slack Incoming Webhook.
- Send alert message with timestamp and latency when anomaly is detected.

**What did I get:**  
Real-time alerts for DNS latency spikes.

---

## Step 9: Review & Iterate 🔄
**Why:**  
Tune model and threshold for best results.

**How:**  
- Adjust autoencoder parameters and anomaly threshold.
- Re-run detection and alerting.

**What did I get:**  
Improved anomaly detection accuracy.

---
