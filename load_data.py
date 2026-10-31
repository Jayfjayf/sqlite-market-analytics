import sqlite3
import yfinance as yf

conn = sqlite3.connect("market.db")

cursor = conn.cursor()

assets_data = [
    ("AAPL", "Apple Inc.", "Equity"),
    ("MSFT", "Microsoft Corp.", "Equity"),
    ("BTC", "Bitcoin", "Crypto")] 


query = "INSERT OR IGNORE INTO assets (ticker, asset_name, asset_class) VALUES (?, ?, ?)" 

# load assets ticker, name and class to assets table
cursor.executemany(query, assets_data) 


# loops through the assets and pull up (and load) trade date, close price and volume from yfinance.
for ticker, name, category in assets_data:  

    # fetch the asset_id from assets table to link and then insert to daily_price table
    cursor.execute("SELECT asset_id FROM assets WHERE ticker = ?", (ticker,)) 
    asset_id = cursor.fetchone()[0]  
    
    df = yf.Ticker(ticker).history(start="2025-01-01", end="2026-10-28")
    
    for date, row in df.iterrows(): 
        clean_date = date.strftime("%Y-%m-%d") 
        clean_price = round(row["Close"], 2)
        clean_vol = int(row["Volume"]) 

        # loads asset id, trade date, close price, and volume on the daily_price table
        cursor.execute(
            """
            INSERT OR IGNORE INTO daily_prices (asset_id, trade_date, close_price, volume)
            VALUES (?, ?, ?, ?)
            """,
            (asset_id, clean_date, clean_price, clean_vol)
        ) 
         

conn.commit()
conn.close()
