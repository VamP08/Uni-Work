import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Load the dataset
df = pd.read_csv('ASSIGNMENT - 5\House_Pricing.csv')

# Display basic information about the dataset
print("Original dataset info:")
print(df.info())

# Handling missing values
# Drop rows with missing values for simplicity (you may choose a more sophisticated approach)
df_cleaned = df.dropna()

# Remove duplicates
df_cleaned = df_cleaned.drop_duplicates()

# Address outliers using Z-score
z_scores = zscore(df_cleaned['Price'])
df_cleaned = df_cleaned[(z_scores < 3)]

# Visualize the distribution of SalePrice before and after cleaning
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(df['Price'], bins=30, kde=True)
plt.title('Distribution of SalePrice (Before Cleaning)')
plt.subplot(1, 2, 2)
sns.histplot(df_cleaned['Price'], bins=30, kde=True)
plt.title('Distribution of SalePrice (After Cleaning)')
plt.show()

# Display cleaned dataset information
print("\nCleaned dataset info:")
print(df_cleaned.info())

# Save the cleaned dataset to a new CSV file
df_cleaned.to_csv("cleaned_houseprice_data.csv", index=False)