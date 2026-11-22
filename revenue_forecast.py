import numpy as np
import pandas as pd

data = {'Ad_Spend': [100, 200, 300, 400, 500],
        'Revenue': [1200, 2100, 3150, 4050, 5100]}
df = pd.DataFrame(data)

r = df['Ad_Spend'].corr(df['Revenue'])

m, b = np.polyfit(df['Ad_Spend'], df['Revenue'], 1)

forecast = m * 750 + b

print(f"Correlation (r): {r:.4f}")
print(f"Equation: Revenue = {m:.2f} * Ad_Spend + {b:.2f}")
print(f"Forecast at $750 Ad Spend: ${forecast:.2f}")