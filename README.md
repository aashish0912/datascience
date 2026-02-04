# Primetrade Data Science Assignment

Subject: Analysis of Trader Behavior vs Market Sentiment

## Overview
This repository contains the analysis for the data science intern assignment. The goal is to study how Bitcoin market sentiment (Fear & Greed Index) impacts trader performance on Hyperliquid.

## Project Structure
- `notebooks/Trader_Analysis.ipynb`: The primary analysis notebook containing:
    - Data loading and cleaning
    - Metric feature engineering (PnL, Win Rate, Volume, Bias)
    - Visualization and Segmentation
    - Strategic insights
- `data/`: Contains the datasets (`bitcoin_sentiment.csv`, `trader_data.csv`).
- `requirements.txt`: List of dependencies.

## Summary of Findings
- **Profitable Volatility**: The highest average PnL and trading volume occur during "Fear" periods.
- **Sentiment Correlation**: Traders shift their directional bias effectively (Net Short in Fear, Net Long in Greed), but short-selling during Fear yields better risk-adjusted returns.
- **Segmentation**: Higher volume traders ("Whales") maintain more consistent win rates during "Extreme Greed" compared to smaller traders.

## Setup Instructions
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook notebooks/Trader_Analysis.ipynb
   ```
3. Run Streamlit Dashboard:
   ```bash
   streamlit run dashboard.py
   ```
