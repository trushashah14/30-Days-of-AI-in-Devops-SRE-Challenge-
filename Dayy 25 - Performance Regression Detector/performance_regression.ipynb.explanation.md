# How Are "Regression" and "OK" Identified in the Data?

## ML/AI Approach Used in the Notebook

- For each metric (e.g., latency, throughput, error_rate), the notebook calculates:
  - `mean_old`: The average value from the old benchmark data.
  - `mean_new`: The average value from the new benchmark data.
  - `diff`: The difference (`mean_new - mean_old`).

- **Labeling for ML:**
  - If `mean_new > mean_old`, the metric is labeled as a regression (`regression = 1`).
  - If `mean_new <= mean_old`, it is labeled as OK (`regression = 0`).

- These labeled results are used to train a Logistic Regression classifier.
- The classifier predicts for each metric whether it is a regression (`⚠️ REGRESSION (ML)`) or OK (`✅ OK (ML)`) based on the features (`mean_old`, `mean_new`, `diff`).

## Output Example

- If the ML model predicts `1` for a metric, it is flagged as a regression.
- If the ML model predicts `0`, it is flagged as OK.

**This dynamic approach allows the model to learn patterns in the data, rather than relying on fixed thresholds.**
