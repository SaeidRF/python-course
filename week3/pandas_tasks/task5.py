import pandas as pd
df = pd.read_csv("data/Cars93_missing.csv")
def swap_columns(frame, c1, c2):
    cols = list(frame.columns)
    i, j = cols.index(c1), cols.index(c2)
    cols[i], cols[j] = cols[j], cols[i]
    return frame[cols]

print(swap_columns(df, "Manufacturer", "Model").head())
print(df.sort_index(axis=1).head())   