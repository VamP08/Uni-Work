import pandas as pd
import numpy as np

# PANDAS 
# Creating a DataFrame from the given data
df = pd.read_csv('ASSIGNMENT - 3\studentData.csv')

print(df.head())

it_data = df[df['Department'] == 'IT']
print(it_data)

# To calculate the average percentage:
average_percentage = df['Percentage'].mean()
print("Average Percentage:", average_percentage)

# Extracting 'Percentage' column and converting to a NumPy array
percentages = df['Percentage'].values  


#NUMPY
#Calculating the maximum percentage:
max_percentage = np.max(percentages)
print("Maximum Percentage:", max_percentage)

#Calculating the minimum percentage:
min_percentage = np.min(percentages)
print("Minimum Percentage:", min_percentage)

#Calculating the mean (average) percentage:
mean_percentage = np.mean(percentages)
print("Mean Percentage:", mean_percentage)

#Calculating the standard deviation of percentages:
std_deviation = np.std(percentages)
print("Standard Deviation of Percentages:", std_deviation)