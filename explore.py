import pandas as pd

df = pd.read_csv("data/retail_sales.csv")

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# Exercise 2: Filter orders from the South
south = df[df["region"] == "South"]

print("\nSouth order count:", len(south))
print(south.head())