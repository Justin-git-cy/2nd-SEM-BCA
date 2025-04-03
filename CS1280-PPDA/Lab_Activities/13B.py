import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate sample dates
dates = pd.date_range(start="2023-01-01", periods=300, freq="D")

# Simulate stock prices
np.random.seed(42)
prices = np.cumsum(np.random.randn(300) * 2) + 100  # Random walk

# Create DataFrame
df = pd.DataFrame({"Date": dates, "Close": prices})
df.set_index("Date", inplace=True)

# Plot the stock prices
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["Close"], label="Stock Price", color='b')
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("Sample Stock Price Trend Over Time")
plt.legend()
plt.show()
