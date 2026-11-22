import pandas as pd

customers = pd.DataFrame({
    'Customer_ID': [101, 102, 103, 104],
    'Tier': ['Enterprise', 'SMB', 'Enterprise', 'SMB']
})

orders = pd.DataFrame({
    'Order_ID': [1, 2, 3, 4, 5],
    'Customer_ID': [101, 102, 101, 103, 104],
    'Amount': [1500, 300, 2000, 1200, 450]
})

merged = pd.merge(orders, customers, on='Customer_ID', how='inner')

summary = merged.groupby('Tier')['Amount'].agg(['sum', 'count'])

print(summary)