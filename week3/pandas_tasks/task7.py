import pandas as pd
df = pd.read_csv("data/Cars93_missing.csv")
df["Price"] = df["Price"].fillna(df["Price"].mean())
print("missing values in 'Price' column:",df["Price"].isnull().sum())