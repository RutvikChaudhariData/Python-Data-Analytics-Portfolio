import pandas as pd
import io

raw_data = """City,Sales
Ahmedabad,750
Surat,300
Surat,300
Rajkot,
Vadodara,600"""

df = pd.read_csv(io.StringIO(raw_data))

df = df.drop_duplicates()

df['Sales'] = df['Sales'].fillna(df['Sales'].mean())

total_sales = df['Sales'].sum()

print(df)
print(f"Total Cleaned Sales: {total_sales}")
