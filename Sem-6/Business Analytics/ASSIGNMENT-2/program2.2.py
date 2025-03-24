import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:\n", df)

# Accessing specific columns
print("Names:\n", df['Name'])

# Descriptive statistics
print("Statistics:\n", df.describe())

# Adding a new column
df['Bonus'] = df['Salary'] * 0.1
print("Updated DataFrame:\n", df)
