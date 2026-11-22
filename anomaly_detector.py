import pandas as pd

data = {'Transaction_ID': range(1, 11),
        'Amount': [100, 110, 105, 95, 102, 98, 108, 92, 100, 850]}
df = pd.DataFrame(data)

mean = df['Amount'].mean()

std = df['Amount'].std()

df['Z_Score'] = (df['Amount'] - mean) / std

anomalies = df[df['Z_Score'].abs() > 2]

print("Detected Anomalies:")
print(anomalies)