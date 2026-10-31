import sqlite3

conn = sqlite3.connect('market.db') 
cursor = conn.cursor() 

sql_schema = """
CREATE TABLE IF NOT EXISTS assets (
    asset_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL UNIQUE,
    asset_name TEXT NOT NULL,
    asset_class TEXT NOT NULL
); 

CREATE TABLE IF NOT EXISTS daily_prices (
    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    asset_id INTEGER NOT NULL,
    trade_date TEXT NOT NULL,
    close_price REAL NOT NULL,
    volume INTEGER,
    FOREIGN KEY (asset_id) REFERENCES assets (asset_id),
    UNIQUE(asset_id, trade_date)
);
"""
cursor.executescript(sql_schema) 
conn.commit()
conn.close() 
