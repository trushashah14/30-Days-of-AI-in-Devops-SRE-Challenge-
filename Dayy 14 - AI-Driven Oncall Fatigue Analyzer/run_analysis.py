import pandas as pd
from mock_api.pagerduty_mock import generate_mock_incidents
from fatigue_model import compute_fatigue_scores
from suggest_rotation_tweaks import (
    generate_monthly_rotation_plan,
    summarize_fatigue  # ✅ Add this import
)

# Step 1: Generate mock incident data
engineers = ["nina", "kai", "ravi", "maria", "liam",
    "sofia", "dante", "yuki", "amir", "zara", "noah", "meera", "elena",
    "devon", "fatima", "jun"]
mock_data = generate_mock_incidents(engineers)
incident_df = pd.DataFrame(mock_data)

# Save raw incident data
incident_df.to_csv("data/mock_incidents.csv", index=False)

# Step 2: Compute fatigue scores
fatigue_df = compute_fatigue_scores(incident_df)
fatigue_df.to_csv("data/fatigue_scores.csv", index=False)

# Step 3: Summarize fatigue and generate monthly rotation plan
summary_df = summarize_fatigue(fatigue_df)
rotation_plan_df = generate_monthly_rotation_plan(summary_df)

# Save summary and plan
summary_df.to_csv("data/fatigue_summary.csv", index=False)
rotation_plan_df.to_csv("data/rotation_plan.csv", index=False)


# Final output confirmation
print("✅ All outputs saved:")
print("- data/mock_incidents.csv")
print("- data/fatigue_scores.csv")
print("- data/fatigue_summary.csv")
print("- data/rotation_plan.csv")
