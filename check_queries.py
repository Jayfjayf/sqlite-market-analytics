import sqlite3

conn = sqlite3.connect("market.db")
cursor = conn.cursor()

# 1. Read your .sql file
with open("queries.sql", "r") as f: 
    query = f.read()

# 2. Execute and print the first 5 rows
cursor.execute(query)
rows = cursor.fetchmany(100)


for row in rows:
    print(row)

conn.close()