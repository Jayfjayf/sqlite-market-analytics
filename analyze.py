import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("market.db")

# pull up 20 day moving average from listed assets
with open("queries2.sql", "r") as f: 
    query = f.read()

df = pd.read_sql(query, conn)
conn.close()

df["trade_date"] = pd.to_datetime(df["trade_date"])

tickers = df["ticker"].unique()

# overlaid plot of the close price and 20 day moving average 
fig, axes = plt.subplots(len(tickers), 1, figsize=(11, 9), sharex=True)

for ax, ticker in zip(axes, tickers):
    subset = df[df["ticker"] == ticker]
    asset_name = subset["asset_name"].iloc[0]
    
    ax.plot(subset["trade_date"], subset["close_price"], label="Daily Close")
    ax.plot(subset["trade_date"], subset["moving_average_20d"], label="20-Day SMA (SQL Window)")
    
    ax.set_title(f"{asset_name} ({ticker}) — Daily Close vs. 20-Day Moving Average")
    ax.set_ylabel("Price (USD)")
    ax.legend()

plt.xlabel("Trade Date (2026)")
plt.tight_layout()
plt.show()