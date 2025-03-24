import pandas as pd

df_excel = pd.read_excel("sales_data.xlsx")
print(df_excel.head())

product_summary = df_excel.groupby("Product").agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Revenue=("Revenue", "sum")
).reset_index()

output_file_path = "product_summary.xlsx"
product_summary.to_excel(output_file_path, index=False)

print(f"\nProduct summary saved to '{output_file_path}' successfully!")