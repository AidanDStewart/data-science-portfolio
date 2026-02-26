# MLB Breakout Prediction Model  
### Identifying a 2+ WAR Jump Candidate Using Elastic Net Logistic Regression

Aidan Stewart  
R | baseballr | FanGraphs Data  

---

## Project Objective

Using publicly available FanGraphs data, I built a predictive model to estimate the probability that an MLB hitter would “break out” in the following season.

**Definition of Breakout:**  
A player increases their WAR by **2.0 or more** year-over-year.

The model ultimately identified **Jordan Walker (St. Louis Cardinals)** as a strong breakout candidate.

---

## Data Collection

- Data Source: FanGraphs  
- Accessed using the `baseballr` package (Bill Petti)  
- Function used: `fg_batter_leaders()`  
- Seasons pulled: 2023, 2024, 2025  
- Minimum: 200 plate appearances  

Each season initially contained ~350 variables per player.

---

## Data Processing & Feature Engineering

- Grouped variables into categories:
  - Batted ball metrics  
  - Plate discipline metrics  
  - Contact quality metrics  

- Selected **48 predictor variables**  
- Created response variable: `did_breakout` (1 = WAR increase ≥ 2, 0 = otherwise)  
- Joined consecutive seasons to compute year-over-year WAR change  

---

## Modeling Approach

Because of:
- High dimensionality  
- Correlated predictors  

I implemented **Elastic Net Logistic Regression**, which combines Ridge and Lasso penalties.

### Model Training
- Trained on 2023 → 2024 breakout outcomes  
- Tested on 2024 data  

### Model Performance
- **AUC = 0.635**

Interpretation:  
Given one breakout player and one non-breakout player, the model correctly assigns higher probability to the breakout player **63.5% of the time**, significantly better than random guessing (50%).

---

## 2025 Breakout Predictions

After training and evaluation, I predicted 2025 breakout probabilities and listed the top 10 candidates.

I excluded players with >3 WAR seasons in 2025, focusing on players likely to take a meaningful step forward rather than already-established stars.

---

## Selected Breakout Candidate: Jordan Walker

- Team: St. Louis Cardinals  
- Position: Right Field  
- Former 1st Round Draft Pick (2020)  
- Career WAR (first 3 seasons): -0.9  

Model breakout probability: **0.73**

---

## Coefficient Analysis

Top contributing features to Walker’s breakout probability:

- Max Exit Velocity  
- Average Exit Velocity  
- Batting Average (negative coefficient)  
- AVG+ (negative coefficient)  

Interpretation:
- Walker hits the ball extremely hard (high upside)
- Below average batting average says he has room to improve

---

## Pitch-Level Analysis (Baseball Savant)

To supplement the model, I analyzed Walker’s 2025 pitch-level data:

### Launch Angle vs Exit Velocity Plot
- Average Launch Angle: **10.3°**
- Hard contact primarily between -10° to 25°
- Produces many hard ground balls
<img width="935" height="577" alt="image" src="https://github.com/user-attachments/assets/0b67e95a-121a-42a8-9d3f-8f11286b56cf" />

Comparison:
- 2020 Kyle Schwarber had an 8.8° launch angle before later increasing it and becoming an MVP candidate.

### Strike Zone xStats Visualizations
Plotted:
- xBA  
- xSLG  
- xwOBA  
<img width="935" height="577" alt="image" src="https://github.com/user-attachments/assets/4ddc6229-d8f4-471e-a7a0-20f92ff6896d" />
<img width="935" height="577" alt="image" src="https://github.com/user-attachments/assets/edc3a95f-2beb-43d0-826f-341c0a588290" />
<img width="935" height="577" alt="image" src="https://github.com/user-attachments/assets/608d9361-f57d-4a09-932d-2f2764b6f219" />


Key Observations:
- Inconsistenties in the top part of the zone between xBA and xSLG 
- Up and in, as well as low and away pitches can be attacked more


---

## Conclusion

Jordan Walker has:

- 99th percentile bat speed  
- 1st percentile whiff rate  
- Elite exit velocity metrics  

If he:
- Improves contact consistency  
- Elevates the baseball more consistently  

He has strong potential to increase WAR by 2+ and take a major step forward.

---

## Repository Contents

- `MiamiMarlinsPredictionCode.Rmd` – Full RMarkdown analysis  
- Model outputs and visualizations  
- Project write-up  

---

## Skills Demonstrated

Elastic Net Regression, Logistic Modeling, Feature Engineering, Model Evaluation (AUC), Coefficient Interpretation, Pitch-Level Data Analysis, R Programming, Sports Analytics
