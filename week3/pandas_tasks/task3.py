import pandas as pd
df = pd.read_csv("data/Cars93_missing.csv")
df.loc[df["Price"] < 10, "Price"] = 10
print(df[["Make", "Price"]].head(25))