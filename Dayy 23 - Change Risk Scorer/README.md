# Day 23: Change Risk Scorer 🚦 – Aug 30, 2025

## Challenge Description 🎯
Use AI to score the risk of proposed infrastructure or application changes before deployment. Integrate PR diff, test coverage, and deployment history to predict risk and explain reasoning.

## Objective 🚀
- Load change features (lines changed, coverage, deployment history)
- Train a risk classifier (RandomForest)
- Use LLM or rule-based explainer for risk reasoning
- Visualize risk scores and explanations for multiple changes

## Code & Implementation 💻
- **Notebook**: [`change_risk_scorer.ipynb`](./change_risk_scorer.ipynb)  
  Main workflow for feature generation, model training, prediction, explanation, and visualization.
- **Step-by-Step Solution**: [`Step-by-Step-Solution.md`](./Step-by-Step-Solution.md)  
  Detailed explanation of each notebook step, including rationale and insights.
- **Sample Data**:  
  - `data/pr_diff.csv` – PR diff features  
  - `data/coverage.csv` – test coverage  
  - `data/deploy.csv` – deployment history and risk labels
- **Output**:  
  - `data/predicted_risks_with_explanations.csv` – risk predictions and explanations  
  - `data/predicted_risks_with_explanations.html` – styled risk table  
  - `data/predicted_risks_with_explanations.pdf` – PDF report

## Workflow 🔄

1. **Generate Features:**  
   Simulate PR diff, coverage, and deployment history data.
2. **Load & Merge Data:**  
   Combine features for each change.
3. **Train Risk Model:**  
   Fit RandomForest classifier on labeled risk data.
4. **Predict & Explain:**  
   Score risk for each change and generate explanations.
5. **Visualize:**  
   Histogram of risk confidence, styled HTML/PDF table.
6. **Review & Export:**  
   Save results for review and reporting.

## Why Each Step Was Chosen 📊
- **Feature Engineering:**  
  Captures key risk factors for changes.
- **ML Classification:**  
  Automates risk scoring based on historical data.
- **Explanation:**  
  Makes risk scores actionable for reviewers.
- **Visualization:**  
  Highlights risk distribution and enables easy review.

## Interpretation of Results 🧠
- **CSV/HTML/PDF Outputs:**  
  Show risk scores, confidence, and explanations for each change.
- **Histogram:**  
  Reveals distribution of high-risk changes.

## What Did I Learn 🧩
- ML can automate risk scoring for code/infrastructure changes.
- Combining multiple features improves risk prediction.
- Explanations are critical for actionable risk management.
- Visual reporting aids change review and approval.

## How to Use in Real-World DevOps/SRE 🌍

### Automated Change Risk Review
**Use Case:**  
Pre-deployment risk scoring for PRs and infrastructure changes.

**Implementation:**  
- Integrate with CI/CD pipelines for automated risk review.
- Use explanations to guide mitigation and rollback planning.

**Industry Examples:**  
- SaaS teams reviewing risky PRs before merge.
- SRE teams prioritizing change reviews based on risk.

## Where Was AI Used? 🤖

- **AI Used:**  
  RandomForest classifier for risk prediction; LLM/rule-based explainer for reasoning.

**AI Technologies Used:**  
- scikit-learn (RandomForest)
- Python (feature engineering, orchestration)
- LLM (optional, for advanced explanations)

## References 📖
- [Change Risk Analysis](https://sre.google/sre-book/change-management/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Ollama Documentation](https://ollama.com/docs)

## Future Enhancements 🚀
- Integrate with real PR and deployment data
- Add more features (file types, code ownership, incident links)
- Use LLM for deeper, context-aware explanations
- Automate feedback loop for continuous model improvement
