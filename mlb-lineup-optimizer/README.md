# MLB Lineup Optimization Tool

An interactive data application that builds optimized MLB batting lineups using role-based scoring and explainable analytics.

---

## Overview

This project simulates how a baseball analytics team might construct an optimal batting order.

The application:
- Ingests MLB hitter data
- Stores it in a SQLite database
- Scores players based on lineup role (e.g., leadoff, cleanup)
- Generates an optimized batting order
- Explains *why* each player goes into their lineup position

The goal is to combine data engineering, analytics, and product design into a single project.

---

## Features (MVP)

- Team and season selection
- Player filtering by minimum plate appearances
- Role-based player scoring system
- Optimized lineup generation (1–9)
- Clear, human-readable explanations for each lineup decision
- Visualizations (OBP vs SLG, lineup score distribution)
- Comparison vs baseline lineup (e.g., OPS-based order)

---

## How It Works

### 1. Data Pipeline

- Raw hitter data is collected and stored locally
- Data is cleaned and standardized using Python (pandas)
- Processed data is loaded into a SQLite database

### 2. Scoring System

Players are scored differently depending on lineup role:

| Lineup Spot | Role | Key Metrics |
|------------|------|------------|
| 1 | Leadoff | OBP, BB%, K%, Baserunning |
| 2 | Contact + balance | OBP, SLG, low K% |
| 3 | Best hitter | wRC+, OBP, SLG |
| 4 | Power hitter | SLG, ISO, HardHit% |
| 5 | Secondary power | SLG, ISO, OBP |
| 6–8 | Remaining hitters | OPS, wRC+ |
| 9 | Weakest or 2nd leadoff | OBP, speed |

Each metric is standardized (z-scores) and combined into weighted formulas.

### 3. Optimization

A greedy algorithm assigns:
- The best available player to each lineup spot
- Based on role-specific scores

### 4. Explainability
Each lineup decision includes a plain-language explanation so users understand *why* a player was selected.

---

## Tools Used

- **Python**
  - pandas
  - SQLAlchemy
- **Database**
  - SQLite
- **Frontend**
  - Streamlit
- **Visualization**
  - Plotly / Matplotlib

---

## Project Goals

- Demonstrate a full data analytics project's workflow
- Apply sports analytics concepts
- Build an interactive analytics product
- Emphasize interpretability over hard to understand models

---

## Current Status

- Project setup and Streamlit application initialized
^^^
- Data pipeling
- Scoring System
- Optimization Engine
- Full UI implementation
- Deployment

---

## Future Improvements

- Pitcher Matchup (Select an opposing pitcher and build the lineup against them)
- Multiple lineup view (analytics heavy, traditional, slugging emphasis)
- Simulation-based lineup evaluation
- Team offensive projections

# Author

Aidan Stewart

Data Analytics | Baseball Analytics | Python | SQL
