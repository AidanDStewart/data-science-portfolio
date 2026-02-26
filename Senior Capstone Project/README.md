# Leveraging Advanced Analytics to Predict Baseball Production

Senior Capstone Project – South Dakota State University  
Aidan Stewart | Spring 2024  

---

## Overview

This project builds a statistical model to quantify and predict MLB player production across aging curves.  

Using data from Baseball Reference and Baseball Savant (Statcast), I created a weighted **CompositeScore** metric combining offensive and defensive performance, then modeled how it changes with age.

The goal: identify when players peak and when decline begins to inform contract and roster decisions.

---

## Production Metric

CompositeScore was built from:

- OPS  
- xBA  
- xISO  
- OAA  

Variables were standardized and weighted:
- 60% Offensive  
- 40% Defensive  

---

## Modeling

Tested:
- Linear regression  
- Quadratic regression  
- Cubic regression  

**Best Model:** Normalized Quadratic  
- Adjusted R² = 0.72  
- All predictors statistically significant  

---

## Key Findings

- Peak production occurs around **ages 26–28**  
- Strong performance often continues through age 31  
- Statistically significant decline begins shortly after peak  

---

## Repository Contents

- `Senior Capstone Project.Rmd` – Full analysis in R  
- Final Paper (PDF)  
- Model outputs & visualizations  

---

## Video Presentation

https://youtu.be/j09sI2JkxhU

---

## ⚾ Skills Demonstrated

R Programming, Data Cleaning, Feature Engineering, Regression Modeling, Hypothesis Testing, Sports Analytics
