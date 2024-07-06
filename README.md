This project implements a basic mean reversion trading strategy for gold futures using straightforward Python libraries and the Yahoo Finance API.

Please note, this project serves solely educational purposes and should not be deployed in live trading without rigorous testing and analysis. Use it at your own discretion.

Overview

This strategy utilizes two moving averages (30-day and 90-day) of the daily closing prices of gold futures. It triggers a buy signal when the difference between the price and the moving averages drops below a specified threshold. Conversely, it generates a sell signal when this difference exceeds another fixed threshold.

The strategy incorporates a stop-loss rule to mitigate downside risk: if the price falls below a certain percentage of the previous day's closing price, any open position is closed.

Results

Using historical data spanning from January 1, 2021, to January 1, 2023, the strategy yielded a total return of $7,577.40 from an initial capital of $100,000, corresponding to a percentage return of 7.58%. Over this period, the strategy executed a total of 18 trades, resulting in 8 profitable trades and 1 loss.

How to Utilize

To execute the strategy, clone the repository and execute the mean_reversion_strategy.py script. For backtesting and visualizing the trading signals, use the gold_futures_meanReversion_backtest.py script. Ensure that you have installed necessary dependencies (yfinance, pandas, and matplotlib) by running pip install -r requirements.txt.
