import numpy as np

n_A, conv_A = 1000, 120
n_B, conv_B = 1000, 155

p_A = conv_A / n_A
p_B = conv_B / n_B

p_pool = (conv_A + conv_B) / (n_A + n_B)

se = np.sqrt(p_pool * (1 - p_pool) * (1/n_A + 1/n_B))

z_score = (p_B - p_A) / se

print(f"Control Rate: {p_A:.2%} | Variant Rate: {p_B:.2%}")
print(f"Z-Score: {z_score:.4f}")
print("Statistically Significant (95% CI):", abs(z_score) > 1.96)