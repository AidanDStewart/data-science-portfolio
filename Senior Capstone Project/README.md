# Leveraging Advanced Analytics to Predict Baseball Production

Senior Capstone Project – South Dakota State University  
Aidan Stewart | Spring 2024  

---

## Overview

This project develops a statistical modeling framework to analyze and predict Major League Baseball (MLB) player performance across aging curves.

Using data from Baseball Reference and Baseball Savant (Statcast), I engineered a weighted **CompositeScore** metric and modeled how player production evolves with age.

The goal is to identify peak perfomance windows and decline patterns to inform data-driven contract and roster decision making.

---

## Problem
MLB teams invest heavily in player contracts, making it critical to understand when players are likely to peak or decline.

This project addresses that problem by:
- Quantifying player production with a unified metric  
- Modeling performance trends over time  
- Identifying statistically significant changes in performance  

---

## Data Sources
- Baseball Reference (career statistics, production benchmarking)  
- Baseball Savant / Statcast (advanced tracking data)

---

## Data Engineering & Preprocessing
- Cleaned and filtered datasets (removed summary rows, irrelevant variables)  
- Handled missing values and standardized percentage-based features  
- Removed outliers (low sample sizes, extreme ages)  
- Normalized shortened 2020 season data for consistency  
- Filtered players with <200 plate appearances to reduce noise  

---

## Feature Engineering

### Composite Performance Metric (CompositeScore)

Developed a weighted performance metric combining offensive and defensive contributions:

**Offensive (60%)**
- OPS  
- xBA  
- xISO  

**Defensive (40%)**
- OAA  

All variables were standardized and combined into a single performance score.  

---

## Modeling Approach

### Models Evaluated
- Linear Regression  
- Quadratic Regression  
- Cubic Regression  

### Final Model: Normalized Quadratic Regression
- Adjusted R²: **0.72**  
- All predictors statistically significant  
- Captures non-linear age-performance relationship  

Normalization removed player-specific bias, isolating true performance trends. 

---

## Statistical Validation

Performed t-tests across age groups to identify statistically significant performance changes:

- Significant decline begins after peak years  
- Strong statistical evidence for age-based performance trends  
- Peak window confirmed through hypothesis testing  

---

## Key Results & Insights
- Peak performance occurs at **ages 26–28**  
- High performance sustained through approximately **age 31**  
- Statistically significant decline begins shortly after peak  
- Normalized model reveals sharper decline when isolating player skill  

These findings can inform:
- Contract timing  
- Player valuation  
- Roster construction decisions  

---

## Repository Contents

- `Senior Capstone Project.Rmd` – Full analysis in R  
- Final Paper (PDF)  
- Model outputs & visualizations  

---

## Future Improvements
- Incorporate injury data and player position  
- Expand to machine learning models (Random Forest, XGBoost)  
- Build an interactive dashboard for real-time analysis  

---

## Video Presentation

https://youtu.be/j09sI2JkxhU

---

## ⚾ Skills Demonstrated

R Programming, Data Cleaning, Feature Engineering, Regression Modeling, Hypothesis Testing, Sports Analytics
