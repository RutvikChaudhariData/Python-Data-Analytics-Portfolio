import pandas as pd

data = {
    'Region': ['West', 'West', 'North', 'North', 'South', 'South', 'West', 'North'],
    'Product': ['Laptop', 'Mouse', 'Laptop', 'Mouse', 'Laptop', 'Mouse', 'Laptop', 'Mouse'],
    'Revenue': [1200, 150, 1100, 200, 1300, 100, 1250, 180]
}
df = pd.DataFrame(data)

pivot = pd.pivot_table(df, values='Revenue', index='Region', columns='Product', aggfunc='sum', fill_value=0)

pivot['Total'] = pivot.sum(axis=1)

print(pivot)