import pandas as pd
import numpy as np

# Create a dataset
data = {
    'CarModel': ['Sedan', 'SUV', 'Truck', 'Hatchback', 'Sedan', 'SUV', 'Truck', 'Hatchback'],
    'Horsepower': [150, 200, 250, 120, 180, 220, 280, 150],
    'FuelEfficiency': [25, 18, 15, 30, 22, 17, 14, 28]
}

df = pd.DataFrame(data)

# Encoding categorical variable (CarModel)
df['CarModelEncoded'] = df['CarModel'].astype('category').cat.codes

# Binning numerical variable (Horsepower)
bins = [0, 150, 200, 250, np.inf]
labels = ['Low', 'Medium', 'High', 'Very High']
df['HorsepowerCategory'] = pd.cut(df['Horsepower'], bins=bins, labels=labels)

# Save the dataset to a CSV file
df.to_csv('car_dataset.csv', index=False)

print("Dataset created and saved as 'car_dataset.csv':\n", df)
