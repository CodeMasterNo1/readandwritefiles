import pandas as pd

# read the sales CSV file
df = pd.read_csv("sales.csv")

# add the subtotal, freight, and tax for each line
df["GrandTotal"] = df["SubTotal"] + df["TaxAmt"] + df["Freight"]


# group the data by customer and calculate the grand total for each customer
df = df.groupby("CustomerID")["GrandTotal"].sum().reset_index()

# round the total to 2 decimal places
df["GrandTotal"] = df["GrandTotal"].round(2)

# write the result to a new CSV file
df.to_csv("sales_total.csv", index=False)
