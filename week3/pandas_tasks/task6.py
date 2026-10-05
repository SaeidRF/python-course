import pandas as pd
df = pd.read_csv("data/Cars93_missing.csv")
print("row count:",len(df))
low, high = df["Price"].quantile([0.05, 0.95])
df = df[(df["Price"] >= low) & (df["Price"] <= high)]
print("row count after removing 5%:",len(df))