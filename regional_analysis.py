import pandas as pd
import io

raw_data = """Region,Product,Revenue,Cost
West,Laptop,1200,850
West,Mouse,150,50
North,Laptop,1100,850
North,Keyboard,300,120
South,Monitor,700,400
South,Mouse,200,50
West,Keyboard,350,120"""

df = pd.read_csv(io.StringIO(raw_data))
df['Profit'] = df['Revenue'] - df['Cost']
summary = df.groupby('Region')[['Revenue', 'Profit']].sum()
summary = summary.sort_values(by='Profit', ascending=False)
summary.to_csv('regional_report.csv')

print(summary)
print("\nExport complete: regional_report.csv saved to Desktop.")
