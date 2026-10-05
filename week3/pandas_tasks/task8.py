import pandas as pd
df1 = pd.DataFrame({"id": [1, 2, 3, 4], "name": ["Ali", "Sara", "Reza", "Maryam"]})
df2 = pd.DataFrame({"id": [1, 2, 3, 4], "score": [90, 85, 70, 60]})
merged_df = pd.merge(df1, df2, on="id")
print("merged dataframe: ")
print(merged_df)
df1["score"] = df2["score"]
print("dataFrame with new column: ")
print(df1)