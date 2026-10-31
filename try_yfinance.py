# import yfinance as yf


# tickers = ["AAPL", "MSFT", "BTC"]


# data = yf.download(tickers, start="2025-01-01", end="2026-10-28")

# print(data.head())

# close_prices = data['Close']
# print(close_prices)

import sqlite3

conn = sqlite3.connect("market.db")
cursor = conn.cursor()

print("--- 1. All Assets ---")
cursor.execute("SELECT * FROM assets;")
for row in cursor.fetchall():
    print(row)

print("\n--- 2. Top 5 Highest Closing Prices for Asset #1 (AAPL) ---")
cursor.execute("""
    SELECT trade_date, close_price, volume 
    FROM daily_prices 
    WHERE asset_id = 1 
    ORDER BY close_price DESC 
    LIMIT 5;
""")
for row in cursor.fetchall():
    print(row)
4
print("\n--- 3. Recent Oct 2026 Prices Over $400 ---")
cursor.execute("""
    SELECT asset_id, trade_date, close_price 
    FROM daily_prices 
    WHERE close_price > 400 AND trade_date >= '2026-10-01'
    ORDER BY trade_date DESC 
    LIMIT 5;
""")
for row in cursor.fetchall():
    print(row)

conn.close()