import pandas as pd
import json

inventory_df = pd.read_csv("inventory.csv")
print(inventory_df.head(),"\n")

with open("sales.json", "r") as file:
    sales_data = json.load(file)
    print(sales_data)
sales_df = pd.DataFrame(sales_data)

consolidated_df = pd.merge(inventory_df, sales_df, on="ProductID")

output_excel_path = "inventory_sales_summary.xlsx"
consolidated_df.to_excel(output_excel_path, index=False)

print(f"\nConsolidated data saved to '{output_excel_path}'.")