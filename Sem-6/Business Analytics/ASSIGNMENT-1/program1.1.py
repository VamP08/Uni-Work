import pandas as pd;

# Read the csv
df=pd.read_csv('exercise.csv')
print("Data Imported",df.head())

# Filter exercise data where duration of exercise is greater than 20 minutes
print("Count before Filtering -",df.shape[0])
df = df[df['Duration']>20]
print("Count after Filtering -",df.shape[0])

# Export filtered data to new CSV File
df.to_csv("updated_exercise.csv",index=False)
print("Data Exported",df.head())