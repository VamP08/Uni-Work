import pandas as pd
import numpy as np

path = 'ASSIGNMENT - 9/Iris_data_sample.csv'

# Importing data
data_csv=pd.read_csv(path)
print("Original Data - ")
print(data_csv)

#Remove Extra Column [that creates new index column]
data_csv=pd.read_csv(path,index_col=0)
print("Removed extra Columns - ")
print(data_csv)

# convert Junk values to NA values
data_csv=pd.read_csv(path,index_col=0, na_values=["??"])
print("\nData after converting junk values to NA -")
print(data_csv)

