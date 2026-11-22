import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('regional_report.csv')

plt.bar(df['Region'], df['Profit'], color='steelblue')

plt.title('Regional Net Profit')
plt.xlabel('Region')
plt.ylabel('Profit ($)')

plt.savefig('regional_profit_chart.png')

print("Chart generated: regional_profit_chart.png saved to Desktop.")