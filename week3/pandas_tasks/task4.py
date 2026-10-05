
import pandas as pd
df = pd.read_csv("data/Cars93_missing.csv")
print("column names:")
print(list(df.columns))
print("missing values:")
print(df.isnull().sum())
print("total missing values:")
print(df.isnull().sum().sum())