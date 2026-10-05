import pandas as pd
df = pd.read_csv("data/Cars93_missing.csv")
df_indexed = df.set_index("Make")
print(df_indexed.head())
