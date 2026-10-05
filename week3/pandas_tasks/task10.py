import pandas as pd

df = pd.read_csv("data/Cars93_missing.csv")
corr_matrix = df.corr(numeric_only=True)
print("correlation matrix")
print(corr_matrix)
