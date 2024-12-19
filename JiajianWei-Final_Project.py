from key import API_KEY
import requests
import pandas as pd
import matplotlib.pyplot as plt


class StockAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.polygon.io"

    def get_stock_data(self, ticker, start_date, end_date):
        """Fetch stock data from Polygon API."""
        url = f"{self.base_url}/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{end_date}?apiKey={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()  # Will raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        if "results" in data:
            return pd.DataFrame(data["results"])
        else:
            print("No results found.")
            return pd.DataFrame()


class StockAnalyzer:
    def __init__(self, stock_data):
        self.stock_data = stock_data

    def add_date_column(self): #Convert timestamp to readable date format.
        self.stock_data['Date'] = pd.to_datetime(self.stock_data['t'], unit='ms')

    def calculate_price_changes(self):#Calculate daily price changes.
        self.stock_data['Price Change'] = self.stock_data['c'].diff()


    def calculate_high_low_avg(self):# Calculate high, low, and average prices.
        high_price = self.stock_data['h'].max()
        low_price = self.stock_data['l'].min()
        avg_price = self.stock_data['c'].mean()
        return high_price, low_price, avg_price

class StockVisualizer:
    def __init__(self, stock_data):
        self.stock_data = stock_data

    def plot_price_changes(self):
        """Plot price changes as a line graph."""
        plt.figure(figsize=(10, 6))
        plt.plot(self.stock_data['Date'], self.stock_data['Price Change'], label="Price Change", color='green')
        plt.title("Stock Price Changes Over Time")
        plt.xlabel("Date")
        plt.ylabel("Price Change (USD)")
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_closing_prices(self):
        """Plot closing prices as a line graph."""
        plt.figure(figsize=(10, 6))
        plt.plot(self.stock_data['Date'], self.stock_data['c'], label="Closing Price", color='blue')
        plt.title("Stock Closing Prices Over Time")
        plt.xlabel("Date")
        plt.ylabel("Closing Price (USD)")
        plt.legend()
        plt.grid(True)
        plt.show()



# API Key and Parameters
api_key = API_KEY
ticker = "AAPL"
start_date = "2024-09-20"
end_date = "2024-09-27"

# Fetch Stock Data
stock_api = StockAPI(api_key)
stock_data = stock_api.get_stock_data(ticker, start_date, end_date)

# Analyze Stock Data
analyzer = StockAnalyzer(stock_data)
analyzer.add_date_column()
analyzer.calculate_price_changes()

# Calculate and display statistics
high_price, low_price, avg_price = analyzer.calculate_high_low_avg()
print(f"Highest Price: {high_price}")
print(f"Lowest Price: {low_price}")
print(f"Average Price: {avg_price}")

# Visualize Stock Data
visualizer = StockVisualizer(stock_data)
visualizer.plot_price_changes()  # Price Change graph
visualizer.plot_closing_prices()  # Closing Price graph

