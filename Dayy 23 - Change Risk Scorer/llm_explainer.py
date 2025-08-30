def explain_risk(pr_features, risk_score, risk_prob):
    explanation = f"""
    Risk Level: {risk_score} ({risk_prob:.2f} confidence)
    • Lines changed: {pr_features['lines_changed']}
    • Test coverage: {pr_features['coverage']}%
    • Deployment history: {pr_features['past_failures']} failures
    """
    if risk_score == "High":
        explanation += "\n⚠️ This change touches critical files with low test coverage and a history of failed rollouts."
    elif risk_score == "Medium":
        explanation += "\n⚠️ Moderate risk due to either size, coverage, or past failures."
    else:
        explanation += "\n✅ Low risk: small change, good coverage, stable history."
    return explanation.strip()