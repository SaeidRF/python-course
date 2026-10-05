import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/Cars93_missing.csv")
df.hist(figsize=(12, 10), bins=10, edgecolor="black")
plt.tight_layout()
plt.show()