import sqlite3
import pandas as pd

df = pd.read_csv('regional_report.csv')
conn = sqlite3.connect(':memory:')
df.to_sql('sales_table', conn, index=False)

query = """
SELECT Region, Profit
FROM sales_table
WHERE Profit > 440
ORDER BY Profit DESC
"""

result = pd.read_sql_query(query, conn)

print(result)
conn.close()