import sqlite3
import pandas as pd

data = {
    'Region': ['West', 'West', 'West', 'North', 'North', 'South', 'South'],
    'Rep': ['Amit', 'Priya', 'Rohan', 'Neha', 'Karan', 'Meera', 'Dev'],
    'Sales': [1500, 2200, 1800, 1900, 1400, 2100, 1600]
}
df = pd.DataFrame(data)
conn = sqlite3.connect(':memory:')
df.to_sql('rep_sales', conn, index=False)

query = """
SELECT
    Region,
    Rep,
    Sales,
    RANK() OVER (PARTITION BY Region ORDER BY Sales DESC) AS Region_Rank,
    SUM(Sales) OVER (PARTITION BY Region) AS Region_Total
FROM rep_sales
"""
result = pd.read_sql_query(query, conn)

print(result)
conn.close()