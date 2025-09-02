import sys
import pandas as pd
import logging
import os
from sklearn.linear_model import LogisticRegression
import numpy as np

logging.basicConfig(level=logging.INFO)

def load_benchmarks(path):
    logging.info(f"Loading benchmark data from {path}")
    if not path or not os.path.isfile(path):
        print(f"❌ File not found: {path}")
        return None
    try:
        df = pd.read_csv(path)
        if df.empty:
            print(f"❌ File is empty: {path}")
            return None
        return df
    except Exception as e:
        print(f"❌ Error loading file {path}: {e}")
        return None

def compare_metrics(old_df, new_df, threshold=0.05):
    results = []
    for col in old_df.columns:
        if col not in new_df.columns:
            print(f"⚠️ Column '{col}' not found in new benchmark file. Skipping.")
            continue
        old_vals = old_df[col].dropna()
        new_vals = new_df[col].dropna()
        if len(old_vals) < 2 or len(new_vals) < 2:
            print(f"⚠️ Not enough data for column '{col}'. Skipping.")
            continue
        try:
            stat, pval = ttest_ind(old_vals, new_vals, equal_var=False)
            mean_old = old_vals.mean()
            mean_new = new_vals.mean()
            regression = (mean_new > mean_old) and (pval < threshold)
            results.append({
                "metric": col,
                "mean_old": mean_old,
                "mean_new": mean_new,
                "p_value": pval,
                "regression": regression
            })
        except Exception as e:
            print(f"❌ Error comparing column '{col}': {e}")
    return results

def report(results):
    print("Performance Regression Report")
    print("-" * 40)
    for r in results:
        flag = "⚠️ REGRESSION" if r["regression"] else "✅ OK"
        print(f"{r['metric']}: old={r['mean_old']:.4f}, new={r['mean_new']:.4f}, p={r['p_value']:.4g} {flag}")

def prepare_ml_features(old_df, new_df):
    results = []
    for col in old_df.columns:
        if col not in new_df.columns:
            print(f"⚠️ Column '{col}' not found in new benchmark file. Skipping.")
            continue
        old_vals = old_df[col].dropna()
        new_vals = new_df[col].dropna()
        if len(old_vals) < 2 or len(new_vals) < 2:
            print(f"⚠️ Not enough data for column '{col}'. Skipping.")
            continue
        mean_old = old_vals.mean()
        mean_new = new_vals.mean()
        diff = mean_new - mean_old
        # For demonstration, label as regression if new > old
        regression = int(mean_new > mean_old)
        results.append({
            "metric": col,
            "mean_old": mean_old,
            "mean_new": mean_new,
            "diff": diff,
            "regression": regression
        })
    return results

def ml_regression_report(results):
    print("Performance Regression Report (ML/AI)")
    print("-" * 40)
    if len(results) < 2:
        print("Not enough results for ML classifier demo.")
        return
    X = np.array([[r["mean_old"], r["mean_new"], r["diff"]] for r in results])
    y = np.array([r["regression"] for r in results])
    clf = LogisticRegression()
    clf.fit(X, y)
    y_pred = clf.predict(X)
    for i, r in enumerate(results):
        ml_flag = "⚠️ REGRESSION (ML)" if y_pred[i] else "✅ OK (ML)"
        print(f"{r['metric']}: old={r['mean_old']:.4f}, new={r['mean_new']:.4f}, diff={r['diff']:.4f} | {ml_flag}")

if __name__ == "__main__":
    old_path = "sample_benchmark_old.csv"
    new_path = "sample_benchmark_new.csv"

    old_df = load_benchmarks(old_path)
    new_df = load_benchmarks(new_path)

    if old_df is None or new_df is None:
        print("❌ Please provide valid CSV files for both old and new benchmarks.")
        sys.exit(1)

    results = prepare_ml_features(old_df, new_df)
    ml_regression_report(results)
