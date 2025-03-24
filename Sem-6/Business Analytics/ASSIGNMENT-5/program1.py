import pandas as pd

# Sample data
data = {
    'Product': ['Laptop', 'Tablet', 'Phone', 'Laptop', 'Tablet'],
    'Price': [1200, 300, 450, 1000, 250],
    'Brand': ['Apple', 'Samsung', 'Google', 'HP', 'Lenovo'],
    'Quantity': [5, 10, 15, 8, 12]
}

df = pd.DataFrame(data)

# 1. Exploring Data
print("Exploring Data:")
print(df.head())
print(df.describe())
print(df.dtypes)

# 2. Data Selection
print("\nData Selection:")
print(df['Product'])
print(df[['Product', 'Price']])
print(df.loc[2])

# 3. Filtering Data
print("\nFiltering Data:")
filtered_df = df[df['Price'] > 500]
print(filtered_df)

# 4. Adding Columns
print("\nAdding Columns:")
df['Discount'] = 0.1
df['Final Price'] = df['Price'] * (1 - df['Discount'])
print(df)

# 5. Handling Missing Data
print("\nHandling Missing Data:")
print(df.isnull().sum())
df.fillna(0, inplace=True)
df.dropna(inplace=True)
print(df)

# 6. Sorting
print("\nSorting:")
df.sort_values(by='Price', ascending=False, inplace=True)
df['Price Rank'] = df['Price'].rank(ascending=False)
print(df)

# 7. GroupBy
print("\nGroup By:")
grouped = df.groupby('Brand')['Price'].mean()
print(grouped)

# 8. Merging
print("\nMerging:")
data2 = {
    'Brand': ['Apple', 'Samsung', 'Google', 'HP', 'Lenovo'],
    'Category': ['Electronics', 'Electronics', 'Technology', 'Computers', 'Computers']
}
df2 = pd.DataFrame(data2)
merged_df = pd.merge(df, df2, on='Brand', how='left')
print(merged_df)

# 9. Pivot Table
print("\nPivot Table:")
pivot_table = merged_df.pivot_table(
    values='Quantity',
    index=['Brand', 'Category'],
    aggfunc='sum'
)
print(pivot_table)