import pandas as pd

def summarize_fatigue(fatigue_df):
    """
    Aggregates fatigue metrics per engineer over the input period.
    Returns a summary DataFrame with total days, average score, max score,
    and count of days above fatigue threshold.
    """
    summary = fatigue_df.groupby("assigned_to").agg({
        "fatigue_score": [
            "count", 
            "mean", 
            "max", 
            lambda x: (x > 4).sum()  # Threshold configurable if needed
        ]
    }).reset_index()

    summary.columns = [
        "engineer", 
        "total_days", 
        "avg_score", 
        "max_score", 
        "days_above_threshold"
    ]
    return summary

def generate_monthly_rotation_plan(summary_df, threshold=4):
    """
    Generates proactive rotation suggestions based on fatigue trends.
    Uses tiered logic to prioritize off-call, monitor, and fallback roles.
    """
    suggestions = []
    for _, row in summary_df.iterrows():
        max_score = row["max_score"]
        avg_score = row["avg_score"]
        days_above = row["days_above_threshold"]

        # Tier 1: High fatigue
        if max_score >= 7 or days_above >= 3:
            action = "🔴 Rotate off-call"
            reason = f"Max fatigue {max_score}, {days_above} days above threshold"

        # Tier 2: Moderate fatigue
        elif max_score >= threshold or days_above >= 1:
            action = "🟠 Monitor closely"
            reason = f"Max fatigue {max_score}, {days_above} days above threshold"

        # Tier 3: Low fatigue
        else:
            action = "🟢 Eligible for fallback or lead"
            reason = f"Stable fatigue profile (max {max_score}, {days_above} days above threshold)"

        suggestions.append({
            "engineer": row["engineer"],
            "suggested_action": action,
            "reason": reason
        })

    return pd.DataFrame(suggestions)