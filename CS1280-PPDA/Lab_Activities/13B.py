import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stock_prices.csv", parse_dates=["Date"], index_col="Date")

plt.figure(figsize=(10, 5))
plt.plot(df.index, df["Close"], label="Stock Price", color='b')
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("Stock Price Trend Over Time")
plt.legend()
plt.show()

df["50-day MA"] = df["Close"].rolling(window=50).mean()
df["200-day MA"] = df["Close"].rolling(window=200).mean()

plt.figure(figsize=(10, 5))
plt.plot(df.index, df["Close"], label="Stock Price", color='b')
plt.plot(df.index, df["50-day MA"], label="50-Day MA", color='r')
plt.plot(df.index, df["200-day MA"], label="200-Day MA", color='g')
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("Stock Price with Moving Averages")
plt.legend()
plt.show()
