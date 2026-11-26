import pandas as pd

data = {
    'Date': ['2026-01-01', '2026-01-02', '2026-01-03', '2026-01-04', '2026-01-05', '2026-01-06', '2026-01-07'],
    'Revenue': [100, 140, 120, 160, 150, 190, 210]
}
df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

df['SMA_3'] = df['Revenue'].rolling(window=3).mean()

df['Daily_Growth_Pct'] = df['Revenue'].pct_change() * 100

print(df.round(2))