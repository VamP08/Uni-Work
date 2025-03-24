import pandas as pd
from sklearn.preprocessing import MinMaxScaler


# Create a sample dataset
data = {'Name': ['Alice', None, 'Charlie', 'David'],
        'Age': [25, 30, None, 40],
        'Salary': ['50000', '60000', '70000', '80000'],
        'Department': ['HR', 'IT', 'Finance', 'HR']}
df = pd.DataFrame(data)

# Display dataset
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Print data types
print(df.dtypes)

# Fill missing categorical values
df['Name'].fillna("Unknown", inplace=True)

# Fill missing numerical values
df['Age'].fillna(df['Age'].mean(), inplace=True)

print("Updated DataFrame:\n", df)

# Convert Salary to numerical
df['Salary'] = df['Salary'].astype(float)

print(df.dtypes)

df = pd.get_dummies(df, columns=['Department'], drop_first=True)
print("Encoded DataFrame:\n", df)

scaler = MinMaxScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

print("Normalized DataFrame:\n", df)

# Load Titanic dataset
titanic = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Handling missing values
titanic['Age'].fillna(titanic['Age'].mean(), inplace=True)
titanic['Embarked'].fillna(titanic['Embarked'].mode()[0], inplace=True)

# Encoding categorical columns
titanic = pd.get_dummies(titanic, columns=['Sex', 'Embarked'], drop_first=True)

# Normalizing numerical columns
titanic[['Fare', 'Age']] = scaler.fit_transform(titanic[['Fare', 'Age']])

print(titanic.head())
