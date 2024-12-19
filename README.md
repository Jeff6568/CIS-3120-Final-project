# CIS-3120-Final-project - Jiajian Wei
# Stock Data Analysis - Final Project

This project fetches stock data from the Polygon.io API, analyzes the stock price changes, and visualizes the data using Python. The script `JiajianWei-Final_Project.py` performs the following tasks:

- Retrieves stock data for a given ticker symbol (e.g., "AAPL") within a specified date range.
- Analyzes the stock data to calculate daily price changes, high/low prices, and the average closing price.
- Visualizes the stock data through:
  - A line graph of stock price changes over time.
  - A line graph of closing prices over time.

## Requirements
- Python 3.x
- `requests` library
- `pandas` library
- `matplotlib` library

## How to Use
1. Obtain an API key from [Polygon.io](https://polygon.io/) and store it in a file named `key.py` with the variable `API_KEY`.
2. Modify the script to change the stock ticker and date range as needed.
3. Run the script `JiajianWei-Final_Project.py` to:
   - Fetch stock data.
   - Display calculated high, low, and average prices.
   - Generate and display the graphs of stock price changes and closing prices.