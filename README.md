# Aidan Stewart - Baseball Research & Development Portfolio

**Data Analyst | Baseball Analytics | R | Player Development**

This portfolio highlights projects focused on predictive modeling, player evaluation, and applied baseball research using R.

---

## Senior Capstone Project

**Skills Demonstrated:** R, Data Cleaning, Feature Engineering, Regression Modeling, Hypothesis Testing, Sports Analytics

### Overview
This senior capstone project developed a composite performance metric to model MLB player production over time. Using data from Baseball Reference and Baseball Savant (Statcast), I constructed a weighted “CompositeScore” combining offensive and defensive metrics, then analyzed how production changes with age.

The objective was to identify peak performance windows and statistically significant decline phases to provide insights relevant to contract valuation and roster construction.

### What I Did
- Cleaned and merged two separate baseball datasets
- Performed exploratory data analysis on each dataset 
- Engineered a weighted composite production metric (60% offense / 40% defense)
- Standardized variables for fair comparison 
- Built and compared linear, quadratic, and cubic regression models
- Applied mean normalization to remove bias
- Conducted a t-test to identify significant changes in production
- Presented results in both written and video format

### Deliverables
- Final Paper
- RMarkdown file with full analysis
- YouTube Presentation  
https://youtu.be/j09sI2JkxhU

---

## Breakout Prediction Project

**Skills Demonstrated:** R, Elastic Net Logistic Regression, Feature Engineering, Model Evaluation  

### Overview
This project built a predictive model to estimate the probability that an MLB hitter would increase their WAR by 2.0 or more in the following season. Using FanGraphs data accessed through the baseballr package, I focused on identifying underlying skill indicators that signal future breakout performance rather than relying solely on traditional statistics.

The model ultimately identified Jordan Walker (St. Louis Cardinals) as a strong breakout candidate based on contact quality, exit velocity, and improvement indicators.

### What I Did
- Pulled hitter data from multiple seasons on FanGraphs (2023-2025)
- Identified 48 predictive features across batted ball, discipline, and contact quality metrics
- Created a binary response variable (WAR increase >= 2)
- Implemented Elastic Net Logistic Regression to hand correlated predictors
- Evaluated model performance (AUC = 0.635)
- Conducted coefficient analysis to find which variables correlated to breaking out
- Compared model results with Baseball Savant visualizations

### Deliverables
- RMarkdown file with full analysis
- Answer writeup explaining reasoning

---

## Career Focus

I am particularly interested in:
- Player Development Analytics  
- Pitching Analytics  
- Applied Sports Science  
- Predictive Modeling in Baseball  
