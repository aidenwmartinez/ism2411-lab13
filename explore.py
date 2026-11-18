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

# Exercise 3: Find the five orders with the highest revenue
top_five = df.sort_values("revenue", ascending=False).head(5)

print("\nTop five orders by revenue:")
print(top_five)

# Exercise 4: Filter by region and revenue
big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]

print("\nSouth orders over $1,000:", len(big_south))
print(big_south.head())

# Exercise 5: Calculate the price per unit for each order
df["per_unit"] = df["revenue"] / df["quantity"]

print("\nFirst five orders with price per unit:")
print(df.head())
print("Average price per unit:", df["per_unit"].mean())