import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Load the dataset
df = pd.read_csv('ASSIGNMENT - 6\Salary_Data.csv')
print(df.head())

# Data Cleaning
# Handling missing values (replace NaN with the mean for numerical columns)
df.fillna(df.mean(), inplace=True)

# Removing outliers using Z-score method
z_scores = zscore(df[['Salary', 'YearsExperience']])
df_no_outliers = df[(z_scores < 3).all(axis=1)]
# Keep only rows where z-scores are less than 3

# Visualize the distribution of Salary after cleaning
plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
plt.boxplot(df_no_outliers['Salary'])
plt.title('Boxplot of Salary (Cleaned)')

# Visualize the distribution of Years of Experience after cleaning
plt.subplot(1, 2, 2)
plt.boxplot(df_no_outliers['YearsExperience'])
plt.title('Boxplot of Years of Experience (Cleaned)')
plt.show()

# Display the cleaned dataset
print("Original dataset shape:", df.shape)
print("Cleaned dataset shape:", df_no_outliers.shape)

# Save the cleaned dataset to a new CSV file
df_no_outliers.to_csv("cleaned_employee_data.csv", index=False)
