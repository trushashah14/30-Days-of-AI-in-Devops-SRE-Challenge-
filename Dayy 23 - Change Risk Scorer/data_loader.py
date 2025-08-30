import pandas as pd

def load_pr_diff(file_path):
    # Simulate PR diff features: lines added, deleted, files changed
    return pd.read_csv(file_path)

def load_test_coverage(file_path):
    # Simulate test coverage metrics
    return pd.read_csv(file_path)

def load_deployment_history(file_path):
    # Historical success/failure rates
    return pd.read_csv(file_path)

def merge_features(pr_df, coverage_df, deploy_df):
    # Merge on PR ID or commit hash
    return pr_df.merge(coverage_df, on="pr_id").merge(deploy_df, on="pr_id")