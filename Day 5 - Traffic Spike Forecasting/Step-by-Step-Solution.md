# Day 5: Traffic Spike Forecasting – Step-by-Step Solution

This document explains each step of the notebook, why it is needed, how it was implemented, and what insights were gained. It also discusses the choice of visualization and the difference between historical and forecasted values.

---

## Step 1: Introduction & Planning

**Why:**  
Clarifies the goal: to forecast HTTP traffic spikes using time series modeling, with no cloud cost.

**How:**  
A markdown cell outlines the workflow: simulate data, train a model, forecast, and visualize.

**What did I get:**  
A clear roadmap for the notebook and project.

---

## Step 2: Install Required Libraries

**Why:**  
Prophet, pandas, matplotlib, and plotly are needed for time series modeling, data manipulation, and visualization.

**How:**  
`!pip install prophet pandas matplotlib --quiet`  
`!pip install plotly --quiet`

**What did I get:**  
All necessary tools installed locally, ensuring no cloud cost.

---

## Step 3: Import Libraries

**Why:**  
To use the installed packages for data processing, modeling, and plotting.

**How:**  
Standard Python imports for pandas, numpy, matplotlib, and Prophet.

**What did I get:**  
Access to functions for data simulation, modeling, and visualization.

---

## Step 4: Simulate Historical HTTP Request Data

**Why:**  
No access to real CloudWatch data; simulation allows testing the forecasting workflow.

**How:**  
- Generate hourly timestamps for 14 days.
- Create a base value, add a sinusoidal pattern (daily cycles), a linear trend (growth), and random noise.
- Store in a pandas DataFrame.

**What did I get:**  
A realistic dataset mimicking actual traffic patterns, ready for modeling.

---

## Step 5: Visualize Simulated Data

**Why:**  
To understand the generated data and verify its realism before modeling.

**How:**  
Plot request counts over time using matplotlib.

**What did I get:**  
A graph showing periodic spikes (daily cycles), an upward trend, and random fluctuations.

---

## Step 6: Train Prophet Model

**Why:**  
Prophet is designed for time series forecasting, capturing trends and seasonality.

**How:**  
Initialize and fit Prophet on the simulated data.

**What did I get:**  
A trained model that understands the underlying patterns in your traffic data.

---

## Step 7: Forecast Next 24 Hours

**Why:**  
To predict future traffic and prepare for potential spikes.

**How:**  
Use Prophet to forecast the next 24 hourly intervals.

**What did I get:**  
A table of predicted values and confidence intervals for the next day.

---

## Step 8: Visualize Predictions vs. Real Data

**Why this graph was chosen:**  
A time series line plot overlays historical and forecasted values, making it easy to compare past and future trends.  
- **Blue line:** Historical (simulated) data  
- **Orange line:** Prophet's forecast  
- **Shaded region:** Confidence interval  
- **Red dashed line:** Forecast start

**How:**  
Plot both historical and forecasted data on the same axes, with clear labels and a vertical line marking the transition.

**What did I get:**  
A visual comparison of past traffic and future expectations, crucial for capacity planning.

---

## Difference Between Historical and Forecasted Values

**Why is there a difference?**
- Prophet smooths out random noise and focuses on underlying patterns (trend, seasonality).
- The simulated data includes strong noise and cycles, which may not be fully captured with only 14 days of training data.
- The forecast is typically smoother and may not match every spike in the historical data.

**What does this mean?**
- The model provides a best estimate for future traffic, not an exact replica of past fluctuations.
- The confidence interval shows the range of plausible future values, accounting for uncertainty.

---

## Step 9: Alternative Graph Visualizations

**Why:**  
Different visualizations provide unique perspectives on model performance and forecast accuracy.

**How:**  
Several plots were created in addition to the time series plot:

- **Scatter Plot:**  
  - *Why plotted:* To visualize individual data points for both historical and forecasted values.
  - *Difference from time series plot:* Emphasizes the spread, clusters, and outliers rather than trends.
  - *Interpretation:* Useful for spotting variability and where predictions deviate from actuals.

- **Bar Chart:**  
  - *Why plotted:* To compare actual and forecasted values for the last 24 hours, hour-by-hour.
  - *Difference from time series plot:* Focuses on short-term, discrete intervals rather than continuous trends.
  - *Interpretation:* Makes it easy to see where the forecast diverges from reality in specific hours.

- **Residual Plot:**  
  - *Why plotted:* To show the error (difference) between actual and forecasted values for each timestamp.
  - *Difference from time series plot:* Highlights model accuracy and bias rather than overall pattern.
  - *Interpretation:* Points near zero indicate good predictions; points far from zero show errors.

- **Interactive Plot (Plotly):**  
  - *Why plotted:* To allow zooming, panning, and hovering for detailed inspection of historical and forecasted data.
  - *Difference from time series plot:* Provides interactivity for deeper exploration, especially with large datasets.
  - *Interpretation:* Useful for communicating results and exploring specific intervals or anomalies.

**What did I get:**  
A comprehensive understanding of model performance, strengths, and weaknesses from multiple visual perspectives.

---

## Step 10: Model Improvement – More Data & Seasonality

**Why:**  
The initial residual plot showed many prediction errors. Increasing the amount of training data and explicitly modeling daily seasonality helps Prophet better learn traffic patterns.

**How:**  
- Simulate 60 days of hourly traffic data instead of 14.
- Retrain Prophet with `daily_seasonality=True`.
- Generate new forecasts and residuals.

**What did I get:**  
A model that better captures periodic spikes and trends, resulting in more accurate predictions.

---

## Step 11: Compare Residuals – Before and After Improvement

**Why:**  
Visual comparison of residuals before and after model improvement helps quantify accuracy gains.

**How:**  
- Plot original residuals (14 days, default Prophet) and improved residuals (60 days, daily seasonality) side-by-side.
- Assess how many points are closer to zero (better predictions).

**What did I get:**  
Clear evidence that more data and proper seasonality modeling reduce errors and improve forecast reliability.

---
