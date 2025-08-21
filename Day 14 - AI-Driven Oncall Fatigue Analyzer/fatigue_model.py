import pandas as pd

def compute_fatigue_scores(incident_df):
    """
    Computes fatigue scores per engineer per day based on incident volume and night alerts.
    Returns a DataFrame with fatigue metrics.
    """
    # Parse timestamps and extract relevant features
    incident_df['created_at'] = pd.to_datetime(incident_df['created_at'])
    incident_df['hour'] = incident_df['created_at'].dt.hour
    incident_df['date'] = incident_df['created_at'].dt.date

    # Flag night alerts (between 10 PM and 6 AM)
    incident_df['night_alert'] = incident_df['hour'].apply(lambda h: 1 if h >= 22 or h < 6 else 0)

    # Aggregate by engineer and date
    grouped = incident_df.groupby(['assigned_to', 'date']).agg(
        total_alerts=('id', 'count'),
        night_alerts=('night_alert', 'sum')
    ).reset_index()

    # Compute fatigue metrics
    grouped['sleep_disruption'] = grouped['night_alerts'].apply(lambda x: 1 if x > 0 else 0)
    grouped['fatigue_score'] = grouped['total_alerts'] + grouped['night_alerts'] * 2

    return grouped