import json
import pandas as pd

raw_json = """
[
    {"order_id": 101, "customer": {"name": "Amit", "tier": "Enterprise"}, "amount": 1500},
    {"order_id": 102, "customer": {"name": "Neha", "tier": "SMB"}, "amount": 400},
    {"order_id": 103, "customer": {"name": "Priya", "tier": "Enterprise"}, "amount": 2200},
    {"order_id": 104, "customer": {"name": "Rohan", "tier": "SMB"}, "amount": 600}
]
"""

records = json.loads(raw_json)

df = pd.json_normalize(records)

summary = df.groupby('customer.tier')['amount'].agg(['mean', 'sum'])

print(df)
print("\nTier Summary:")
print(summary)