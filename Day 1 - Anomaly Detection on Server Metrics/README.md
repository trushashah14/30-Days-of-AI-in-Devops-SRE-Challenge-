# Day 1: Anomaly Detection on Server Metrics

**Date:** 2025-08-08

## Description
Applied anomaly detection to server metrics (CPU usage/time-series) using threshold-based methods and advanced ML algorithms (Isolation Forest & One-Class SVM) to identify outliers and potential incidents.

## Why is this task relevant to DevOps/SRE/AI?
Early detection of abnormal server behavior helps prevent outages and enables proactive incident response. AI/ML can automate and enhance this process.


## Code & Implementation
- **Notebook**: [anomaly_detection.ipynb](./anomaly_detection.ipynb) - Complete implementation
- **Documentation**: [Step-by-Step-Guide.md](./Step-by-Step-Guide.md) - Detailed methodology and challenges

## Results

### Threshold-Based Detection (Step 2)
- Detected 2 anomalies at 08:00 (90% CPU) and 18:00 (95% CPU)
- 100% accuracy with simple threshold method (CPU > 50%)

### Machine Learning Detection (Step 3)
- **Isolation Forest**: Detected 3 anomalies (hours 7, 8, 18)
- **One-Class SVM**: Detected 2 anomalies (hours 2, 7)
- **Algorithm Diversity**: Each method detected different anomaly patterns
- **Zero Complete Agreement**: Shows complementary nature of different approaches

### Visualizations
![CPU Anomaly Detection](./cpu_anomaly_detection_plot.png)
![Method Comparison](./anomaly_comparison_plot.png)

## What did I learn?
- Threshold vs. ML-based anomaly detection approaches
- **Two ML Algorithms**: Isolation Forest (tree-based) and One-Class SVM (boundary-based)
- Algorithm complementarity: Different methods detect different anomaly types
- Data preprocessing and environment setup challenges
- Multi-algorithm comparison and evaluation methods

## References & Resources

### General Anomaly Detection
- [PyOD documentation](https://pyod.readthedocs.io/en/latest/)
- [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html)
- [Intro to Anomaly Detection in Python](https://towardsdatascience.com/anomaly-detection-in-python-using-scikit-learn-36b6f2c2e2d2)

### Isolation Forest Resources
- [Isolation Forest Original Paper](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf)
- [Isolation Forest in scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html)
- [Understanding Isolation Forest](https://towardsdatascience.com/isolation-forest-algorithm-for-anomaly-detection-c4f8b0ef3e8e)

### One-Class SVM Resources
- [One-Class SVM Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html)
- [One-Class SVM for Novelty Detection](https://scikit-learn.org/stable/auto_examples/svm/plot_oneclass.html)
- [Support Vector Machines for Anomaly Detection](https://machinelearningmastery.com/one-class-classification-algorithms/)
- [SVM Anomaly Detection Tutorial](https://towardsdatascience.com/anomaly-detection-with-one-class-svm-8b9c7a0e0c1f)

### Data Processing & Visualization
- [pandas documentation](https://pandas.pydata.org/docs/)
- [matplotlib documentation](https://matplotlib.org/stable/users/index.html)
- [Visualizing Time Series Data](https://realpython.com/python-matplotlib-guide/)

## Real-World Applications

### Threshold-Based Detection
**Use Case**: **AWS CloudWatch CPU Alerts**
- **Implementation**: Set CPU utilization alerts at 80% threshold for EC2 instances
- **Advantage**: Immediate alerts for critical resource exhaustion
- **Industry Example**: E-commerce platforms use threshold alerts during Black Friday traffic spikes
- **DevOps Integration**: Automatically trigger auto-scaling groups when CPU > 75%

### Isolation Forest
**Use Case**: **Netflix Content Delivery Network (CDN) Monitoring**
- **Implementation**: Detect unusual traffic patterns across global edge servers
- **Advantage**: Identifies complex patterns like coordinated DDoS attacks or viral content spikes
- **Industry Example**: Streaming services detect content delivery anomalies before user complaints
- **SRE Integration**: Proactive capacity planning and geographic load balancing

### One-Class SVM
**Use Case**: **Financial Trading System Performance Monitoring**
- **Implementation**: Monitor API response times and transaction processing latencies
- **Advantage**: Detects subtle performance degradation patterns before system failure
- **Industry Example**: Banks use SVM to detect trading system anomalies during market volatility
- **Production Integration**: Triggers circuit breakers and failover mechanisms automatically

## Next Steps/Improvements
- **Multi-Metric Analysis**: Extend to memory, disk I/O, network bandwidth, and response time metrics
- **Real Production Data**: Apply algorithms to actual server logs with noise and missing data
- **Ensemble Methods**: Combine multiple algorithms with weighted voting for improved accuracy
- **Real-Time Processing**: Stream processing with Apache Kafka and real-time ML inference
- **Dashboard Integration**: Grafana/Kibana dashboards with anomaly overlays and alert management


